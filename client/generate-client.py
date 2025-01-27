#!/usr/bin/env python3

import os.path
from os import path
import os

# ----------------------------------------- Set according to directory - var ----------------------------
current_path = os.getcwd()

# ------------------------------------------- Helper functions ---------------------------------------------
def write_to_file(path, content):
    file = open(path, "w", encoding="utf-8")
    file.write(content)
    file.close()

def create_file_if_not_exists(file_path, content):
    if not path.exists(file_path):
        try:
            write_to_file(file_path, content)
            print(f"✅ {os.path.basename(file_path)} successfully created...")
        except:
            print(f"❌ Something went wrong when creating {os.path.basename(file_path)}...")
    else:
        print(f"ℹ️ {os.path.basename(file_path)} already exists, skipping...")

# ------------------------------------------- File contents ---------------------------------------------
tsconfig_content = '''{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}'''

tailwind_config_content = '''import {nextui} from '@nextui-org/theme'

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-sans)"],
        mono: ["var(--font-mono)"],
      },
    },
  },
  darkMode: "class",
  plugins: [nextui()],
}'''

sitemap_generator_content = '''const sitemap = require("nextjs-sitemap-generator");
sitemap({
  baseUrl: "https://next-app.com/",
  ignoredPaths: ["admin", "login"],
  ignoredExtensions: [
    "js",
    "map",
    "json",
    "png",
    "jpeg",
    "jpg",
    "svg",
    "icon",
    "mp4",
  ],
  extraPaths: ["/extraPath"],
  pagesDirectory: __dirname + "/.next/server/pages",
  targetDirectory: "public/",
  sitemapFilename: "sitemap.xml",
  nextConfigPath: __dirname + "/next.config.js",
});'''

postcss_config_content = '''module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}'''

package_json_content = '''{
  "name": "next-app-template",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "dev": "next dev --turbopack",
     "build": "next build --no-lint",
    "start": "next start",
    "lint": "eslint . --ext .ts,.tsx -c .eslintrc.json --fix"
  },
  "dependencies": {
    "@google-cloud/storage": "^7.14.0",
    "@nextui-org/button": "^2.2.3",
    "@nextui-org/card": "^2.2.7",
    "@nextui-org/code": "2.2.3",
    "@nextui-org/form": "^2.1.6",
    "@nextui-org/input": "^2.4.6",
    "@nextui-org/kbd": "2.2.3",
    "@nextui-org/link": "2.2.3",
    "@nextui-org/listbox": "2.3.3",
    "@nextui-org/navbar": "2.2.3",
    "@nextui-org/snippet": "2.2.4",
    "@nextui-org/switch": "2.2.3",
    "@nextui-org/system": "2.4.3",
    "@nextui-org/theme": "2.4.1",
    "@radix-ui/react-avatar": "^1.1.1",
    "@react-aria/ssr": "3.9.7",
    "@react-aria/visually-hidden": "3.8.18",
    "axios": "^1.7.9",
    "bootstrap": "^5.3.3",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "firebase": "^11.0.2",
    "framer-motion": "11.13.1",
    "intl-messageformat": "^10.5.0",
    "lucide-react": "^0.468.0",
    "next": "15.0.4",
    "next-themes": "^0.4.4",
    "nextjs-sitemap-generator": "^1.3.1",
    "react": "18.3.1",
    "react-bootstrap": "^2.10.6",
    "react-dom": "18.3.1",
    "react-firebase-hooks": "^5.1.1",
    "react-social-icons": "^6.18.0",
    "react-social-login-buttons": "^4.1.0",
    "sass": "^1.82.0",
    "tailwind-merge": "^2.5.5",
    "tailwindcss-animate": "^1.0.7"
  },
  "devDependencies": {
    "@next/eslint-plugin-next": "15.0.4",
    "@react-types/shared": "3.25.0",
    "@types/node": "20.5.7",
    "@types/react": "18.3.3",
    "@types/react-dom": "18.3.0",
    "@typescript-eslint/eslint-plugin": "8.11.0",
    "@typescript-eslint/parser": "8.11.0",
    "autoprefixer": "^10.4.19",
    "eslint": "^8.57.0",
    "eslint-config-next": "15.0.4",
    "eslint-config-prettier": "9.1.0",
    "eslint-plugin-import": "^2.26.0",
    "eslint-plugin-jsx-a11y": "^6.4.1",
    "eslint-plugin-node": "^11.1.0",
    "eslint-plugin-prettier": "5.2.1",
    "eslint-plugin-react": "^7.23.2",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-unused-imports": "4.1.4",
    "postcss": "^8.4.49",
    "prettier": "3.3.3",
    "tailwind-variants": "^0.1.20",
    "tailwindcss": "^3.4.16",
    "typescript": "5.6.3"
  }
}
'''

next_config_content = '''/** @type {import('next').NextConfig} */
const nextConfig = {
    output: 'standalone',
};

module.exports = nextConfig;'''

next_env_content = '''/// <reference types="next" />
/// <reference types="next/image-types/global" />

// NOTE: This file should not be edited
// see https://nextjs.org/docs/app/building-your-application/configuring/typescript for more information.'''

firebase_content = '''// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyBXIwZtbJwfTVWrXB3VAGNMakcb4ayfWRk",
    authDomain: "general-2ed6c.firebaseapp.com",
    projectId: "general-2ed6c",
    storageBucket: "general-2ed6c.appspot.com",
    messagingSenderId: "435839427932",
    appId: "1:435839427932:web:a0129a5f945d87cdc98d99",
    measurementId: "G-0HK7RN392Z"
  };

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export default app;

export const initFirebase = () => {
  return app;
};'''

dockerfile_content = '''# Base image
FROM node:18-alpine AS base
WORKDIR /app

# Dependencies stage
FROM base AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine
RUN apk add --no-cache libc6-compat

# Copy package files
COPY package.json package-lock.json* ./
RUN npm ci

# Builder stage
FROM base AS builder
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Build the application
ENV NEXT_TELEMETRY_DISABLED 1
RUN npm run build

# Runner stage
FROM base AS runner
WORKDIR /app

ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public

# Set the correct permission for prerender cache
RUN mkdir .next
RUN chown nextjs:nodejs .next

# Automatically leverage output traces to reduce image size
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT 3000
ENV HOSTNAME "0.0.0.0"

CMD ["node", "server.js"]'''

docker_compose_content = '''version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    restart: always
    # Add healthcheck
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000"]
      interval: 30s
      timeout: 10s
      retries: 3'''

components_json_content = '''{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "styles/globals.scss",
    "baseColor": "zinc",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}'''

gitignore_content = '''# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# local env files
.env*.local

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts'''

eslintrc_content = '''{
  "$schema": "https://json.schemastore.org/eslintrc.json",
  "env": {
    "browser": false,
    "es2021": true,
    "node": true
  },
  "extends": [
    "plugin:react/recommended",
    "plugin:prettier/recommended",
    "plugin:react-hooks/recommended",
    "plugin:jsx-a11y/recommended",
    "plugin:@next/next/recommended"
  ],
  "plugins": [
    "react",
    "unused-imports",
    "import",
    "@typescript-eslint",
    "jsx-a11y",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaFeatures": {
      "jsx": true
    },
    "ecmaVersion": 12,
    "sourceType": "module"
  },
  "settings": {
    "react": {
      "version": "detect"
    }
  },
  "rules": {
    "no-console": "warn",
    "react/prop-types": "off",
    "react/jsx-uses-react": "off",
    "react/react-in-jsx-scope": "off",
    "react-hooks/exhaustive-deps": "off",
    "jsx-a11y/click-events-have-key-events": "warn",
    "jsx-a11y/interactive-supports-focus": "warn",
    "prettier/prettier": [
      "warn",
      {
        "endOfLine": "auto"
      }
    ],
    "no-unused-vars": "off",
    "unused-imports/no-unused-vars": "off",
    "unused-imports/no-unused-imports": "warn",
    "@typescript-eslint/no-unused-vars": [
      "warn",
      {
        "args": "after-used",
        "ignoreRestSiblings": false,
        "argsIgnorePattern": "^_.*?$"
      }
    ],
    "import/order": "warn",
    "react/self-closing-comp": "warn",
    "react/jsx-sort-props": "warn",
    "padding-line-between-statements": "warn"
  }
}

'''

eslintignore_content = '''.now/*
*.css
.changeset
dist
esm/*
public/*
tests/*
scripts/*
*.config.js
.DS_Store
node_modules
coverage
.next
build
!.commitlintrc.cjs
!.lintstagedrc.cjs
!jest.config.js
!plopfile.js
!react-shim.js
!tsup.config.ts'''

dockerignore_content = '''node_modules
.next
.git
.env*.local
npm-debug.log*
yarn-debug.log*
yarn-error.log*
README.md
.dockerignore
Dockerfile
docker-compose.yml'''

env_content = '''STRIPE_PRODUCT_ID=prod_example
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=http://localhost:3002

GOOGLE_CLOUD_PROJECT_ID=example-project-id
GOOGLE_CLOUD_CLIENT_EMAIL=example@example.iam.gserviceaccount.com
GOOGLE_CLOUD_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----"
GOOGLE_CLOUD_BUCKET_NAME=example-bucket-name'''

types_index_content = '''import { SVGProps } from "react";

export type IconSvgProps = SVGProps<SVGSVGElement> & {
  size?: number;
};'''

# Add style content constants
styles_variables_content = '''$primary-color: #167c93;
$shadow-color: rgba(16, 28, 42, 0.1);

$secondary-color: #bfd4b7;
$background-color: #1B1B20;
$foreground-color: grey;
$border-color: rgb(106, 111, 129);
$border-shadow-color: rgba(252, 70, 100, 0.2);
$text-color: #ababae;
$card-color: #202028;

$box-shadow-color: rgba(0, 0, 0, 0.1);
$btn-border-color: rgb(222, 226, 230);

$red: rgb(252, 70, 100);
$green: #2b8c44;

$pastel-teal:#78BFB8;
$pastel-teal-dark:#5BA69E;


$pastel-blue:#A6D8DB;
$pastel-blue-dark:#639FA6;

$pastel-pink: #f3a3a3;
$pastel-pink-dark: #ed8b8b;

$pastel-orange: #f6c17a;
$pastel-orange-dark: #fba454;

$pastel-red: #f25430;
$pastel-red-dark: #d94b2c;

$pastel-green: #97BF6F;
$pastel-green-dark: #578C3E; 


$blackish: #1B1B20;
$greyish: #202028;
$grey:#4B4B54;
$h-font:#9c9ca4;

// ------------------- pastel colors

// #A7DCC7
// #3FA693
// #CFF2B8
// #9FBFA1

// #78BFB8
// #5BA69E

// #027373
// #025959

// #66B8CC
// #62A2B3

// #A6D8DB
// #639FA6

// #C6ADFF
// #BD9CF9

// #FEF2CD
// #FFE7AD

// #F2AA52
// #F29C50

// #F6C17A
// #FBA454

// #FEB1A9
// #FFB7AD

// #FFADCB

// #F25430
// #F24738

// #F25A64
// #FF545A
// #D94C43
// #A62D35

// #B91E3C
// #8C192D
'''

styles_globals_content = '''@import "./Variables.scss";
@tailwind base;
@tailwind components;
@tailwind utilities;

@import url("https://fonts.googleapis.com/css2?family=Sofia+Sans:ital,wght@0,100..1000;1,100..1000&display=swap");

*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Sofia Sans", sans-serif;
  font-weight: 600 !important;
  h1 {
    font-weight: bold;
    font-size: 2.5rem;
  }

  h2 {
    font-weight: bold;
    font-size: 2rem;
  }

  h3 {
    font-weight: bold;
    font-size: 1.75rem;
  }

  h4 {
    font-weight: bold;
    font-size: 1.5rem;
  }
}

.page {
  margin-bottom: 50px;
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
}

.content-header {
  font-weight: bold;
  margin: 25px 0;
}

.u-link{
  text-decoration: underline;
}

// ----------------------------------------------- buttons -----------------------------------------
.primary-btn,
.red-button,
.green-button
 {
  width: 100%;
  cursor: pointer;
  position: relative;
  text-decoration: none;
  overflow: hidden;
  z-index: 1;
}

.social-sign-in-btn{
  width: 100% !important;
  position: relative;
  right: 6px;
}

.red-button {
  background-color: $pastel-red;
  border: 3px solid $pastel-red;
}

.red-button:hover {
  background-color: $pastel-red-dark;
  border: 3px solid $pastel-red-dark;
}

.red-outline-button {
  background-color: transparent;
  border: 3px solid $pastel-red;
  color: $pastel-red;
}

.red-outline-button:hover {
  background-color: transparent;
  border: 3px solid $pastel-red-dark;
  color: $pastel-red-dark;
}

.green-button {
  background-color: $pastel-green;
  border: 3px solid $pastel-green;
}

.green-button:hover {
  background-color: $pastel-green-dark;
  border: 3px solid $pastel-green-dark;
}

.content-container {
  min-width: 350px;
  max-width: 550px;
  padding: 30px;
}

.button-link {
  text-decoration: none;
  color: black !important;
}

'''

styles_account_content = '''@import "./Variables.scss";

.account-container {
  max-width: 800px;
  margin: 0 auto;
  // padding: 2rem;
  
  .profile-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
    
    .avatar-section {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1rem;
    }
    
    .profile-info {
      text-align: center;
      width: 100%;
      max-width: 400px;
      
      h2 {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
      }
      
      .email {
        color: #666;
        margin-bottom: 1rem;
      }
      
      .bio {
        margin-bottom: 1.5rem;
      }
    }
    
    .edit-profile {
      width: 100%;
      max-width: 400px;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      
      .edit-actions {
        display: flex;
        gap: 1rem;
        justify-content: center;
        margin-top: 1rem;
      }
    }
    
    .subscription-section {
      width: 100%;
      text-align: center;
      margin: 2rem 0;
      
      h3 {
        margin-bottom: 1.5rem;
        font-size: 1.25rem;
      }
      
      .plans-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-bottom: 1.5rem;
      }
    }
  }
}

// Responsive adjustments
@media (max-width: 640px) {
  .account-container {
    padding: 1rem;
    margin: 1rem;
    
    .profile-section {
      gap: 1.5rem;
      
      .subscription-section {
        .plans-grid {
          grid-template-columns: 1fr;
        }
      }
    }
  }
}
'''

styles_footer_content = '''@import "./Variables.scss";

.Footer {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 20px;

  hr {
    width: 100vw;
    border: 0;
    height: 1px;
    background-color: $grey;
    margin: 0 0 25px 0;
  }

  .footer-wrapper {
    width: 100%;
    max-width: 1200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 0 25px 0;
  }

  .footer-links {
    display: flex;
    gap: 25px;
    justify-content: center;
    align-items: center;
    margin-bottom: 15px;

    a {
      color: var(--foreground);
       transition: color 0.2s ease;

      &:hover {
        color: var(--primary);
      }
    }
  }

  .socials {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 25px;

    .social-icon {
      width: 45px !important;
      height: 45px !important;
    }
  }

  @media only screen and (max-width: 900px) {
    padding: 0 10px;
    
    .footer-links {
      gap: 15px;
      
      a {
        font-size: 0.85rem;
      }
    }

    .socials {
      gap: 15px;
    }
  }
}
'''

styles_login_content = '''@import "./Variables.scss";

.Login {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
'''

styles_product_content = '''@import "./Variables.scss";

.Product {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 2rem;

  .container {
    padding: 25px 0;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;
    gap: 25px;
    flex-wrap: wrap;
  }

  .sub-card {
    width: 300px;
    min-height: 400px;
    padding: 15px;
    border: 1px solid $border-color !important;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .features {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;

    ul {
      padding-left: 0;
      list-style: none;
    }
  }

  .title{
    font-size: 32px;
    font-weight: bold;
  }

  button{
    margin-top: 25px !important;
  }
}
'''

styles_register_content = '''@import "./Variables.scss";

.Register {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
'''

# Add public content constants
next_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 394 80"><path fill="#000" d="M262 0h68.5v12.7h-27.2v66.6h-13.6V12.7H262V0ZM149 0v12.7H94v20.4h44.3v12.6H94v21h55v12.6H80.5V0h68.7zm34.3 0h-17.8l63.8 79.4h17.9l-32-39.7 32-39.6h-17.9l-23 28.6-23-28.6zm18.3 56.7-9-11-27.1 33.7h17.8l18.3-22.7z"/><path fill="#000" d="M81 79.3 17 0H0v79.3h13.6V17l50.2 62.3H81Zm252.6-.4c-1 0-1.8-.4-2.5-1s-1.1-1.6-1.1-2.6.3-1.8 1-2.5 1.6-1 2.6-1 1.8.3 2.5 1a3.4 3.4 0 0 1 .6 4.3 3.7 3.7 0 0 1-3 1.8zm23.2-33.5h6v23.3c0 2.1-.4 4-1.3 5.5a9.1 9.1 0 0 1-3.8 3.5c-1.6.8-3.5 1.3-5.7 1.3-2 0-3.7-.4-5.3-1s-2.8-1.8-3.7-3.2c-.9-1.3-1.4-3-1.4-5h6c.1.8.3 1.6.7 2.2s1 1.2 1.6 1.5c.7.4 1.5.5 2.4.5 1 0 1.8-.2 2.4-.6a4 4 0 0 0 1.6-1.8c.3-.8.5-1.8.5-3V45.5zm30.9 9.1a4.4 4.4 0 0 0-2-3.3 7.5 7.5 0 0 0-4.3-1.1c-1.3 0-2.4.2-3.3.5-.9.4-1.6 1-2 1.6a3.5 3.5 0 0 0-.3 4c.3.5.7.9 1.3 1.2l1.8 1 2 .5 3.2.8c1.3.3 2.5.7 3.7 1.2a13 13 0 0 1 3.2 1.8 8.1 8.1 0 0 1 3 6.5c0 2-.5 3.7-1.5 5.1a10 10 0 0 1-4.4 3.5c-1.8.8-4.1 1.2-6.8 1.2-2.6 0-4.9-.4-6.8-1.2-2-.8-3.4-2-4.5-3.5a10 10 0 0 1-1.7-5.6h6a5 5 0 0 0 3.5 4.6c1 .4 2.2.6 3.4.6 1.3 0 2.5-.2 3.5-.6 1-.4 1.8-1 2.4-1.7a4 4 0 0 0 .8-2.4c0-.9-.2-1.6-.7-2.2a11 11 0 0 0-2.1-1.4l-3.2-1-3.8-1c-2.8-.7-5-1.7-6.6-3.2a7.2 7.2 0 0 1-2.4-5.7 8 8 0 0 1 1.7-5 10 10 0 0 1 4.3-3.5c2-.8 4-1.2 6.4-1.2 2.3 0 4.4.4 6.2 1.2 1.8.8 3.2 2 4.3 3.4 1 1.4 1.5 3 1.5 5h-5.8z"/></svg>'''

vercel_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 283 64"><path fill="black" d="M141 16c-11 0-19 7-19 18s9 18 20 18c7 0 13-3 16-7l-7-5c-2 3-6 4-9 4-5 0-9-3-10-7h28v-3c0-11-8-18-19-18zm-9 15c1-4 4-7 9-7s8 3 9 7h-18zm117-15c-11 0-19 7-19 18s9 18 20 18c6 0 12-3 16-7l-8-5c-2 3-5 4-8 4-5 0-9-3-11-7h28l1-3c0-11-8-18-19-18zm-10 15c2-4 5-7 10-7s8 3 9 7h-19zm-39 3c0 6 4 10 10 10 4 0 7-2 9-5l8 5c-3 5-9 8-17 8-11 0-19-7-19-18s8-18 19-18c8 0 14 3 17 8l-8 5c-2-3-5-5-9-5-6 0-10 4-10 10zm83-29v46h-9V5h9zM37 0l37 64H0L37 0zm92 5-27 48L74 5h10l18 30 17-30h10zm59 12v10l-3-1c-6 0-10 4-10 10v15h-9V17h9v9c0-5 6-9 13-9z"/></svg>'''

# Add lib content constants
utils_content = '''import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}'''

# Add credentials content constants
credentials_content = '''{
    "type": "service_account",
    "project_id": "realitygenai",
    "private_key_id": "PRIVATE_KEY_ID",
    "private_key": "-----BEGIN PRIVATE KEY-----\\nPRIVATE_KEY_CONTENTS\\n-----END PRIVATE KEY-----\\n",
    "client_email": "realitygen-ai-official@realitygenai.iam.gserviceaccount.com",
    "client_id": "CLIENT_ID",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/realitygen-ai-official%40realitygenai.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}'''

# Add context content constants
user_auth_context_content = '''"use client"; // Add this line to indicate this is a Client Component

import { createContext, useContext, useEffect, useState } from "react";
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  onAuthStateChanged,
  signOut,
  GoogleAuthProvider,
  signInWithPopup,
} from "firebase/auth";
import { auth } from "@/firebase";

const userAuthContext = createContext();

export function UserAuthContextProvider({ children }) {
  const [user, setUser] = useState({});

  function logIn(email, password) {
    return signInWithEmailAndPassword(auth, email, password);
  }

  function signUp(email, password) {
    return createUserWithEmailAndPassword(auth, email, password);
  }

  function logOut() {
    return signOut(auth);
  }

  function googleSignIn() {
    const googleAuthProvider = new GoogleAuthProvider();
    return signInWithPopup(auth, googleAuthProvider);
  }

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
    });

    return () => {
      unsubscribe();
    };
  }, []);

  return (
    <userAuthContext.Provider
      value={{ user, logIn, signUp, logOut, googleSignIn }}
    >
      {children}
    </userAuthContext.Provider>
  );
}

export function useUserAuth() {
  return useContext(userAuthContext);
}'''

# Add config content constants
fonts_content = '''import { Fira_Code as FontMono, Inter as FontSans } from "next/font/google";

export const fontSans = FontSans({
  subsets: ["latin"],
  variable: "--font-sans",
});

export const fontMono = FontMono({
  subsets: ["latin"],
  variable: "--font-mono",
});'''

site_content = '''export type SiteConfig = typeof siteConfig;

export const siteConfig = {
  name: "Website Name",
  description: "Make beautiful websites.",
  links: {
   
  },
};'''

# Add components content constants
footer_content = '''import React from "react";
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

export default Footer;'''

icons_content = '''import * as React from "react";

import { IconSvgProps } from "@/types";

export const Logo: React.FC<IconSvgProps> = ({
  size = 36,
  width,
  height,
  ...props
}) => (
  <svg
    fill="none"
    height={size || height}
    viewBox="0 0 32 32"
    width={size || width}
    {...props}
  >
    <path
      clipRule="evenodd"
      d="M17.6482 10.1305L15.8785 7.02583L7.02979 22.5499H10.5278L17.6482 10.1305ZM19.8798 14.0457L18.11 17.1983L19.394 19.4511H16.8453L15.1056 22.5499H24.7272L19.8798 14.0457Z"
      fill="currentColor"
      fillRule="evenodd"
    />
  </svg>
);

export const DiscordIcon: React.FC<IconSvgProps> = ({
  size = 24,
  width,
  height,
  ...props
}) => {
  return (
    <svg
      height={size || height}
      viewBox="0 0 24 24"
      width={size || width}
      {...props}
    >
      <path
        d="M14.82 4.26a10.14 10.14 0 0 0-.53 1.1 14.66 14.66 0 0 0-4.58 0 10.14 10.14 0 0 0-.53-1.1 16 16 0 0 0-4.13 1.3 17.33 17.33 0 0 0-3 11.59 16.6 16.6 0 0 0 5.07 2.59A12.89 12.89 0 0 0 8.23 18a9.65 9.65 0 0 1-1.71-.83 3.39 3.39 0 0 0 .42-.33 11.66 11.66 0 0 0 10.12 0q.21.18.42.33a10.84 10.84 0 0 1-1.71.84 12.41 12.41 0 0 0 1.08 1.78 16.44 16.44 0 0 0 5.06-2.59 17.22 17.22 0 0 0-3-11.59 16.09 16.09 0 0 0-4.09-1.35zM8.68 14.81a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.93 1.93 0 0 1 1.8 2 1.93 1.93 0 0 1-1.8 2zm6.64 0a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.92 1.92 0 0 1 1.8 2 1.92 1.92 0 0 1-1.8 2z"
        fill="currentColor"
      />
    </svg>
  );
};

export const TwitterIcon: React.FC<IconSvgProps> = ({
  size = 24,
  width,
  height,
  ...props
}) => {
  return (
    <svg
      height={size || height}
      viewBox="0 0 24 24"
      width={size || width}
      {...props}
    >
      <path
        d="M19.633 7.997c.013.175.013.349.013.523 0 5.325-4.053 11.461-11.46 11.461-2.282 0-4.402-.661-6.186-1.809.324.037.636.05.973.05a8.07 8.07 0 0 0 5.001-1.721 4.036 4.036 0 0 1-3.767-2.793c.249.037.499.062.761.062.361 0 .724-.05 1.061-.137a4.027 4.027 0 0 1-3.23-3.953v-.05c.537.299 1.16.486 1.82.511a4.022 4.022 0 0 1-1.796-3.354c0-.748.199-1.434.548-2.032a11.457 11.457 0 0 0 8.306 4.215c-.062-.3-.1-.611-.1-.923a4.026 4.026 0 0 1 4.028-4.028c1.16 0 2.207.486 2.943 1.272a7.957 7.957 0 0 0 2.556-.973 4.02 4.02 0 0 1-1.771 2.22 8.073 8.073 0 0 0 2.319-.624 8.645 8.645 0 0 1-2.019 2.083z"
        fill="currentColor"
      />
    </svg>
  );
};

export const GithubIcon: React.FC<IconSvgProps> = ({
  size = 24,
  width,
  height,
  ...props
}) => {
  return (
    <svg
      height={size || height}
      viewBox="0 0 24 24"
      width={size || width}
      {...props}
    >
      <path
        clipRule="evenodd"
        d="M12.026 2c-5.509 0-9.974 4.465-9.974 9.974 0 4.406 2.857 8.145 6.821 9.465.499.09.679-.217.679-.481 0-.237-.008-.865-.011-1.696-2.775.602-3.361-1.338-3.361-1.338-.452-1.152-1.107-1.459-1.107-1.459-.905-.619.069-.605.069-.605 1.002.07 1.527 1.028 1.527 1.028.89 1.524 2.336 1.084 2.902.829.091-.645.351-1.085.635-1.334-2.214-.251-4.542-1.107-4.542-4.93 0-1.087.389-1.979 1.024-2.675-.101-.253-.446-1.268.099-2.64 0 0 .837-.269 2.742 1.021a9.582 9.582 0 0 1 2.496-.336 9.554 9.554 0 0 1 2.496.336c1.906-1.291 2.742-1.021 2.742-1.021.545 1.372.203 2.387.099 2.64.64.696 1.024 1.587 1.024 2.675 0 3.833-2.33 4.675-4.552 4.922.355.308.675.916.675 1.846 0 1.334-.012 2.41-.012 2.737 0 .267.178.577.687.479C19.146 20.115 22 16.379 22 11.974 22 6.465 17.535 2 12.026 2z"
        fill="currentColor"
        fillRule="evenodd"
      />
    </svg>
  );
};

export const MoonFilledIcon = ({
  size = 24,
  width,
  height,
  ...props
}: IconSvgProps) => (
  <svg
    aria-hidden="true"
    focusable="false"
    height={size || height}
    role="presentation"
    viewBox="0 0 24 24"
    width={size || width}
    {...props}
  >
    <path
      d="M21.53 15.93c-.16-.27-.61-.69-1.73-.49a8.46 8.46 0 01-1.88.13 8.409 8.409 0 01-5.91-2.82 8.068 8.068 0 01-1.44-8.66c.44-1.01.13-1.54-.09-1.76s-.77-.55-1.83-.11a10.318 10.318 0 00-6.32 10.21 10.475 10.475 0 007.04 8.99 10 10 0 002.89.55c.16.01.32.02.48.02a10.5 10.5 0 008.47-4.27c.67-.93.49-1.519.32-1.79z"
      fill="currentColor"
    />
  </svg>
);

export const SunFilledIcon = ({
  size = 24,
  width,
  height,
  ...props
}: IconSvgProps) => (
  <svg
    aria-hidden="true"
    focusable="false"
    height={size || height}
    role="presentation"
    viewBox="0 0 24 24"
    width={size || width}
    {...props}
  >
    <g fill="currentColor">
      <path d="M19 12a7 7 0 11-7-7 7 7 0 017 7z" />
      <path d="M12 22.96a.969.969 0 01-1-.96v-.08a1 1 0 012 0 1.038 1.038 0 01-1 1.04zm7.14-2.82a1.024 1.024 0 01-.71-.29l-.13-.13a1 1 0 011.41-1.41l.13.13a1 1 0 010 1.41.984.984 0 01-.7.29zm-14.28 0a1.024 1.024 0 01-.71-.29 1 1 0 010-1.41l.13-.13a1 1 0 011.41 1.41l-.13.13a1 1 0 01-.7.29zM22 13h-.08a1 1 0 010-2 1.038 1.038 0 011.04 1 .969.969 0 01-.96 1zM2.08 13H2a1 1 0 010-2 1.038 1.038 0 011.04 1 .969.969 0 01-.96 1zm16.93-7.01a1.024 1.024 0 01-.71-.29 1 1 0 010-1.41l.13-.13a1 1 0 011.41 1.41l-.13.13a.984.984 0 01-.7.29zm-14.02 0a1.024 1.024 0 01-.71-.29l-.13-.14a1 1 0 011.41-1.41l.13.13a1 1 0 010 1.41.97.97 0 01-.7.3zM12 3.04a.969.969 0 01-1-.96V2a1 1 0 012 0 1.038 1.038 0 01-1 1.04z" />
    </g>
  </svg>
);

export const HeartFilledIcon = ({
  size = 24,
  width,
  height,
  ...props
}: IconSvgProps) => (
  <svg
    aria-hidden="true"
    focusable="false"
    height={size || height}
    role="presentation"
    viewBox="0 0 24 24"
    width={size || width}
    {...props}
  >
    <path
      d="M12.62 20.81c-.34.12-.9.12-1.24 0C8.48 19.82 2 15.69 2 8.69 2 5.6 4.49 3.1 7.56 3.1c1.82 0 3.43.88 4.44 2.24a5.53 5.53 0 0 1 4.44-2.24C19.51 3.1 22 5.6 22 8.69c0 7-6.48 11.13-9.38 12.12Z"
      fill="currentColor"
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={1.5}
    />
  </svg>
);

export const SearchIcon = (props: IconSvgProps) => (
  <svg
    aria-hidden="true"
    fill="none"
    focusable="false"
    height="1em"
    role="presentation"
    viewBox="0 0 24 24"
    width="1em"
    {...props}
  >
    <path
      d="M11.5 21C16.7467 21 21 16.7467 21 11.5C21 6.25329 16.7467 2 11.5 2C6.25329 2 2 6.25329 2 11.5C2 16.7467 6.25329 21 11.5 21Z"
      stroke="currentColor"
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth="2"
    />
    <path
      d="M22 22L20 20"
      stroke="currentColor"
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth="2"
    />
  </svg>
);

export const NextUILogo: React.FC<IconSvgProps> = (props) => {
  const { width, height = 40 } = props;

  return (
    <svg
      fill="none"
      height={height}
      viewBox="0 0 161 32"
      width={width}
      xmlns="http://www.w3.org/2000/svg"
      {...props}
    >
      <path
        className="fill-black dark:fill-white"
        d="M55.6827 5V26.6275H53.7794L41.1235 8.51665H40.9563V26.6275H39V5H40.89L53.5911 23.1323H53.7555V5H55.6827ZM67.4831 26.9663C66.1109 27.0019 64.7581 26.6329 63.5903 25.9044C62.4852 25.185 61.6054 24.1633 61.0537 22.9582C60.4354 21.5961 60.1298 20.1106 60.1598 18.6126C60.132 17.1113 60.4375 15.6228 61.0537 14.2563C61.5954 13.0511 62.4525 12.0179 63.5326 11.268C64.6166 10.5379 65.8958 10.16 67.1986 10.1852C68.0611 10.1837 68.9162 10.3468 69.7187 10.666C70.5398 10.9946 71.2829 11.4948 71.8992 12.1337C72.5764 12.8435 73.0985 13.6889 73.4318 14.6152C73.8311 15.7483 74.0226 16.9455 73.9968 18.1479V19.0773H63.2262V17.4194H72.0935C72.1083 16.4456 71.8952 15.4821 71.4714 14.6072C71.083 13.803 70.4874 13.1191 69.7472 12.6272C68.9887 12.1348 68.1022 11.8812 67.2006 11.8987C66.2411 11.8807 65.3005 12.1689 64.5128 12.7223C63.7332 13.2783 63.1083 14.0275 62.6984 14.8978C62.2582 15.8199 62.0314 16.831 62.0352 17.8546V18.8476C62.009 20.0078 62.2354 21.1595 62.6984 22.2217C63.1005 23.1349 63.7564 23.9108 64.5864 24.4554C65.4554 24.9973 66.4621 25.2717 67.4831 25.2448C68.1676 25.2588 68.848 25.1368 69.4859 24.8859C70.0301 24.6666 70.5242 24.3376 70.9382 23.919C71.3183 23.5345 71.6217 23.0799 71.8322 22.5799L73.5995 23.1604C73.3388 23.8697 72.9304 24.5143 72.4019 25.0506C71.8132 25.6529 71.1086 26.1269 70.3314 26.4434C69.4258 26.8068 68.4575 26.9846 67.4831 26.9663V26.9663ZM78.8233 10.4075L82.9655 17.325L87.1076 10.4075H89.2683L84.1008 18.5175L89.2683 26.6275H87.103L82.9608 19.9317L78.8193 26.6275H76.6647L81.7711 18.5169L76.6647 10.4062L78.8233 10.4075ZM99.5142 10.4075V12.0447H91.8413V10.4075H99.5142ZM94.2427 6.52397H96.1148V22.3931C96.086 22.9446 96.2051 23.4938 96.4597 23.9827C96.6652 24.344 96.9805 24.629 97.3589 24.7955C97.7328 24.9548 98.1349 25.0357 98.5407 25.0332C98.7508 25.0359 98.9607 25.02 99.168 24.9857C99.3422 24.954 99.4956 24.9205 99.6283 24.8853L100.026 26.5853C99.8062 26.6672 99.5805 26.7327 99.3511 26.7815C99.0274 26.847 98.6977 26.8771 98.3676 26.8712C97.6854 26.871 97.0119 26.7156 96.3973 26.4166C95.7683 26.1156 95.2317 25.6485 94.8442 25.0647C94.4214 24.4018 94.2097 23.6242 94.2374 22.8363L94.2427 6.52397ZM118.398 5H120.354V19.3204C120.376 20.7052 120.022 22.0697 119.328 23.2649C118.644 24.4235 117.658 25.3698 116.477 26.0001C115.168 26.6879 113.708 27.0311 112.232 26.9978C110.759 27.029 109.302 26.6835 107.996 25.9934C106.815 25.362 105.827 24.4161 105.141 23.2582C104.447 22.0651 104.092 20.7022 104.115 19.319V5H106.08V19.1831C106.061 20.2559 106.324 21.3147 106.843 22.2511C107.349 23.1459 108.094 23.8795 108.992 24.3683C109.993 24.9011 111.111 25.1664 112.242 25.139C113.373 25.1656 114.493 24.9003 115.495 24.3683C116.395 23.8815 117.14 23.1475 117.644 22.2511C118.16 21.3136 118.421 20.2553 118.402 19.1831L118.398 5ZM128 5V26.6275H126.041V5H128Z"
      />
      <path
        className="fill-black dark:fill-white"
        d="M23.5294 0H8.47059C3.79241 0 0 3.79241 0 8.47059V23.5294C0 28.2076 3.79241 32 8.47059 32H23.5294C28.2076 32 32 28.2076 32 23.5294V8.47059C32 3.79241 28.2076 0 23.5294 0Z"
      />
      <path
        className="fill-white dark:fill-black"
        d="M17.5667 9.21729H18.8111V18.2403C18.8255 19.1128 18.6 19.9726 18.159 20.7256C17.7241 21.4555 17.0968 22.0518 16.3458 22.4491C15.5717 22.8683 14.6722 23.0779 13.6473 23.0779C12.627 23.0779 11.7286 22.8672 10.9521 22.4457C10.2007 22.0478 9.5727 21.4518 9.13602 20.7223C8.6948 19.9705 8.4692 19.1118 8.48396 18.2403V9.21729H9.72854V18.1538C9.71656 18.8298 9.88417 19.4968 10.2143 20.0868C10.5362 20.6506 11.0099 21.1129 11.5814 21.421C12.1689 21.7448 12.8576 21.9067 13.6475 21.9067C14.4374 21.9067 15.1272 21.7448 15.7169 21.421C16.2895 21.1142 16.7635 20.6516 17.0844 20.0868C17.4124 19.4961 17.5788 18.8293 17.5667 18.1538V9.21729ZM23.6753 9.21729V22.845H22.4309V9.21729H23.6753Z"
      />
    </svg>
  );
};
'''

navbar_content = '''"use client";
import {
  Navbar as NextUINavbar,
  NavbarContent,
  NavbarMenu,
  NavbarMenuToggle,
  NavbarBrand,
  NavbarItem,
  NavbarMenuItem,
} from "@nextui-org/navbar";
import { Button } from "@nextui-org/button";

import { Link } from "@nextui-org/link";
import { link as linkStyles } from "@nextui-org/theme";
import NextLink from "next/link";
import clsx from "clsx";
import { ThemeSwitch } from "@/components/theme-switch";
import { Logo } from "@/components/icons";
import { initFirebase } from "@/firebase";
import { getAuth } from "firebase/auth";
import { useAuthState } from "react-firebase-hooks/auth";
import { useRouter } from "next/navigation";

export const Navbar = () => {
  const app = initFirebase();
  const auth = getAuth(app);
  const [user, loading] = useAuthState(auth);
  const router = useRouter();

  const handleAuthAction = async () => {
    if (user) {
      // If user is logged in, sign them out
      await auth.signOut();
      router.push('/'); // Redirect to home after logout
    } else {
      // If no user, redirect to login page
      router.push('/pages/login');
    }
  };

  return (
    <NextUINavbar maxWidth="xl" position="sticky">
      <NavbarContent className="basis-1/5 sm:basis-full" justify="start">
        <NavbarBrand as="li" className="gap-3 max-w-fit">
          <NextLink className="flex justify-start items-center gap-1" href="/">
            <Logo />
            <p className="font-bold text-inherit">LOGO</p>
          </NextLink>
        </NavbarBrand>
        <ul className="hidden lg:flex gap-4 justify-start ml-2">
          {[
            { label: "Home", href: "/" },
            { label: "Pricing", href: "/pages/products" },
            { label: "Account", href: "/pages/account" },
          ].map((item) => (
            <NavbarItem key={item.href}>
              <NextLink
                className={clsx(
                  linkStyles({ color: "foreground" }),
                  "data-[active=true]:text-primary data-[active=true]:font-medium"
                )}
                color="foreground"
                href={item.href}
              >
                {item.label}
              </NextLink>
            </NavbarItem>
          ))}
        </ul>
      </NavbarContent>

      <NavbarContent
        className="hidden sm:flex basis-1/5 sm:basis-full"
        justify="end"
      >
        <NavbarItem>
          <Button 
            color="primary" 
            variant="solid" 
            className="primary-btn"
            onClick={handleAuthAction}
          >
            {user ? "Logout" : "Login"}
          </Button>
        </NavbarItem>
        <NavbarItem className="hidden sm:flex gap-2">
          <ThemeSwitch />
        </NavbarItem>
      </NavbarContent>

      <NavbarContent className="sm:hidden basis-1 pl-4" justify="end">
        <ThemeSwitch />
        <NavbarMenuToggle />
      </NavbarContent>

      <NavbarMenu>
        <div className="mx-4 mt-2 flex flex-col gap-2">
          {[
            { label: "Home", href: "/" },
            { label: "Pricing", href: "/pages/products" },
            { label: "Account", href: "/pages/account" },
            { 
              label: user ? "Logout" : "Login", 
              href: "#",
              onClick: handleAuthAction 
            },
          ].map((item, index) => (
            <NavbarMenuItem key={`${item.label}-${index}`}>
              {item.onClick ? (
                <Link 
                  color={"foreground"} 
                  href={item.href} 
                  size="lg"
                  onClick={item.onClick}
                >
                  {item.label}
                </Link>
              ) : (
                <Link color={"foreground"} href={item.href} size="lg">
                  {item.label}
                </Link>
              )}
            </NavbarMenuItem>
          ))}
        </div>
      </NavbarMenu>
    </NextUINavbar>
  );
};
'''

primitives_content = '''import { tv } from "tailwind-variants";

export const title = tv({
  base: "tracking-tight inline font-semibold",
  variants: {
    color: {
      violet: "from-[#FF1CF7] to-[#b249f8]",
      yellow: "from-[#FF705B] to-[#FFB457]",
      blue: "from-[#5EA2EF] to-[#0072F5]",
      cyan: "from-[#00b7fa] to-[#01cfea]",
      green: "from-[#6FEE8D] to-[#17c964]",
      pink: "from-[#FF72E1] to-[#F54C7A]",
      foreground: "dark:from-[#FFFFFF] dark:to-[#4B4B4B]",
    },
    size: {
      sm: "text-3xl lg:text-4xl",
      md: "text-[2.3rem] lg:text-5xl leading-9",
      lg: "text-4xl lg:text-6xl",
    },
    fullWidth: {
      true: "w-full block",
    },
  },
  defaultVariants: {
    size: "md",
  },
  compoundVariants: [
    {
      color: [
        "violet",
        "yellow",
        "blue",
        "cyan",
        "green",
        "pink",
        "foreground",
      ],
      class: "bg-clip-text text-transparent bg-gradient-to-b",
    },
  ],
});

export const subtitle = tv({
  base: "w-full md:w-1/2 my-2 text-lg lg:text-xl text-default-600 block max-w-full",
  variants: {
    fullWidth: {
      true: "!w-full",
    },
  },
  defaultVariants: {
    fullWidth: true,
  },
});
'''

theme_switch_content = '''"use client";

import { FC } from "react";
import { VisuallyHidden } from "@react-aria/visually-hidden";
import { SwitchProps, useSwitch } from "@nextui-org/switch";
import { useTheme } from "next-themes";
import { useIsSSR } from "@react-aria/ssr";
import clsx from "clsx";

import { SunFilledIcon, MoonFilledIcon } from "@/components/icons";

export interface ThemeSwitchProps {
  className?: string;
  classNames?: SwitchProps["classNames"];
}

export const ThemeSwitch: FC<ThemeSwitchProps> = ({
  className,
  classNames,
}) => {
  const { theme, setTheme } = useTheme();
  const isSSR = useIsSSR();

  const onChange = () => {
    theme === "light" ? setTheme("dark") : setTheme("light");
  };

  const {
    Component,
    slots,
    isSelected,
    getBaseProps,
    getInputProps,
    getWrapperProps,
  } = useSwitch({
    isSelected: theme === "light" || isSSR,
    "aria-label": `Switch to ${theme === "light" || isSSR ? "dark" : "light"} mode`,
    onChange,
  });

  return (
    <Component
      {...getBaseProps({
        className: clsx(
          "px-px transition-opacity hover:opacity-80 cursor-pointer",
          className,
          classNames?.base,
        ),
      })}
    >
      <VisuallyHidden>
        <input {...getInputProps()} />
      </VisuallyHidden>
      <div
        {...getWrapperProps()}
        className={slots.wrapper({
          class: clsx(
            [
              "w-auto h-auto",
              "bg-transparent",
              "rounded-lg",
              "flex items-center justify-center",
              "group-data-[selected=true]:bg-transparent",
              "!text-default-500",
              "pt-px",
              "px-0",
              "mx-0",
            ],
            classNames?.wrapper,
          ),
        })}
      >
        {!isSelected || isSSR ? (
          <SunFilledIcon size={22} />
        ) : (
          <MoonFilledIcon size={22} />
        )}
      </div>
    </Component>
  );
};
'''

# Add UI components content
avatar_content = '''"use client"

import * as React from "react"
import * as AvatarPrimitive from "@radix-ui/react-avatar"

import { cn } from "@/lib/utils"

const Avatar = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Root>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Root
    ref={ref}
    className={cn(
      "relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full",
      className
    )}
    {...props}
  />
))
Avatar.displayName = AvatarPrimitive.Root.displayName

const AvatarImage = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Image>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Image>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Image
    ref={ref}
    className={cn("aspect-square h-full w-full", className)}
    {...props}
  />
))
AvatarImage.displayName = AvatarPrimitive.Image.displayName

const AvatarFallback = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Fallback>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Fallback>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Fallback
    ref={ref}
    className={cn(
      "flex h-full w-full items-center justify-center rounded-full bg-muted",
      className
    )}
    {...props}
  />
))
AvatarFallback.displayName = AvatarPrimitive.Fallback.displayName

export { Avatar, AvatarImage, AvatarFallback }
'''

card_content = '''import * as React from "react"

import { cn } from "@/lib/utils"

const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-xl border bg-card text-card-foreground shadow",
      className
    )}
    {...props}
  />
))
Card.displayName = "Card"

const CardHeader = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 p-6", className)}
    {...props}
  />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("font-semibold leading-none tracking-tight", className)}
    {...props}
  />
))
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex items-center p-6 pt-0", className)}
    {...props}
  />
))
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }
'''

# Add app content constants
auth_router_content = '''
"use client";
import { useEffect } from "react";
import { usePathname, useRouter } from "next/navigation";
import { initFirebase } from "@/firebase";
import { User, getAuth } from "firebase/auth";
import { useAuthState } from "react-firebase-hooks/auth";

const LOGIN_ROUTE = "/pages/login";

// --------- routes that only authed users can see
const ACCOUNT_ROUTE = "/pages/account";

const AuthRouter = (props: any) => {
  const app = initFirebase();
  const auth = getAuth(app);
  const [user, loading] = useAuthState(auth);
  const router = useRouter();
  const pathName = usePathname();

  // Pages that require the user to be authenticated
  const protectedRoutes = ["/pages/account", "/pages/hidden"];

  const redirect = (
    isLoading: boolean,
    firebaseUser: User | null | undefined,
  ) => {
    if (!isLoading) {
      if (firebaseUser) {
        // User is logged in
        if (pathName === LOGIN_ROUTE) {
          router.push(ACCOUNT_ROUTE); // Redirect from login to account if logged in
        }
      } else {
        // User is not logged in
        if (protectedRoutes.includes(pathName)) {
          router.push(LOGIN_ROUTE); // Redirect to login if trying to access a protected route
        }
      }
    }
  };

  useEffect(() => {
    redirect(loading, user);
  }, [loading, user, pathName]);

  if (loading) {
    return null; // Show a loader or return null while checking auth state
  } else {
    return <>{props.children}</>; // Render children when not loading
  }
};

export default AuthRouter;
'''

error_content = '''"use client";

import { useEffect } from "react";

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}'''

layout_content = '''import "@/styles/globals.scss";
import { Metadata, Viewport } from "next";
import clsx from "clsx";
import Footer from "@/components/footer";
import { Providers } from "./providers";
import AuthRouter from "./authRouter";
import { siteConfig } from "@/config/site";
import { fontSans } from "@/config/fonts";
import { Navbar } from "@/components/navbar";

export const metadata: Metadata = {
  title: {
    default: siteConfig.name,
    template: `%s - ${siteConfig.name}`,
  },
  description: siteConfig.description,
  icons: {
    icon: "/favicon.ico",
  },
};

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "white" },
    { media: "(prefers-color-scheme: dark)", color: "black" },
  ],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html suppressHydrationWarning lang="en">
      <head />
      <body
        className={clsx(
          "min-h-screen bg-background font-sans antialiased",
          fontSans.variable
        )}
      >
        <Providers>
          <AuthRouter>
            <div className="relative flex flex-col h-screen">
              <Navbar />
              <main className="container mx-auto max-w-7xl pt-16 px-6 flex-grow">
                {children}
              </main>
              <Footer />
            </div>
          </AuthRouter>
        </Providers>
      </body>
    </html>
  );
}'''

not_found_content = '''import React from 'react';
import Link from 'next/link';

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center ">
      <h1 className="text-4xl font-bold mb-4">404 - Page Not Found</h1>
      <p className="text-lg mb-8">Sorry, the page you are looking for does not exist.</p>
      <Link href="/">
        <button className='primary-btn'>Go Back Home</button>
      </Link>
    </div>
  );
}'''

page_content = '''import { title } from "@/components/primitives";

export default function Home() {
  return (
    <section className="flex flex-col items-center justify-center gap-4 py-8 md:py-10">
      <div className="inline-block max-w-xl text-center justify-center">
        <span className={title()}>Make&nbsp;</span>
        <span className={title({ color: "violet" })}>beautiful&nbsp;</span>
        <br />
        <span className={title()}>websites.</span>
      </div>
    </section>
  );
}'''

providers_content = '''"use client";

import type { ThemeProviderProps } from "next-themes";
import * as React from "react";
import { NextUIProvider } from "@nextui-org/system";
import { useRouter } from "next/navigation";
import { ThemeProvider as NextThemesProvider } from "next-themes";

export interface ProvidersProps {
  children: React.ReactNode;
  themeProps?: ThemeProviderProps;
}

export function Providers({ children, themeProps }: ProvidersProps) {
  const router = useRouter();

  return (
    <NextUIProvider navigate={router.push}>
      <NextThemesProvider {...themeProps}>{children}</NextThemesProvider>
    </NextUIProvider>
  );
}'''

# Add API content constants
upload_route_content = '''import { Storage } from '@google-cloud/storage';
import { NextResponse } from 'next/server';
import { headers } from 'next/headers';
import path from 'path';

export async function POST(request: Request) {
  const headersList = await headers();
  const origin = headersList.get('origin') || '';
  
  const corsHeaders = {
    'Access-Control-Allow-Origin': origin,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Allow-Credentials': 'true',
    'Referrer-Policy': 'origin'
  };

  try {
    // Initialize storage with ADC
    const storage = new Storage({
      projectId: 'realitygenai',
      // Let ADC handle authentication
      keyFilename: path.join(process.cwd(), 'credentials', 'realitygenai-91609dea9a4a.json')
    });

    const formData = await request.formData();
    const file = formData.get('file') as File;
    const gid = formData.get('gid') as string;

    if (!file || !gid) {
      return NextResponse.json(
        { error: 'File and GID are required' },
        { status: 400, headers: corsHeaders }
      );
    }

    // Get bucket reference
    const bucket = storage.bucket('realitygenai-avatar');
    const fileName = `${gid}-${Date.now()}-${file.name}`;
    const blob = bucket.file(fileName);

    // Convert file to buffer
    const buffer = Buffer.from(await file.arrayBuffer());

    // Create write stream
    const blobStream = blob.createWriteStream({
      resumable: false,
      contentType: file.type
    });

    // Handle upload using promises
    await new Promise((resolve, reject) => {
      blobStream.on('error', (error) => reject(error));
      blobStream.on('finish', () => resolve(true));
      blobStream.end(buffer);
    });

    // Make the file public
    await blob.makePublic();

    // Get the public URL
    const publicUrl = `https://storage.googleapis.com/realitygenai-avatar/${fileName}`;
    
    return NextResponse.json({ url: publicUrl }, { headers: corsHeaders });

  } catch (error: any) {
    console.error('Upload error:', error);
    console.error('Error details:', {
      message: error.message,
      stack: error.stack,
      code: error.code
    });
    
    return NextResponse.json(
      { error: error.message || 'Upload failed' },
      { status: 500, headers: corsHeaders }
    );
  }
}

export const config = {
  api: {
    bodyParser: false,
  },
};'''

# Add login page content constants
login_page_content = '''"use client";
import React, { useState } from "react";
import { Button } from "@nextui-org/button";
import { Form } from "@nextui-org/form";
import { Input } from "@nextui-org/input";
import { GoogleLoginButton } from "react-social-login-buttons";
import { useRouter } from "next/navigation";
import { initFirebase } from "@/firebase";
import {
  getAuth,
  signInWithEmailAndPassword,
  GoogleAuthProvider,
  signInWithPopup,
} from "firebase/auth";
import "../../../styles/Login.scss";
import Link from "next/link";
import { Card } from "@/components/ui/card";

const Login = () => {
  const app = initFirebase();
  const auth = getAuth(app);
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await signInWithEmailAndPassword(auth, email, password);
      router.push("/pages/account");
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleSignIn = async () => {
    setError("");
    setLoading(true);
    try {
      const provider = new GoogleAuthProvider();
      const result = await signInWithPopup(auth, provider);
      if (result.user) {
        router.push("/pages/account");
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="Login page">
      <div className="container">
        <h1 className="content-header">Log In</h1>
        <Card className="content-container">
          {error && <div className="text-danger mb-4">{error}</div>}
          <Form onSubmit={handleSubmit}>
            <Input
              label="Email"
              type="email"
              placeholder="Enter your email"
              autoComplete="username"
              className="mb-4"
              isRequired
              onChange={(e) => setEmail(e.target.value)}
              isInvalid={!!error}
            />
            <Input
              label="Password"
              type="password"
              placeholder="Enter your password"
              autoComplete="current-password"
              className="mb-4"
              isRequired
              onChange={(e) => setPassword(e.target.value)}
              isInvalid={!!error}
            />
            <Button
              className="primary-btn"
              color="primary"
              variant="solid"
              type="submit"
              disabled={loading}
            >
              Log In
            </Button>
            <GoogleLoginButton
              className="social-sign-in-btn"
              onClick={handleGoogleSignIn}
            />
            <p>
              Don't have an account?{" "}
              <Link className="u-link" href="/pages/register">
                Sign Up
              </Link>
            </p>
          </Form>
        </Card>
      </div>
    </div>
  );
};

export default Login;'''

# Add products page content constants
products_page_content = '''"use client";

import React from "react";
import { useRouter } from "next/navigation";
import { getAuth } from "firebase/auth";
import { initFirebase } from "@/firebase";
import { getCheckoutUrl } from "../account/stripePayment";
import "../../../styles/Product.scss";
import { Card, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@nextui-org/button";

const Product = () => {
  const app = initFirebase();
  const auth = getAuth(app);
  const router = useRouter();

  const subscribe = async (priceId) => {
    if (!auth.currentUser) {
      router.push("/login"); // Redirect to login if not logged in
      return;
    }

    try {
      const checkoutUrl = await getCheckoutUrl(app, priceId);
      router.push(checkoutUrl);
    } catch (error) {
      console.error("Failed to subscribe:", error.message);
    }
  };

  return (
    <div className="page Product">
      <h1>Subscribe to benefit!</h1>
      <div className="container">
        <Card className="sub-card">
          <CardHeader>
            <CardTitle className="title">Basic</CardTitle>
            <CardTitle>$6 / Month</CardTitle>
            <div className="features">
              <ul>
                <li>✓ Access to basic features</li>
                <li>✓ 5 projects per month</li>
                <li>✓ Basic support</li>
                <li>✓ 1GB storage</li>
              </ul>
            </div>
            <Button
              color="primary"
              variant="ghost"
              className="primary-btn"
              onClick={() => subscribe("price_1PyaUqEWTDUOm33EpvHFA80P")}
            >
              Subscribe
            </Button>
          </CardHeader>
        </Card>

        <Card className="sub-card">
          <CardHeader>
            <CardTitle className="title">Premium</CardTitle>
            <CardTitle>$12 / Month</CardTitle>
            <div className="features">
              <ul>
                <li>✓ All Basic features</li>
                <li>✓ 15 projects per month</li>
                <li>✓ Priority support</li>
                <li>✓ 10GB storage</li>
                <li>✓ Advanced analytics</li>
              </ul>
            </div>
            <Button
              color="primary"
              variant="ghost"
              className="primary-btn"
              onClick={() => subscribe("price_1PyaVCEWTDUOm33EFYT1O64B")}
            >
              Subscribe
            </Button>
          </CardHeader>
        </Card>

        <Card className="sub-card">
          <CardHeader>
            <CardTitle className="title">Ultimate</CardTitle>
            <CardTitle>$18 / Month</CardTitle>
            <div className="features">
              <ul>
                <li>✓ All Premium features</li>
                <li>✓ Unlimited projects</li>
                <li>✓ 24/7 priority support</li>
                <li>✓ 50GB storage</li>
                <li>✓ Custom analytics</li>
                <li>✓ API access</li>
              </ul>
            </div>
            <Button
              color="primary"
              className="primary-btn"
              onClick={() => subscribe("price_1PyaVREWTDUOm33Epun180Ji")}
            >
              Subscribe
            </Button>
          </CardHeader>
        </Card>
      </div>
    </div>
  );
};

export default Product;'''

# Add register page content constants
register_page_content = '''"use client";
import React, { useState } from "react";
import { Button } from "@nextui-org/button";
import { Form } from "@nextui-org/form";
import { Input } from "@nextui-org/input";
import { GoogleLoginButton } from "react-social-login-buttons";
import { useRouter } from "next/navigation";
import { initFirebase } from "@/firebase";
import {
  getAuth,
  createUserWithEmailAndPassword,
  GoogleAuthProvider,
  signInWithPopup,
} from "firebase/auth";
import "../../../styles/Register.scss";
import Link from "next/link";
import { Card } from "@/components/ui/card";

const Register = () => {
  const app = initFirebase();
  const auth = getAuth(app);
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setError("Passwords do not match");
      return;
    }
    setError("");
    setLoading(true);
    try {
      await createUserWithEmailAndPassword(auth, email, password);
      router.push("/pages/account");  
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleSignIn = async () => {
    setError("");
    setLoading(true);
    try {
      const provider = new GoogleAuthProvider();
      const result = await signInWithPopup(auth, provider);
      if (result.user) {
        router.push("/pages/account");  
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="Register page">
      <div className="container">
        <h1 className="content-header">Register</h1>
        <Card className="content-container">
          {error && <div className="text-danger mb-4">{error}</div>}
          <Form onSubmit={handleSubmit}>
            <Input
              label="Email"
              type="email"
              placeholder="Enter your email"
              autoComplete="username"
              className="mb-4"
              isRequired
              onChange={(e) => setEmail(e.target.value)}
              isInvalid={!!error}
            />
            <Input
              label="Password"
              type="password"
              placeholder="Enter your password"
              autoComplete="new-password"
              className="mb-4"
              isRequired
              onChange={(e) => setPassword(e.target.value)}
              isInvalid={!!error}
            />
            <Input
              label="Confirm Password"
              type="password"
              placeholder="Confirm your password"
              autoComplete="new-password"
              className="mb-4"
              isRequired
              onChange={(e) => setConfirmPassword(e.target.value)}
              isInvalid={!!error}
            />
            <Button className="primary-btn" color="primary" variant="solid" type="submit" disabled={loading}>
              {loading ? "Registering..." : "Register"}
            </Button>
            <p>or</p>
            <GoogleLoginButton
              className="social-sign-in-btn"
              onClick={handleGoogleSignIn}
            />
            <p>
              Already have an account?{" "}
              <Link className="u-link" href="/pages/login">
                Log In
              </Link>
            </p>
          </Form>
        </Card>
      </div>
    </div>
  );
};

export default Register;'''

# Add getPremiumStatus content
get_premium_status_content = '''import { FirebaseApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import {
  collection,
  getFirestore,
  onSnapshot,
  query,
  where,
} from "firebase/firestore";

export const getSubscriptionStatus = async (app: FirebaseApp) => {
  const auth = getAuth(app);
  const userId = auth.currentUser?.uid;
  if (!userId) throw new Error("User not logged in");

  const db = getFirestore(app);
  const subscriptionsRef = collection(db, "customers", userId, "subscriptions");
  const q = query(
    subscriptionsRef,
    where("status", "in", ["trialing", "active"])
  );

  return new Promise<any[]>((resolve, reject) => {
    const unsubscribe = onSnapshot(
      q,
      (snapshot) => {
        if (snapshot.docs.length === 0) {
          resolve([]);
        } else {
          const subscriptions = snapshot.docs.map((doc) => {
            const subscriptionData = doc.data();
            const planName =
              subscriptionData.items?.[0]?.price?.product?.name ||
              "Unknown Plan";

            return {
              ...subscriptionData,
              planName,
            };
          });

          resolve(subscriptions);
        }
        unsubscribe();
      },
      reject
    );
  });
};'''

# Add stripePayment content
stripe_payment_content = '''"use client";
import { FirebaseApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import {
  collection,
  getFirestore,
  onSnapshot,
  addDoc,
} from "firebase/firestore";
import { getFunctions, httpsCallable } from "firebase/functions";

export const getCheckoutUrl = async (
  app: FirebaseApp,
  priceId: string,
): Promise<string> => {
  const auth = getAuth(app);
  const userId = auth.currentUser?.uid;
  if (!userId) throw new Error("User is not authenticated");

  const db = getFirestore(app);
  const checkoutSessionRef = collection(
    db,
    "customers",
    userId,
    "checkout_sessions",
  );

  const docRef = await addDoc(checkoutSessionRef, {
    price: priceId,
    success_url: window.location.origin,
    cancel_url: window.location.origin,
  });

  return new Promise<string>((resolve, reject) => {
    const unsubscribe = onSnapshot(docRef, (snap) => {
      const { error, url } = snap.data() as {
        error?: { message: string };
        url?: string;
      };
      if (error) {
        unsubscribe();
        reject(new Error(`An error occurred: ${error.message}`));
      }
      if (url) {
        console.log("Stripe Checkout URL:", url);
        unsubscribe();
        resolve(url);
      }
    });
  });
};

export const getPortalUrl = async (app: FirebaseApp): Promise<string> => {
  const auth = getAuth(app);
  const user = auth.currentUser;

  if (!user) throw new Error("User not authenticated");

  const functions = getFunctions(app, "us-central1");
  const functionRef = httpsCallable(
    functions,
    "ext-firestore-stripe-payments-createPortalLink",
  );

  try {
    const { data } = await functionRef({
      customerId: user.uid,
      returnUrl: window.location.origin,
    });

    // Type assertion to specify the expected shape of the data
    const portalData = data as { url: string };
    if (!portalData.url) throw new Error("No URL returned from Stripe");
    console.log("Reroute to Stripe portal: ", portalData.url);
    return portalData.url;
  } catch (error) {
    console.error("Failed to obtain Stripe portal URL:", error);
    throw error;
  }
};'''

# Add account page content
account_page_content = '''"use client";

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
}'''

# Add VSCode settings content
vscode_settings_content = '''{
  "typescript.tsdk": "node_modules/typescript/lib"
}'''

# ------------------------------------------- Create files ---------------------------------------------
def create_initial_files():
    # Ensure all root-level app files are created
    app_dir = os.path.join(current_path, "app")
    
    if not os.path.exists(app_dir):
        os.makedirs(app_dir)
        print("✅ app directory successfully created...")
    else:
        print("ℹ️ app directory already exists, skipping...")

    # Create all root-level app files
    create_file_if_not_exists(os.path.join(app_dir, "authRouter.tsx"), auth_router_content)
    create_file_if_not_exists(os.path.join(app_dir, "error.tsx"), error_content)
    create_file_if_not_exists(os.path.join(app_dir, "layout.tsx"), layout_content)
    create_file_if_not_exists(os.path.join(app_dir, "not-found.tsx"), not_found_content)
    create_file_if_not_exists(os.path.join(app_dir, "page.tsx"), page_content)
    create_file_if_not_exists(os.path.join(app_dir, "providers.tsx"), providers_content)

    # Create public directory if it doesn't exist
    public_dir = os.path.join(current_path, "public")
    if not os.path.exists(public_dir):
        os.makedirs(public_dir)
        print("✅ public directory successfully created...")
    else:
        print("ℹ️ public directory already exists, skipping...")

    # Create public files
    create_file_if_not_exists(os.path.join(public_dir, "next.svg"), next_svg_content)
    create_file_if_not_exists(os.path.join(public_dir, "vercel.svg"), vercel_svg_content)

    # Create types directory if it doesn't exist
    types_dir = os.path.join(current_path, "types")
    if not os.path.exists(types_dir):
        os.makedirs(types_dir)
        print("✅ types directory successfully created...")
    else:
        print("ℹ️ types directory already exists, skipping...")

    # Create all files
    create_file_if_not_exists(os.path.join(types_dir, "index.ts"), types_index_content)
    create_file_if_not_exists(os.path.join(current_path, "tsconfig.json"), tsconfig_content)
    create_file_if_not_exists(os.path.join(current_path, "tailwind.config.js"), tailwind_config_content)
    create_file_if_not_exists(os.path.join(current_path, "site-map-generator.js"), sitemap_generator_content)
    create_file_if_not_exists(os.path.join(current_path, "postcss.config.js"), postcss_config_content)
    create_file_if_not_exists(os.path.join(current_path, "package.json"), package_json_content)
    create_file_if_not_exists(os.path.join(current_path, "next.config.js"), next_config_content)
    create_file_if_not_exists(os.path.join(current_path, "next-env.d.ts"), next_env_content)
    create_file_if_not_exists(os.path.join(current_path, "firebase.ts"), firebase_content)
    create_file_if_not_exists(os.path.join(current_path, "Dockerfile"), dockerfile_content)
    create_file_if_not_exists(os.path.join(current_path, "docker-compose.yml"), docker_compose_content)
    create_file_if_not_exists(os.path.join(current_path, "components.json"), components_json_content)
    create_file_if_not_exists(os.path.join(current_path, ".gitignore"), gitignore_content)
    create_file_if_not_exists(os.path.join(current_path, ".eslintrc.json"), eslintrc_content)
    create_file_if_not_exists(os.path.join(current_path, ".eslintignore"), eslintignore_content)
    create_file_if_not_exists(os.path.join(current_path, ".dockerignore"), dockerignore_content)
    create_file_if_not_exists(os.path.join(current_path, ".env"), env_content)

    # Create styles directory if it doesn't exist
    styles_dir = os.path.join(current_path, "styles")
    if not os.path.exists(styles_dir):
        os.makedirs(styles_dir)
        print("✅ styles directory successfully created...")
    else:
        print("ℹ️ styles directory already exists, skipping...")

    # Create style files
    create_file_if_not_exists(os.path.join(styles_dir, "Variables.scss"), styles_variables_content)
    create_file_if_not_exists(os.path.join(styles_dir, "globals.scss"), styles_globals_content)
    create_file_if_not_exists(os.path.join(styles_dir, "Account.scss"), styles_account_content)
    create_file_if_not_exists(os.path.join(styles_dir, "Footer.scss"), styles_footer_content)
    create_file_if_not_exists(os.path.join(styles_dir, "Login.scss"), styles_login_content)
    create_file_if_not_exists(os.path.join(styles_dir, "Product.scss"), styles_product_content)
    create_file_if_not_exists(os.path.join(styles_dir, "Register.scss"), styles_register_content)

    # Create lib directory if it doesn't exist
    lib_dir = os.path.join(current_path, "lib")
    if not os.path.exists(lib_dir):
        os.makedirs(lib_dir)
        print("✅ lib directory successfully created...")
    else:
        print("ℹ️ lib directory already exists, skipping...")

    # Create lib files
    create_file_if_not_exists(os.path.join(lib_dir, "utils.ts"), utils_content)

    # Create credentials directory if it doesn't exist
    credentials_dir = os.path.join(current_path, "credentials")
    if not os.path.exists(credentials_dir):
        os.makedirs(credentials_dir)
        print("✅ credentials directory successfully created...")
    else:
        print("ℹ️ credentials directory already exists, skipping...")

    # Create credentials file
    create_file_if_not_exists(os.path.join(credentials_dir, "realitygenai-91609dea9a4a.json"), credentials_content)

    # Create context directory if it doesn't exist
    context_dir = os.path.join(current_path, "context")
    if not os.path.exists(context_dir):
        os.makedirs(context_dir)
        print("✅ context directory successfully created...")
    else:
        print("ℹ️ context directory already exists, skipping...")

    # Create context files
    create_file_if_not_exists(os.path.join(context_dir, "UserAuthContext.js"), user_auth_context_content)

    # Create config directory if it doesn't exist
    config_dir = os.path.join(current_path, "config")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
        print("✅ config directory successfully created...")
    else:
        print("ℹ️ config directory already exists, skipping...")

    # Create config files
    create_file_if_not_exists(os.path.join(config_dir, "fonts.ts"), fonts_content)
    create_file_if_not_exists(os.path.join(config_dir, "site.ts"), site_content)

    # Create components directory and its subdirectories
    components_dir = os.path.join(current_path, "components")
    ui_dir = os.path.join(components_dir, "ui")
    
    for dir_path in [components_dir, ui_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"✅ {dir_path} directory successfully created...")
        else:
            print(f"ℹ️ {dir_path} directory already exists, skipping...")

    # Create main component files
    create_file_if_not_exists(os.path.join(components_dir, "footer.tsx"), footer_content)
    create_file_if_not_exists(os.path.join(components_dir, "icons.tsx"), icons_content)
    create_file_if_not_exists(os.path.join(components_dir, "navbar.tsx"), navbar_content)
    create_file_if_not_exists(os.path.join(components_dir, "primitives.ts"), primitives_content)
    create_file_if_not_exists(os.path.join(components_dir, "theme-switch.tsx"), theme_switch_content)

    # Create UI component files
    create_file_if_not_exists(os.path.join(ui_dir, "avatar.tsx"), avatar_content)
    create_file_if_not_exists(os.path.join(ui_dir, "card.tsx"), card_content)

    # Create app directory and its subdirectories
    app_dir = os.path.join(current_path, "app")
    api_dir = os.path.join(app_dir, "api")
    upload_dir = os.path.join(api_dir, "upload")
    
    for dir_path in [app_dir, api_dir, upload_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"✅ {dir_path} directory successfully created...")
        else:
            print(f"ℹ️ {dir_path} directory already exists, skipping...")

    # Create main app files
    create_file_if_not_exists(os.path.join(app_dir, "authRouter.tsx"), auth_router_content)
    create_file_if_not_exists(os.path.join(app_dir, "error.tsx"), error_content)
    create_file_if_not_exists(os.path.join(app_dir, "layout.tsx"), layout_content)
    create_file_if_not_exists(os.path.join(app_dir, "not-found.tsx"), not_found_content)
    create_file_if_not_exists(os.path.join(app_dir, "page.tsx"), page_content)
    create_file_if_not_exists(os.path.join(app_dir, "providers.tsx"), providers_content)

    # Create API files
    create_file_if_not_exists(os.path.join(upload_dir, "route.ts"), upload_route_content)

    # Create pages directory and its subdirectories
    app_dir = os.path.join(current_path, "app")
    pages_dir = os.path.join(app_dir, "pages")
    login_dir = os.path.join(pages_dir, "login")
    
    for dir_path in [pages_dir, login_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"✅ {dir_path} directory successfully created...")
        else:
            print(f"ℹ️ {dir_path} directory already exists, skipping...")

    # Create login page file
    create_file_if_not_exists(os.path.join(login_dir, "page.js"), login_page_content)

    # Create products directory within pages
    app_dir = os.path.join(current_path, "app")
    pages_dir = os.path.join(app_dir, "pages")
    products_dir = os.path.join(pages_dir, "products")
    
    if not os.path.exists(products_dir):
        os.makedirs(products_dir)
        print("✅ products directory successfully created...")
    else:
        print("ℹ️ products directory already exists, skipping...")

    # Create products page file
    create_file_if_not_exists(os.path.join(products_dir, "page.js"), products_page_content)

    # Create register directory within pages
    app_dir = os.path.join(current_path, "app")
    pages_dir = os.path.join(app_dir, "pages")
    register_dir = os.path.join(pages_dir, "register")
    
    if not os.path.exists(register_dir):
        os.makedirs(register_dir)
        print("✅ register directory successfully created...")
    else:
        print("ℹ️ register directory already exists, skipping...")

    # Create register page file
    create_file_if_not_exists(os.path.join(register_dir, "page.js"), register_page_content)

    # Create account directory within pages
    app_dir = os.path.join(current_path, "app")
    pages_dir = os.path.join(app_dir, "pages")
    account_dir = os.path.join(pages_dir, "account")
    
    if not os.path.exists(account_dir):
        os.makedirs(account_dir)
        print("✅ account directory successfully created...")
    else:
        print("ℹ️ account directory already exists, skipping...")

    # Create getPremiumStatus file
    create_file_if_not_exists(os.path.join(account_dir, "getPremiumStatus.ts"), get_premium_status_content)

    # Create stripePayment file in account directory
    app_dir = os.path.join(current_path, "app")
    pages_dir = os.path.join(app_dir, "pages")
    account_dir = os.path.join(pages_dir, "account")
    
    create_file_if_not_exists(os.path.join(account_dir, "stripePayment.tsx"), stripe_payment_content)

    # Create page.tsx in account directory
    app_dir = os.path.join(current_path, "app")
    pages_dir = os.path.join(app_dir, "pages")
    account_dir = os.path.join(pages_dir, "account")
    
    create_file_if_not_exists(os.path.join(account_dir, "page.tsx"), account_page_content)

    # Create .vscode directory
    vscode_dir = os.path.join(current_path, ".vscode")
    
    if not os.path.exists(vscode_dir):
        os.makedirs(vscode_dir)
        print("✅ .vscode directory successfully created...")
    else:
        print("ℹ️ .vscode directory already exists, skipping...")

    # Create settings.json
    create_file_if_not_exists(os.path.join(vscode_dir, "settings.json"), vscode_settings_content)

# ------------------------------------------- Main execution ---------------------------------------------
if __name__ == "__main__":
    print("🚀 Starting Next.js client generator...")
    create_initial_files()
    print("✨ Initial file creation complete!")
