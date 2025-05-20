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

