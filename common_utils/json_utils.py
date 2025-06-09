import json

def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def extract_entry_functions(json_data):
    try:
        return json_data["module"]["exposed_functions"]
    except KeyError:
        return []

def get_structs(json_data):
    return json_data.get("module", {}).get("structs", [])

def get_module_name(json_data):
    return json_data.get("module", {}).get("name", "Unknown")

# Example usage
if __name__ == "__main__":
    data = load_json("module.json")
    entries = extract_entry_functions(data)
    print(f"Entry Functions: {[e['name'] for e in entries]}")
