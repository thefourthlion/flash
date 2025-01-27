"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { initFirebase } from "@/firebase";
import { getAuth, updateProfile } from "firebase/auth";
import { getCheckoutUrl, getPortalUrl } from "./stripePayment";
import { getSubscriptionStatus } from "./getPremiumStatus";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@nextui-org/button";
import { Input } from "@nextui-org/input";
import { Textarea } from "@nextui-org/input";
import "../../../styles/Account.scss";

export default function AccountPage() {
  const app = initFirebase();
  const auth = getAuth(app);
  const router = useRouter();

  // State declarations
  const [userName, setUserName] = useState<string | null>(null);
  const [email, setEmail] = useState<string | null>(null);
  const [subscriptions, setSubscriptions] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [bio, setBio] = useState<string>("");
  const [isEditing, setIsEditing] = useState(false);
  const [newUserName, setNewUserName] = useState<string>("");
  const [newBio, setNewBio] = useState<string>("");
  const [avatarUrl, setAvatarUrl] = useState<string>("");
  const [isUploadingImage, setIsUploadingImage] = useState(false);

  // Load user data
  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged((user) => {
      if (user) {
        setUserName(user.displayName);
        setEmail(user.email);
        setAvatarUrl(user.photoURL || "");
      } else {
        router.push("/pages/login");
      }
      setLoading(false);
    });

    return () => unsubscribe();
  }, [auth, router]);

  // Load subscription data
  useEffect(() => {
    const loadSubscriptions = async () => {
      if (auth.currentUser) {
        const activeSubscriptions = await getSubscriptionStatus(app);
        setSubscriptions(activeSubscriptions);
      }
    };

    loadSubscriptions();
  }, [app, auth.currentUser]);

  const handleImageUpload = async (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    if (!event.target.files || !event.target.files[0]) return;
    setIsUploadingImage(true);

    try {
      const file = event.target.files[0];
      const formData = new FormData();
      formData.append("file", file);
      formData.append("gid", auth.currentUser?.uid || "");

      const response = await fetch("/api/upload", {
        method: "POST",
        body: formData,
      });

      const { url } = await response.json();

      if (auth.currentUser) {
        await updateProfile(auth.currentUser, {
          photoURL: url,
        });
        setAvatarUrl(url);
      }
    } catch (error) {
      console.error("Error uploading image:", error);
    } finally {
      setIsUploadingImage(false);
    }
  };

  const handleUpdateProfile = async () => {
    try {
      if (auth.currentUser) {
        await updateProfile(auth.currentUser, {
          displayName: newUserName || userName,
        });
        setBio(newBio);
        setIsEditing(false);
        setUserName(newUserName);
      }
    } catch (error) {
      console.error("Error updating profile:", error);
    }
  };

  const handleSignOut = async () => {
    try {
      await auth.signOut();
      router.push("/pages/login");
    } catch (error) {
      console.error("Error signing out:", error);
    }
  };

  const handleUpgradeToSubscription = async (priceId: string) => {
    const checkoutUrl = await getCheckoutUrl(app, priceId);
    router.push(checkoutUrl);
  };

  const handleManageSubscription = async () => {
    const portalUrl = await getPortalUrl(app);
    router.push(portalUrl);
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="page">
      <div className="account-container">
        <div className="profile-section">
          <div className="avatar-section">
            <Avatar className="w-24 h-24">
              <AvatarImage src={avatarUrl} />
              <AvatarFallback>{userName?.charAt(0) || "U"}</AvatarFallback>
            </Avatar>
            <Input
              type="file"
              accept="image/*"
              className="hidden"
              id="avatar-upload"
              onChange={handleImageUpload}
              disabled={isUploadingImage}
            />
            <Button
              color="primary"
              variant="ghost"
              onClick={() => document.getElementById("avatar-upload")?.click()}
              disabled={isUploadingImage}
            >
              {isUploadingImage ? "Uploading..." : "Change Avatar"}
            </Button>
          </div>

          {isEditing ? (
            <div className="edit-profile">
              <Input
                placeholder="Username"
                value={newUserName}
                onChange={(e) => setNewUserName(e.target.value)}
              />
              <Textarea
                placeholder="Bio"
                value={newBio}
                onChange={(e) => setNewBio(e.target.value)}
              />
              <div className="edit-actions">
                <Button
                  color="primary"
                  variant="ghost"
                  onClick={handleUpdateProfile}
                >
                  Save
                </Button>
                <Button
                  className="red-outline-button"
                  onClick={() => setIsEditing(false)}
                >
                  Cancel
                </Button>
              </div>
            </div>
          ) : (
            <div className="profile-info">
              <h2>{userName}</h2>
              <p className="email">{email}</p>
              <p className="bio">{bio || "No bio yet"}</p>
              <Button
                onClick={() => {
                  setIsEditing(true);
                  setNewUserName(userName || "");
                  setNewBio(bio);
                }}
                color="primary"
                variant="ghost"
              >
                Edit Profile
              </Button>
            </div>
          )}

          <div className="subscription-section">
            <h3>Available Plans</h3>
            <div className="plans-grid">
              <Button
                onClick={() => handleUpgradeToSubscription("price_basic")}
                color="primary"
                variant="ghost"
              >
                Basic Plan - $6/month
              </Button>
              <Button
                onClick={() => handleUpgradeToSubscription("price_premium")}
                color="primary"
                variant="ghost"
              >
                Premium Plan - $12/month
              </Button>
              <Button
                onClick={() => handleUpgradeToSubscription("price_extra")}
                color="primary"
              >
                Extra Plan - $18/month
              </Button>
            </div>
            <Button
              onClick={handleManageSubscription}
              className="red-outline-button"
            >
              Manage Subscription
            </Button>
          </div>

          <Button className="red-button" onClick={handleSignOut}>
            Sign Out
          </Button>
        </div>
      </div>
    </div>
  );
}