import os
import base64

def load_bytecode_file(file_path):
    with open(file_path, "rb") as f:
        return f.read()

def decode_base64_mv(encoded_string):
    try:
        return base64.b64decode(encoded_string)
    except Exception as e:
        print(f"[ERROR] Failed to decode base64 bytecode: {e}")
        return None

def list_mv_files(directory):
    return [f for f in os.listdir(directory) if f.endswith(".mv")]

# Example usage
if __name__ == "__main__":
    mv_files = list_mv_files("bytecode/")
    for mv in mv_files:
        bytecode = load_bytecode_file(os.path.join("bytecode", mv))
        print(f"Loaded {mv}, size = {len(bytecode)} bytes")
