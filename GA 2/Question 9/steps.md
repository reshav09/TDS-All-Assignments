---

# 🚀 Setting Up a GitHub Codespace

This guide shows you how to create a GitHub Codespace, add an MIT license, and run a command to display environment variables.

---

## 📝 Step 1: Create a New Repository

1. Sign in to [GitHub](https://github.com/)
2. Click the "+" in the top-right, then select **New repository**
3. Fill in details:

   * Name: e.g., "eshopco-onboarding"
   * Visibility: Public
   * Check **Add a README file**
4. Click **Create repository**

---

## 🖥 Step 2: Launch a Codespace

1. In the repository, click the **Code** button
2. Select the **Codespaces** tab, then click **Create codespace on main**
3. Wait for initialization

---

## 📄 Step 3: Add an MIT License

1. In Codespace, click the **Explorer** icon (Ctrl+Shift+E)
2. Create a new file named **LICENSE** and paste the MIT License text into it
3. Save the file (Ctrl+S)

---

## 💾 Step 4: Commit and Push the License

1. Click the **Source Control** icon (Ctrl+Shift+G)
2. Stage the LICENSE file, then commit with message: *Add MIT License*
3. Push the changes

---

## 💻 Step 5: Run the Required Command

1. Open the terminal (Ctrl + \`)
2. Run:

   ```
   echo $GITHUB_REPOSITORY $GITHUB_TOKEN
   ```
3. Copy the output

---

## 📋 Step 6: Submit the Output

Paste the output from the terminal as your answer.

---

## ⚠️ Keep Your Codespace Active

* **Do not close** your Codespace until after submitting. Closing it will lose access to the environment variables.

---

## 🚧 Troubleshooting

* If Codespace fails to launch, refresh and try again.
* Ensure you're in the correct terminal session if variables don't show.
* Reopen Codespace from the **Codespaces** menu if accidentally closed.

---

