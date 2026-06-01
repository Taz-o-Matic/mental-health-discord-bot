import json

def transform_to_bot_format():
    with open('hotlines_temp.json', 'r', encoding='utf-8') as f:
        source = json.load(f)

    bot_format = {"countries": {}}

    for country, data in source.items():
        country_name = country.strip()
        bot_format["countries"][country_name] = {
            "national": [],
            "states": {},
            "provinces": {}
        }

        if isinstance(data, dict) and "phones" in data:
            for phone in data.get("phones", []):
                entry = {
                    "name": phone.get("name", "Crisis Line"),
                    "number": phone.get("number", ""),
                    "notes": phone.get("description", ""),
                    "url": phone.get("url", "")
                }
                bot_format["countries"][country_name]["national"].append(entry)

    with open('hotlines.json', 'w', encoding='utf-8') as f:
        json.dump(bot_format, f, indent=2, ensure_ascii=False)

    print(f"✅ Transformed {len(bot_format['countries'])} countries")

if __name__ == "__main__":
    transform_to_bot_format()
