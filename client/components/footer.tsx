import React from "react";
import Link from "next/link";
import { SocialIcon } from "react-social-icons";
import "../styles/Footer.scss";

const Footer = () => {
  return (
    <footer className="Footer">
      <hr />
      <div className="footer-wrapper">
        <div className="footer-links">
          <Link className="u-link" href="/">Home</Link>
          <Link className="u-link" href="/pages/pricing">Pricing</Link>
          <Link className="u-link" href="/pages/account">Account</Link>
          <Link className="u-link" href="/pages/register">Register</Link>
        </div>
        <div className="socials">
          <SocialIcon url="https://x.com" aria-label="X" className="social-icon"/>
          <SocialIcon url="https://discord.com" aria-label="Discord" className="social-icon"/>
          <SocialIcon url="https://substack.com" aria-label="Substack" className="social-icon"/>
          <SocialIcon url="https://github.com" aria-label="GitHub" className="social-icon"/>
        </div>
      </div>
    </footer>
  );
};

export default Footer;