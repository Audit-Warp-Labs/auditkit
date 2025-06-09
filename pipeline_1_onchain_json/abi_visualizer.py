# Creating content for pipeline_1_onchain_json/abi_visualizer.py

from json_parser import extract_entry_functions

def print_abi_summary(json_data):
    entry_funcs = extract_entry_functions(json_data)
    print("=== ABI Summary ===")
    for f in entry_funcs:
        print(f"Function: {f['name']}")
        print(f"  Params: {f['parameters']}")
        print(f"  Visibility: {f['visibility']}")
        print(f"  Generic: {f.get('generic_type_params', [])}")
        print("---------------")


# Writing files
base_path = "/mnt/data/SuiAuditWarpToolkit/pipeline_1_onchain_json/"

files_to_write = {
    "json_parser.py": json_parser_code,
    "entry_function_audit.py": entry_function_audit_code,
    "ownership_checker.py": ownership_checker_code,
    "capability_analyzer.py": capability_analyzer_code,
    "abi_visualizer.py": abi_visualizer_code,
}

for filename, content in files_to_write.items():
    with open(base_path + filename, "w") as f:
        f.write(content)

"SuiAuditWarpToolkit/pipeline_1_onchain_json/ scripts generated."
