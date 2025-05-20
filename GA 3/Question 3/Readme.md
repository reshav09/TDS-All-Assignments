Follow these simple steps to generate random US addresses:

#Open Developer Tools

Right-click anywhere on the webpage
Select "Inspect" or "Inspect Element"
Click on the "Console" tab
Paste the Code

#Copy the following JavaScript code:


const textarea = document.getElementById('q-generate-addresses-with-llms');
textarea.style.visibility = 'visible';
textarea.style.opacity = '1';
textarea.style.display = 'block';
textarea.removeAttribute('disabled');

// Step 2: Pre-fill the textarea with the correct JSON structure for generating addresses
const defaultJson = JSON.stringify({
  model: "gpt-4o-mini",
  messages: [
    {
      role: "system",
      content: "Respond in JSON"
    },
    {
      role: "user",
      content: "Generate 10 random addresses in the US"
    }
  ],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "address_response",
      strict: true,
      schema: {
        type: "object",
        properties: {
          addresses: {
            type: "array",
            items: {
              type: "object",
              properties: {
                country: { type: "string" },
                state: { type: "string" },
                apartment: { type: "string" }
              },
              required: ["country", "state", "apartment"],
              additionalProperties: false
            }
          }
        },
        required: ["addresses"],
        additionalProperties: false
      }
    }
  }
}, null, 2);

// Set the default JSON structure in the textarea
textarea.value = defaultJson;

#Paste it into the console
Run the Code

#Press Enter to execute the code
This will make a hidden textarea visible and fill it with JSON
Complete the Process

#Click the "Check" button on the page
