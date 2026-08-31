import json
import time

def load_walkthrough():
    with open('config/sequences/master_walkthrough.json', 'r') as f:
        data = json.load(f)
    return data

def play_sequence():
    walkthrough = load_walkthrough()
    print(f"=== {walkthrough['title']} ===")
    print(f"Presentation Style: {walkthrough['style']}\n")
    
    for cp in walkthrough['checkpoints']:
        print(f"[CHECKPOINT {cp['id']}] Type: {cp['type'].upper()} | Scene: {cp['name']}")
        time.sleep(0.5)  # Simulate smooth cinematic pacing
    
    print("\nWalkthrough sequence loop complete!")

if __name__ == '__main__':
    play_sequence()
