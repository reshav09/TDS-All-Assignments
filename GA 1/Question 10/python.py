import json

# Original data
products = [#paste your json data here]

# Step 1: Filter
filtered = [p for p in products if p['price'] >= 139.55]

# Step 2: Sort
sorted_products = sorted(
    filtered,
    key=lambda p: (p['category'], -p['price'], p['name'])
)

# Step 3: Minified JSON string
minified_json = json.dumps(sorted_products, separators=(',', ':'))
print(minified_json)

