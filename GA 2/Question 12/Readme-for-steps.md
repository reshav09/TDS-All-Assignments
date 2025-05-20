---

### **Exposing Ollama to the Internet with ngrok on Ubuntu/Fedora/Arch**

This guide will show you how to expose Ollama to the internet with CORS support and ngrok in linux. 

---

### **Step 1: Configure Ollama with CORS Support**

1. **Close Ollama if it's running:**

   * If Ollama is running, terminate it via terminal by pressing `Ctrl + C` or finding the process and killing it.

2. **Set the `OLLAMA_ORIGINS` environment variable:**

   * For CORS support, you need to set the `OLLAMA_ORIGINS` environment variable.

   **Temporary Method (Terminal Session)**:

   ```bash
   export OLLAMA_ORIGINS="*"
   ```

   **Permanent Method (for future sessions):**

   * Open your shell configuration file (e.g., `.bashrc`, `.zshrc`, or `.bash_profile`).

     ```bash
     nano ~/.bashrc  # or ~/.zshrc if you use Zsh
     ```

   * Add the following line at the end of the file:

     ```bash
     export OLLAMA_ORIGINS="*"
     ```

   * After saving and closing the file, reload your shell configuration:

     ```bash
     source ~/.bashrc  # or source ~/.zshrc
     ```

3. **Start Ollama**:

   * After setting the environment variable, run Ollama again:

     ```bash
     ollama serve
     ```

---

### **Step 2: Download and Install ngrok**

1. **Install ngrok**:

   * For Ubuntu/Fedora/Arch, you can install ngrok using the package manager or download the binary directly from ngrok’s website.

   **For Ubuntu/Fedora/Arch:**

   * Install ngrok via `snap`:

     ```bash
     sudo snap install ngrok
     ```

   **Alternatively (for Arch or manual install)**:

   * Download the latest ngrok binary from the [ngrok website](https://ngrok.com/download).

     ```bash
     wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.zip
     unzip ngrok-v3-stable-linux-amd64.zip
     sudo mv ngrok /usr/local/bin/
     ```

2. **Verify installation**:

   ```bash
   ngrok version
   ```

---

### **Step 3: Create an ngrok Account and Get Your Auth Token**

1. **Sign up for ngrok**:

   * Go to [ngrok's signup page](https://dashboard.ngrok.com/signup).
   * Sign up using either your email or GitHub account.

2. **Get your auth token**:

   * After signing in, go to [ngrok's auth token page](https://dashboard.ngrok.com/get-started/your-authtoken).
   * Copy the auth token.

---

### **Step 4: Configure ngrok**

1. **Set up your ngrok configuration**:

   * Open your terminal and configure ngrok by adding your auth token:

     ```bash
     ngrok config add-authtoken YOUR_AUTH_TOKEN
     ```

     Replace `YOUR_AUTH_TOKEN` with the token you copied from the ngrok dashboard.

2. **Start ngrok**:

   * Start ngrok with the following command to expose your local Ollama server to the internet:

     ```bash
     ngrok http 11434 --response-header-add "X-Email: your-email@example.com" --response-header-add "Access-Control-Expose-Headers: X-Email" --response-header-add "Access-Control-Allow-Headers: ngrok-skip-browser-warning" --response-header-add 'Access-Control-Expose-Headers: *'
     ```

   * This will create a forwarding URL such as:

     ```bash
     Forwarding  https://abcd1234.ngrok-free.app -> http://localhost:11434
     ```

3. **Copy the HTTPS forwarding URL**:

   * This URL will allow external access to your Ollama server. You can now share this URL or use it in applications.

---

### **Step 5: Verify the Setup**

1. **Visit the ngrok URL**:

   * Open a web browser and go to your ngrok URL, adding `/api/version` to check the version of Ollama. Example:

     ```bash
     https://abcd1234.ngrok-free.app/api/version
     ```

2. **Check the response**:

   * You should see a JSON response with the version information for Ollama. For example:

     ```json
     {
       "version": "1.2.3"
     }
     ```

3. **Check the response headers**:

   * Use your browser's Developer Tools (press `F12` and go to the `Network` tab) to inspect the response headers.
   * Ensure that `Access-Control-Allow-Origin` is present and includes `*`.

---

### **Important Notes**

1. **Retrying if necessary**:

   * If you encounter issues, try:

     * Stopping ngrok (`Ctrl+C`) and restarting it.
     * Checking the ngrok dashboard at [http://localhost:4040](http://localhost:4040) to inspect requests and responses.

2. **Cache issues**:

   * Clear your browser cache or try using incognito mode if you encounter old data.
   * Use a unique query parameter (e.g., `?t=123`) to bypass cache.

3. **Formatting the URL correctly**:

   * Use the exact ngrok URL without a trailing slash.
   * Ensure that the forwarded URL is used exactly as provided.

4. **Keep ngrok running**:

   * Keep the terminal with ngrok running to maintain the exposed URL.

---

### **Troubleshooting**

1. **CORS errors**:

   * If you see CORS errors, double-check that the `OLLAMA_ORIGINS` environment variable is correctly set and that Ollama is running.

2. **Ngrok tunnel issues**:

   * Ensure that the port (`11434`) is correct, and Ollama is running on that port.

3. **Security warnings**:

   * Ngrok might show a warning about the security of the connection. This is normal for temporary URLs and can be safely bypassed for testing purposes.

4. **Automated test failure**:

   * If automated tests continue to fail, try restarting the ngrok tunnel for a new URL.

---
