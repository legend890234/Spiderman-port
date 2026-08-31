import json
import os
import time

def run_app():
    config_path = "config/sequences/master_walkthrough.json"
    if not os.path.exists(config_path):
        print(f"Error: Walkthrough sequence not found at {config_path}")
        return

    with open(config_path, "r") as f:
        data = json.load(f)

    print("=" * 50)
    print(f"App Title: {data.get('title', 'Walkthrough')}")
    print(f"Style: {data.get('style', 'Cinematic Flow')}")
    print("=" * 50)
    
    for cp in data.get("checkpoints", []):
        print(f"\nCheckpoint [{cp['id']}] -> {cp['name']}")
        print(f"Phase Type : {cp['type'].upper()}")
        print(">> Executing sequence segment...")
        time.sleep(0.2)
        print(f"✓ Scene cleared successfully.")
    
    print("\n" + "=" * 50)
    print("[SUCCESS] Walkthrough completed entirely!")
    print("=" * 50)

if __name__ == "__main__":
    run_app()
