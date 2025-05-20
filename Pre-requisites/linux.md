---

# Setting up a Development Environment on Ubuntu/Fedora

This guide helps you set up a modern development environment on Ubuntu or Fedora, including Git, Node.js, and `uv` for Python.

---

## Prerequisites

* A system running Ubuntu 20.04+ or Fedora 36+
* Sudo (administrator) access to the terminal
* Internet connection

---

## Step 1: Update Your System

### On Ubuntu:

```bash
sudo apt update && sudo apt upgrade -y
```

### On Fedora:

```bash
sudo dnf upgrade --refresh -y
```

---

## Step 2: Install Essential Tools

### On Ubuntu:

```bash
sudo apt install -y wget curl git ca-certificates
```

### On Fedora:

```bash
sudo dnf install -y wget curl git ca-certificates
```

---

## Step 3: Install Node Version Manager (nvm)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

> 💡 **Note**: You may need to restart your terminal or source your profile:

```bash
source ~/.bashrc    # or ~/.zshrc if you're using zsh
```

---

## Step 4: Install Node.js 22

```bash
nvm install 22
```

Verify installation:

```bash
node -v       # Should display "v22.15.0"
nvm current   # Should display "v22.15.0"
```

---

## Step 5: Install the `uv` Package Manager for Python

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Final Step: Restart Terminal

Close and reopen your terminal to finalize all environment settings.

---

## Troubleshooting

If you encounter problems:

* Ensure `nvm` is properly sourced (`source ~/.bashrc` or equivalent)
* Re-run installation commands if they failed midway
* Use `--help` flags for more info (e.g., `nvm --help`)

---

## Next Steps

You now have a ready-to-use development environment with:

* Git for version control
* Node.js 22 for JS/TS development
* `uv` for Python package management

Happy coding! 🚀

---

Let me know if you want a version specific to **only Ubuntu** or **only Fedora**, or if you want to include tools like Python, Docker, or VS Code.

