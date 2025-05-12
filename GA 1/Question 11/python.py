import json

raw_old_config = '''
[
  {"key": "setting1", "value": "on", "enabled": false}
]
'''

raw_new_config = '''
[
  {"key": "setting1", "value": "off", "enabled": true}
]
'''



# DO NOT replace 'true' or 'false' — let json.loads() handle them
old_confign = json.loads(raw_old_config)
new_confign = json.loads(raw_new_config)


# Safe dictionary creation
old_dict = {item['key']: item for item in old_confign if isinstance(item, dict) and 'key' in item}
new_dict = {item['key']: item for item in new_confign if isinstance(item, dict) and 'key' in item}


changed_settings = []
for key in new_dict:
    if key in old_dict:
        old_val = old_dict[key].get('value')
        new_val = new_dict[key].get('value')
        if old_val != new_val:
            changed_settings.append({
                "key": key,
                "old_value": old_val,
                "new_value": new_val
            })


# Output results
print(f"Total changed settings: {len(changed_settings)}")
