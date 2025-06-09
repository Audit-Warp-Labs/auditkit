from json_parser import extract_entry_functions

def find_capability_usage(json_data):
    findings = []
    entry_funcs = extract_entry_functions(json_data)
    for func in entry_funcs:
        params = func.get('parameters', [])
        for p in params:
            if 'Cap' in str(p):  # heuristic
                findings.append({
                    "function": func.get("name"),
                    "capability_type": p
                })
    return findings
