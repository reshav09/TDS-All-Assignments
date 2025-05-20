---

# 🛠 Setting Up a GitHub Action with Your Email in the Step Name

This guide walks you through creating a GitHub Action where your **email appears as a step name**.

---

## ✅ Steps

### 1. Create or Use a Repository

* Sign in at [github.com](https://github.com)
* Create a new repo or open an existing one

### 2. Create the Workflow File

* Go to the **Actions** tab → click **"New workflow"**
* Choose **"set up a workflow yourself"**
* Replace the content with:

```yaml
name: Email Step Example

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  sample-job:
    runs-on: ubuntu-latest
    steps:
      - name: your.email@example.com
        run: echo "Hello from your GitHub Action!"
      - name: Display date
        run: date
```

* Click **"Start commit"** → commit the file

### 3. Run the Workflow

* Go to **Actions** → select the workflow → click **"Run workflow"**
* Or just push a change to the `main` branch

### 4. Verify

* Open the latest workflow run from the **Actions** tab
* Ensure your email appears as the step name and it completes successfully ✅

---

## Notes

* Save the file in `.github/workflows/`
* Your email is only used as a label (not sent/stored)
* The workflow is public if your repo is public

---

## Example Repo URL

```
https://github.com/<your-username>/<your-repository>
```
