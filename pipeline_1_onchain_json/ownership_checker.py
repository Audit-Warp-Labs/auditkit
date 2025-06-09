from json_parser import extract_structs

def detect_owner_patterns(structs):
    potential_owners = []
    for s in structs:
        fields = s.get("fields", [])
        for field in fields:
            if "owner" in field.get("name", "").lower() and field.get("type") == "address":
                potential_owners.append({
                    "struct": s.get("name"),
                    "owner_field": field
                })
    return potential_owners


