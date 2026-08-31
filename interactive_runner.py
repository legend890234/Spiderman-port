import json
import sys
import time

def load_walkthrough():
    with open('config/sequences/master_walkthrough.json', 'r') as f:
        return json.load(f)

def run_interactive_flow():
    data = load_walkthrough()
    print(f"\n==================================================")
    print(f" {data['title']}")
    print(f" Style: {data['style']} (No Commentary)")
    print(f"==================================================")
    print("Controls: Press [ENTER] to execute transition | 'q' to quit\n")
    
    total_start = time.time()
    
    for cp in data['checkpoints']:
        print(f"--------------------------------------------------")
        print(f"Checkpoint [{cp['id']}] -> {cp['name']}")
        print(f"Phase Type : {cp['type'].upper()}")
        
        start_time = time.time()
        user_input = input(">> Trigger next sequence segment... ")
        
        if user_input.strip().lower() == 'q':
            print("\nWalkthrough session saved and closed.")
            sys.exit(0)
            
        elapsed = time.time() - start_time
        print(f"✓ Scene cleared in {elapsed:.2f}s (Seamless Flow)")
        
    total_time = time.time() - total_start
    print(f"\n==================================================")
    print(f" [SUCCESS] Walkthrough completed entirely!")
    print(f" Total Sequence Duration: {total_time:.2f} seconds")
    print(f"==================================================")

if __name__ == '__main__':
    run_interactive_flow()
