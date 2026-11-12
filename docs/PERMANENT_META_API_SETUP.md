# 🔑 The Bulletproof Guide to Meta Graph API Setup (Permanent & Never-Expiring)

> **Objective:** Set up a Facebook Page Access Token that **never expires**, works with LazyMeta out of the box, and **will not break** even if you change passwords or log out of devices.

---

## 🧠 Why Most Meta Tokens Break (The 3 Token Traps)

1. **The 1-Hour Trap:** The default token generated in the Graph API Explorer is a temporary testing token. It dies after 60–120 minutes (`OAuthException: Error validating access token: Session has expired`).
2. **The 60-Day Trap:** Standard long-lived user tokens expire after 60 days.
3. **The User Token vs. Page Token Trap:** Posting to a Page requires a **Page Access Token**, NOT a **User Access Token**.
4. **The Password Reset Trap:** If a Page token is tied to a personal Facebook account, any password reset or 2FA checkpoint revokes the token immediately.

Below are the **two foolproof methods** to get a permanent token:
* **Method 1 (Enterprise / Recommended):** Meta Business Portfolio **System User** (100% immune to personal account password changes).
* **Method 2 (Fast / Developer):** Graph API Explorer **Long-Lived Page Token Exchange** (`Expires: Never`).

---

## 🛠️ Prerequisites
1. A **Facebook Account** that is an **Admin** of the target Facebook Page.
2. A **Meta for Developers Account** (register for free at [developers.facebook.com](https://developers.facebook.com)).

---

## 🚀 METHOD 1: System User Permanent Token (100% Bulletproof - Recommended)

A **System User** is an automated bot identity owned by your Business Portfolio. It has no personal profile, no password to reset, and its tokens **never expire**.

### Step 1: Create a Meta App
1. Go to [developers.facebook.com/apps](https://developers.facebook.com/apps) and click **Create App**.
2. **App Type:** Select **"Other"** $\rightarrow$ Click **Next**.
3. **App Purpose:** Select **"Business"** $\rightarrow$ Click **Next**.
4. Give your app a name (e.g. `LazyMeta Scheduler`) and connect it to your Business Account/Portfolio.
5. Click **Create App**.

### Step 2: Create a System User in Business Settings
1. Open **Meta Business Settings**: [business.facebook.com/settings](https://business.facebook.com/settings).
2. In the left sidebar, navigate to **Users** $\rightarrow$ **System Users**.
3. Click **Add** (or **Create System User**).
4. **System Username:** `lazymeta-bot`
5. **System User Role:** Select **Admin** $\rightarrow$ Click **Create System User**.

### Step 3: Assign Page Permissions to the System User
1. Click on your newly created `lazymeta-bot` in the System Users list.
2. Click **Add Assets**.
3. In the modal:
   * Select **Pages** (under Asset Type).
   * Check your target Facebook Page.
   * Toggle on **Full Control (Manage Page)**.
4. Click **Save Changes**.

### Step 4: Generate the Permanent Token
1. In the same System User view, click **Generate New Token**.
2. **Select App:** Choose your `LazyMeta Scheduler` app.
3. **Token Expiration:** Select **Never** (or **Permanent**).
4. **Permissions:** Scroll and check these 3 essential permissions:
   * `pages_show_list`
   * `pages_read_engagement`
   * `pages_manage_posts`
5. Click **Generate Token**.
6. **Copy and save this token immediately** (Meta will never show it to you again!).

---

## ⚡ METHOD 2: Graph API Explorer Token Exchange (Fast Developer Route)

If you don't use Business Manager, this method creates a Page Access Token with `Expires: Never`.

### Step 1: Create your Meta App
1. Go to [developers.facebook.com/apps](https://developers.facebook.com/apps) $\rightarrow$ **Create App**.
2. Select **Other** $\rightarrow$ **Business** $\rightarrow$ Name it `LazyMeta App` $\rightarrow$ **Create App**.
3. Go to **App Settings** $\rightarrow$ **Basic** in the left menu.
4. Note down:
   * **App ID** (e.g. `123456789012345`)
   * **App Secret** (click **Show**, e.g. `a1b2c3d4e5f6g7h8...`)

### Step 2: Generate Short-Lived Token
1. Open the **Graph API Explorer**: [developers.facebook.com/tools/explorer](https://developers.facebook.com/tools/explorer).
2. In the top-right corner:
   * **Meta App:** Select your `LazyMeta App`.
   * **User or Page:** Select **User Token**.
3. Under **Permissions**, click **Add a Permission** and add:
   * `pages_show_list`
   * `pages_read_engagement`
   * `pages_manage_posts`
4. Click **Generate Access Token**.
5. Approve the Facebook popup dialog and check your target Page.
6. Copy the generated token string.

### Step 3: Exchange for Long-Lived User Token (60 Days)
Open a new browser tab or run this URL in your terminal/browser (replace `{app-id}`, `{app-secret}`, and `{short-lived-token}`):

```text
https://graph.facebook.com/v22.0/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={short-lived-token}
```

Meta will return a JSON response like this:
```json
{
  "access_token": "EAABwz...",
  "token_type": "bearer",
  "expires_in": 5184000
}
```
Copy this new `access_token` (this is your 60-day Long-Lived User Token).

### Step 4: The Magic Trick: Generate the NEVER-EXPIRING Page Token
1. Go back to the **Graph API Explorer**: [developers.facebook.com/tools/explorer](https://developers.facebook.com/tools/explorer).
2. Paste the **Long-Lived User Token** (from Step 3) into the **Access Token** bar.
3. In the query box, type:
   ```text
   GET /me/accounts
   ```
4. Click **Submit**.
5. In the JSON output, locate your Page name:
   ```json
   {
     "data": [
       {
         "name": "Your Page Name",
         "id": "102938475610293",
         "access_token": "EAAGNO...",  <--- THIS IS YOUR PERMANENT PAGE TOKEN!
         "tasks": [
           "ANALYZE",
           "ADVERTISE",
           "MODERATE",
           "CREATE_CONTENT",
           "MANAGE"
         ]
       }
     ]
   }
   ```
6. Copy the `access_token` inside your Page object.

---

## 🔍 How to Verify that Your Token "Never Expires"

1. Open Meta's official **Access Token Debugger**: [developers.facebook.com/tools/debug/accesstoken](https://developers.facebook.com/tools/debug/accesstoken).
2. Paste your Page Access Token into the box and click **Debug**.
3. Verify the following fields:
   * **App ID:** Matches your App ID.
   * **Type:** `Page` (MUST be `Page`, NOT `User`).
   * **Expires:** **`Never`** (or `2 months` with auto-renewal).
   * **Scopes:** Must include `pages_manage_posts` and `pages_read_engagement`.

---

## 📍 How to Find Your Numeric Facebook Page ID

Your Facebook Page ID is a numeric string (e.g. `102938475610293`):

* **Method 1 (From the API response above):** In Step 4 of the Graph Explorer, the `"id"` field right next to your Page name is your Page ID.
* **Method 2 (From Facebook UI):**
  1. Go to your Facebook Page on desktop.
  2. Click **About** $\rightarrow$ **Page transparency**.
  3. Look for **Page ID**: `102938475610293`.

---

## ⚙️ Plug into LazyMeta `.env`

In your `lazymeta` project directory, open your `.env` file (or copy from `.env.example`):

```bash
cp .env.example .env
```

Fill in the two fields:
```env
META_PAGE_ID=102938475610293
META_PAGE_ACCESS_TOKEN=EAAGNO...your_permanent_page_token_here...
META_GRAPH_VERSION=v22.0
META_REQUEST_DELAY=2.5
```

---

## 🩺 Final Verification: Run Meta Doctor

Run LazyMeta's pre-flight health check:

```bash
python run.py doctor
```

If configured correctly, you will see:
```text
✓ Git Security: Credentials are not tracked in git.
✓ Configuration: API Version: v22.0, Delay: 2.5s
✓ Meta Connection: Successfully connected as Your Page Name (ID: 102938475610293)
✓ Publishing Permissions: Page posting rights verified.

All systems operational! LazyMeta is ready to schedule.
```

---

## 🛡️ The "Won't Break" Golden Rules

1. **Always use a Page Token, never a User Token:** Only Page tokens have permission to schedule visitor timeline posts.
2. **Do not post faster than 2.0s delay:** Meta aggressively monitors automated uploads. LazyMeta's `2.5s` default delay keeps you safely below Meta's velocity triggers.
3. **App in Live vs. Development Mode:**
   * If your app is in **Development Mode**, the Page Access Token will only work for accounts that are Admins/Developers/Testers of the App.
   * If you are managing your own page, Development Mode is completely fine!
   * If you are managing client pages outside your account, switch the App to **Live Mode** in the Meta App Dashboard header.
4. **Never commit `.env` to git:** LazyMeta has pre-configured `.gitignore` to protect your token from ever leaking to public repositories.
