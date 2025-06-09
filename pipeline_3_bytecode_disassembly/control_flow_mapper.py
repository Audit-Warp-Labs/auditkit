def extract_jump_targets(instructions):
    targets = set()
    for instr in instructions:
        if "br" in instr or "branch" in instr:
            parts = instr.split()
            for part in parts:
                if part.startswith("L"):
                    targets.add(part)
    return targets

def map_control_flow(function_map):
    flow_map = {}
    for fn, instrs in function_map.items():
        jump_targets = extract_jump_targets(instrs)
        flow_map[fn] = {
            "instruction_count": len(instrs),
            "jump_targets": list(jump_targets)
        }
    return flow_map

# Example usage
if __name__ == "__main__":
    from disassembly_parser import parse_disassembled_output
    text = open("disassembled_output.txt").read()
    fn_map = parse_disassembled_output(text)
    flow = map_control_flow(fn_map)
    print(flow)
