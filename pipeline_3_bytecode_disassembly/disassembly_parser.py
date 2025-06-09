import re

def parse_disassembled_output(disassembled_text):
    functions = {}
    current_function = None
    current_instructions = []

    for line in disassembled_text.splitlines():
        if line.startswith("function "):
            if current_function:
                functions[current_function] = current_instructions
            current_function = line.strip().split()[1].replace(":", "")
            current_instructions = []
        elif line.strip().startswith("0x"):
            current_instructions.append(line.strip())

    if current_function:
        functions[current_function] = current_instructions

    return functions

# Example usage
if __name__ == "__main__":
    sample_output = open("disassembled_output.txt").read()
    parsed = parse_disassembled_output(sample_output)
    for fn, instructions in parsed.items():
        print(f"\nFunction: {fn}")
        for ins in instructions:
            print(f"  {ins}")
