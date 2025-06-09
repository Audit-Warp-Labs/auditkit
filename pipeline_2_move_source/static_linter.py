def lint_move_file(file_path):
    open the .move file and read lines

    issues = []

    for line_number, line in enumerate(lines):
        if line contains "assert!(false" or "TODO":
            issues.append(f"Line {line_number}: Suspicious assertion or TODO comment")

        if line exceeds 120 characters:
            issues.append(f"Line {line_number}: Line too long")

        if line has unnecessary use of "copy" or "move":
            issues.append(f"Line {line_number}: Redundant resource operation")

    return issues

# Entry point
if __name__ == "__main__":
    for file in sources_dir:
        issues = lint_move_file(file)
        print(f"Issues in {file}:")
        for issue in issues:
            print(f"  - {issue}")
