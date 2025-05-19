import json
import os
import re

image_dir = "static/splash"
output_file = "skins.json"


# Split CamelCase: "StreetDemons" → "Street Demons"
def split_camel_case(s):
    # Add space between a lowercase and uppercase letter (e.g., StreetDemons)
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", s)
    # Add space between letters and numbers (e.g., Worlds2018)
    s = re.sub(r"(?<=[a-zA-Z])(?=[0-9])", " ", s)
    return s


def clean_skin_name(filename):
    base = filename.replace("_HD.jpg", "").replace("_HD.png", "")
    base = base.replace("_Skin", "").replace("Skin", "")

    parts = base.split("_")
    if len(parts) >= 2:
        champ = parts[0].capitalize()
        skin_parts = parts[1:]

        if any("original" in part.lower() for part in skin_parts):
            return champ

        # Clean and format each part
        skin_name = " ".join(split_camel_case(part).title() for part in skin_parts)

        # Preserve known acronyms
        skin_name = (
            skin_name.replace("Project", "PROJECT")
            .replace("Fnatic", "FNATIC")
            .replace("Ssg", "SSG")
            .replace("Tpa", "TPA")
            .replace("Sktt1", "SKT T1")
            .replace("Ig", "IG")
            .replace("Fpx", "FPX")
            .replace("Edg", "EDG")
        )

        return f"{skin_name} {champ}"
    else:
        return base.title()


# Build the dictionary
skin_map = {
    file: clean_skin_name(file)
    for file in os.listdir(image_dir)
    if file.endswith((".jpg", ".png"))
}

with open(output_file, "w") as f:
    json.dump(skin_map, f, indent=2)

print(f"✅ Generated {len(skin_map)} skins in {output_file}.")
