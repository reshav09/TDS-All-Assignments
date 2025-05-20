---

# 🚀 Creating and Pushing a Docker Image to Docker Hub

This guide walks you through setting up Docker, creating a Python app, building an image, and pushing it to Docker Hub.

---

## 🖥 Step 1: Install Docker on Ubuntu/Fedora/Arch

1. **Update your package list**:

   For **Ubuntu** or **Debian**-based systems:

   ```
   sudo apt-get update
   ```

   For **Fedora**:

   ```
   sudo dnf update
   ```

   For **Arch Linux**:

   ```
   sudo pacman -Syu
   ```

2. **Install Docker**:

   * For **Ubuntu/Debian**:

     ```
     sudo apt-get install docker.io
     ```

   * For **Fedora**:

     ```
     sudo dnf install docker
     ```

   * For **Arch Linux**:

     ```
     sudo pacman -S docker
     ```

3. **Start Docker**:

   Enable and start the Docker service:

   ```
   sudo systemctl enable --now docker
   ```

4. **Verify Installation**:

   * Check if Docker is running:

     ```
     sudo systemctl status docker
     ```
   * Verify Docker version:

     ```
     docker --version
     ```

---

## ✅ Step 2: Verify Docker Installation

1. Open a terminal and run:

   ```
   docker --version
   ```

2. Run a simple container to test:

   ```
   docker run hello-world
   ```

   If successful, you'll see a confirmation message.

---

## 📝 Step 3: Set Up a Docker Hub Account

1. Go to [Docker Hub](https://hub.docker.com/), sign up, and verify your email.

---

## 🔑 Step 4: Log in to Docker Hub

1. Open a terminal and log in:

   ```
   docker login
   ```

2. Enter your Docker Hub credentials.

---

## 📁 Step 5: Create a Project Directory

1. Create and navigate to a new directory for your Docker project:

   ```
   mkdir docker-hello-world
   cd docker-hello-world
   ```

---

## 🐍 Step 6: Write a Simple Python Application

1. Create a file named `app.py` containing:

   ```python
   print("Hello from my Docker container!")
   ```

   Or use this command:

   ```
   echo print("Hello from my Docker container!") > app.py
   ```

---

## 🛠 Step 7: Create a Dockerfile

1. In the same directory, create a file named `Dockerfile` (without an extension):

   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY app.py .

   CMD ["python", "app.py"]
   ```

   This Dockerfile:

   * Uses Python 3.9 as the base image
   * Sets the working directory to `/app`
   * Copies your `app.py` into the container
   * Runs `app.py` when the container starts

---

## 🏗 Step 8: Build the Docker Image

1. Build your Docker image with a custom tag:

   ```
   docker build -t yourusername/hello-python:latest .
   ```

2. Verify the image:

   ```
   docker images
   ```

---

## ⚙️ Step 9: Test the Docker Image Locally

1. Run your Docker container:

   ```
   docker run yourusername/hello-python:latest
   ```

   The output should be: `Hello from my Docker container!`

---

## 🔖 Step 10: Tag the Docker Image

1. Add a custom tag (e.g., based on your roll number):

   ```
   docker tag yourusername/hello-python:latest yourusername/hello-python:rollnumber
   ```

   Replace `rollnumber` with your unique identifier.

---

## ⬆️ Step 11: Push the Image to Docker Hub

1. Push the `latest` tag:

   ```
   docker push yourusername/hello-python:latest
   ```

2. Push the custom tag:

   ```
   docker push yourusername/hello-python:rollnumber
   ```

---

## 🌐 Step 12: Verify Your Image on Docker Hub

1. Visit [Docker Hub](https://hub.docker.com/), log in, and go to your repository.
2. Check that both the `latest` and `rollnumber` tags appear.

Your image URL will look like this:

```
https://hub.docker.com/repository/docker/yourusername/hello-python/general
```

---

## 🔧 Troubleshooting Tips

* **Docker fails to start**: Ensure **Virtualization** is enabled in your BIOS (for systems using virtualization features).
* **Can't push images**: Run `docker login` to authenticate. Ensure the image name starts with your Docker Hub username.
* **Build failures**: Check for syntax errors in the Dockerfile or missing files like `app.py`.
* **"Permission denied" errors**: On Linux, prepend `sudo` to Docker commands if you're not in the Docker group, or add your user to the Docker group:

  ```
  sudo usermod -aG docker $USER
  ```

---
