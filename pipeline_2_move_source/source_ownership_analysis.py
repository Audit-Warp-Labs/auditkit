def parse_ownership_patterns(file_path):
    open file and tokenize each function
    look for:
        - function parameters of type address or &signer
        - usage of tx_context::sender()
        - assert!(sender == owner) or similar checks

    for each entry function:
        determine if access control is present
        if missing or weak, flag a warning

    return list of ownership risk findings

# Entry point
if __name__ == "__main__":
    for file in sources_dir:
        findings = parse_ownership_patterns(file)
        print(f"Ownership analysis of {file}:")
        for finding in findings:
            print(f"  - {finding}")
