def check_for_unsafe_patterns(source_code):
    issues = []
    if "public(friend)" in source_code:
        issues.append("Warning: Usage of public(friend) found.")
    if "::borrow_global_mut" in source_code:
        issues.append("Potential unsafe borrow_global_mut usage.")
    if "::move_from" in source_code:
        issues.append("Resource removal (move_from) detected.")
    return issues


