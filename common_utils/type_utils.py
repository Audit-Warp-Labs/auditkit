def is_capability(type_str):
    return "Cap" in type_str or "capability" in type_str.lower()

def is_address_or_signer(param_type):
    return param_type in ["address", "&signer", "signer"]

def flatten_generic_type(type_info):
    if isinstance(type_info, dict) and "Struct" in type_info:
        return type_info["Struct"]["name"]
    return str(type_info)

# Example usage
if __name__ == "__main__":
    print(is_capability("BurnCap"))
    print(is_address_or_signer("&signer"))
