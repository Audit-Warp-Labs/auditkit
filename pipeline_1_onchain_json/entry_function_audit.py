from json_parser import extract_entry_functions

def audit_entry_functions(json_data):
    results = []
    entry_funcs = extract_entry_functions(json_data)
    for func in entry_funcs:
        name = func.get('name')
        params = func.get('parameters', [])
        checks_sender = any('tx_context::sender' in str(param) for param in params)
        result = {
            "function": name,
            "parameters": params,
            "checks_sender": checks_sender,
            "public": func.get("visibility") == "public"
        }
        results.append(result)
    return results

