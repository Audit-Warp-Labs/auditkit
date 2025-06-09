import json

def load_sui_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def extract_entry_functions(json_data):
    return json_data.get('entry_functions', [])

def extract_structs(json_data):
    return json_data.get('structs', [])

def extract_module_info(json_data):
    return {
        "name": json_data.get("name"),
        "address": json_data.get("address"),
        "friends": json_data.get("friends", [])
    }


