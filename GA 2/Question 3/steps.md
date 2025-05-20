---

# Publishing a GitHub Pages Site

This guide walks you through creating and publishing a simple static website using GitHub Pages. It includes a method for displaying an email address without Cloudflare obfuscation.

---

## Step 1: Create a New GitHub Repository

1. Log in to your GitHub account.
2. Click the **+** icon in the top-right corner, then choose **New repository**.
3. Give your repository a name (e.g., `my-project-site`).
4. Optionally, add a description.
5. Set the visibility to **Public**.
6. Check the box to **Add a README file**.
7. Click **Create repository**.

---

## Step 2: Enable GitHub Pages

1. Go to your repository’s **Settings**.
2. In the left sidebar, select **Pages**.
3. Under **Source**, choose the `main` branch.
4. Click **Save**.
5. Wait a few minutes while GitHub builds and publishes your site.

---

## Step 3: Add HTML Content

1. In your repository, click **Add file** → **Create new file**.
2. Name the file `index.html`.
3. Paste in the following sample HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Web Project</title>
</head>
<body>
    <h1>Welcome to My Site</h1>
    <!--email_off-->your.email@example.com<!--/email_off-->
    <br>
</body>
</html>
```

4. Replace `your.email@example.com` with your actual email address.
5. Click **Commit changes** to save the file.

---

## Step 4: View Your Published Site

1. After a few minutes, visit your GitHub Pages URL:

   ```
   https://<your-username>.github.io/<your-repository-name>/
   ```

   Example:

   ```
   https://username.github.io/my-project-site/
   ```

2. Confirm the site loads and the email appears as expected.

3. If the page doesn't show the latest version, try appending `?v=1` to the URL to bypass cache:

   ```
   https://username.github.io/my-project-site/?v=1
   ```

---

## How Email Protection Works

GitHub Pages can work alongside Cloudflare, which sometimes obfuscates email addresses by default. To prevent this, wrap your email address in special comment tags like so:

```html
<!--email_off-->your.email@example.com<!--/email_off-->
```

This disables Cloudflare's obfuscation for that specific address, ensuring it displays exactly as written.

---

## Troubleshooting Tips

* Make sure the repository is **public**.
* Ensure GitHub Pages is enabled and set to the correct branch.
* Wait 5–10 minutes for the site to update.
* Try a hard refresh (`Ctrl+Shift+R`) or view the page in an incognito window.
* Check for typos in your file or branch settings.

---

## GitHub Pages URL Format

Once everything is set up, your site will be available at:

```
https://<your-username>.github.io/<your-repository-name>/
```

Replace `<your-username>` and `<your-repository-name>` with your actual GitHub username and repo name.

---


