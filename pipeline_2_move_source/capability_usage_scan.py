def detect_capabilities(file_path):
    capabilities = []
    open and parse the file for struct names like MintCap, BurnCap, etc.

    for each function:
        check parameters and local variables for capability types
        if capabilities are passed into public/entry functions, flag as a possible risk
        if capabilities are moved or returned, flag for misuse

    return capability scan results

# Entry point
if __name__ == "__main__":
    for move_file in sources_dir:
        scan = detect_capabilities(move_file)
        print(f"Capabilities used in {move_file}:")
        for result in scan:
            print(f"  - {result}")
