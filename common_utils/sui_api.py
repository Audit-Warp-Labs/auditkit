import subprocess
import json

def fetch_module_json(package_id):
    try:
        result = subprocess.run(
            ["sui", "client", "object", package_id],
            capture_output=True,
            text=True
        )
        return json.loads(result.stdout)
    except Exception as e:
        print(f"[ERROR] Failed to fetch module JSON: {e}")
        return None

def dry_run_entry(package_id, function, args):
    # Stub for dry-run execution
    cmd = ["sui", "client", "dry-run", package_id, "--function", function] + args
    return subprocess.run(cmd, capture_output=True, text=True).stdout

# Example
if __name__ == "__main__":
    module = fetch_module_json("0xabc...")
    if module:
        print("Module fetched successfully.")
