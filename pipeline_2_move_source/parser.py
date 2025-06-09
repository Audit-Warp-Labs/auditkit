import re

def extract_functions(source_code):
    function_pattern = re.compile(r'public\\s+(entry\\s+)?fun\\s+(\\w+)\\s*\\((.*?)\\)', re.MULTILINE | re.DOTALL)
    return function_pattern.findall(source_code)

def extract_structs(source_code):
    struct_pattern = re.compile(r'struct\\s+(\\w+)\\s*{(.*?)}', re.MULTILINE | re.DOTALL)
    return struct_pattern.findall(source_code)

def extract_spec_blocks(source_code):
    spec_pattern = re.compile(r'spec\\s+(.*?)\\s*{(.*?)}', re.MULTILINE | re.DOTALL)
    return spec_pattern.findall(source_code)


