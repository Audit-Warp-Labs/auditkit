import re
from parser import extract_functions

def build_call_graph(source_code):
    functions = extract_functions(source_code)
    calls = {}
    for _, name, _ in functions:
        pattern = re.compile(rf'\\b{name}\\b\\s*\\(', re.MULTILINE)
        matches = pattern.findall(source_code)
        calls[name] = matches
    return calls


# Writing files to pipeline_2_move_source
base_path = "/mnt/data/SuiAuditWarpToolkit/pipeline_2_move_source/"

files_to_write = {
    "parser.py": parser_code,
    "linter.py": linter_code,
    "spec_checker.py": spec_checker_code,
    "resource_usage.py": resource_usage_code,
    "function_graph.py": function_graph_code,
}

for filename, content in files_to_write.items():
    with open(base_path + filename, "w") as f:
        f.write(content)

"SuiAuditWarpToolkit/pipeline_2_move_source/ scripts generated."
