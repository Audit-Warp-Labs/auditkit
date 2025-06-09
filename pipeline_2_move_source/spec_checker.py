from parser import extract_functions, extract_spec_blocks

def check_missing_specs(source_code):
    specs = extract_spec_blocks(source_code)
    func_names_with_spec = {s[0] for s in specs}
    funcs = extract_functions(source_code)
    results = []
    for is_entry, name, _ in funcs:
        if name not in func_names_with_spec:
            results.append(f"Function '{name}' missing spec block.")
    return results


