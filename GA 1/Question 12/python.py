import json

# Paste your key=value pairs as a multiline string
raw_input = """
name=John
age=30
enabled=true
city=New York
"""

# Parse into dictionary
result = {}
for line in raw_input.strip().splitlines():
    if '=' in line:
        key, value = line.split('=', 1)
        result[key.strip()] = value.strip()

# Convert to JSON
json_output = json.dumps(result, indent=2)
print(json_output)

