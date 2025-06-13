import os
import json
import yaml
import re

def extract_metadata_and_content(md_text):
    # Match the YAML front matter block between ---
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', md_text, re.DOTALL)
    if not match:
        return None

    yaml_block, content = match.groups()

    try:
        metadata = yaml.safe_load(yaml_block)
    except yaml.YAMLError:
        return None

    title = metadata.get("title")
    url = metadata.get("original_url")
    downloaded_at = metadata.get("downloaded_at")

    if not all([title, url, downloaded_at]):
        return None

    # Split content into lines and clean them
    content_lines = content.strip().splitlines()
    cleaned_lines = []

    for line in content_lines:
        line = line.strip()

        # Skip repeated markdown links to title
        if line.lower().startswith("[") and title.split(".", 1)[-1].strip().lower() in line.lower():
            continue

        # Skip markdown underline headings like "======" or "------"
        if re.match(r'^=+$', line) or re.match(r'^-+$', line):
            continue

        # Skip standalone navigation lines
        if re.match(r'^\s*\[(Previous|Next).*?\]\(.*?\)\s*$', line, re.IGNORECASE):
            continue

        cleaned_lines.append(line)

       # Join cleaned lines
    cleaned_content = " ".join(cleaned_lines).strip()

    # 🔥 Remove inline navigation links like "[Previous...](...)" or "[Next...](...)" anywhere in text
    cleaned_content = re.sub(r'\[Previous.*?\]\(.*?\)', '', cleaned_content, flags=re.IGNORECASE)
    cleaned_content = re.sub(r'\[Next.*?\]\(.*?\)', '', cleaned_content, flags=re.IGNORECASE)

    # 🔥 Remove "**NOTE**: ..." or "NOTE: ..." at the beginning of content
    cleaned_content = re.sub(r'^(\*\*NOTE\*\*|NOTE|Note):\s*', '', cleaned_content, flags=re.IGNORECASE)

    # Normalize whitespace
    cleaned_content = re.sub(r'\s+', ' ', cleaned_content)


    return {
        "title": title,
        "source": url,
        "content": cleaned_content,
        "downloaded_at": downloaded_at
    }


def convert_all_md_to_json(folder_path):
    output = []

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".md"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                md_text = f.read()
                result = extract_metadata_and_content(md_text)
                if result:
                    output.append(result)
                else:
                    print(f"⚠️ Skipped: {filename} (bad metadata format)")

    return output

if __name__ == "__main__":
    input_folder = "tds_pages_md"
    output_json = "tds_content.json"

    data = convert_all_md_to_json(input_folder)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Converted {len(data)} markdown files to {output_json}")
