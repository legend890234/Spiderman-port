import json
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_checkpoints():
    path = "config/sequences/master_walkthrough.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f).get("checkpoints", [])
    return [
        {"id": 1, "type": "gameplay", "name": "Fisk Tower Infiltration & Rooftop Pursuit"}
    ]

def play_game():
    checkpoints = load_checkpoints()
    
    for cp in checkpoints:
        clear_screen()
        print("=" * 60)
        print(f"CHECKPOINT [{cp['id']}]: {cp['name']}")
        print(f"Phase Type: {cp['type'].upper()}")
        print("=" * 60)
        
        print("\n[COMMAND DECK - SHIRRAKO WALKTHROUGH FLOW]")
        print(" [w] Web-Zip / Swing Traversal")
        print(" [c] Combat Engagement (Web-Strike & Combo)")
        print(" [g] Deploy Gadget (Impact Webbing)")
        print(" [f] Cinematic Finisher / QTE Trigger")
        print(" [s] Skip / Seamless Flow Advance")
        
        action = input("\nEnter command > ").strip().lower()
        
        if action == 'w':
            print("\n-> Executing fluid web-swinging arc across Manhattan...")
            time.sleep(0.4)
            print("-> Momentum maintained. Entering next zone.")
        elif action == 'c':
            print("\n-> Engaging thugs: Aerial combo executed cleanly!")
            time.sleep(0.4)
            print("-> Focus meter building up. Threat neutralized.")
        elif action == 'g':
            print("\n-> Firing Impact Webbing against wall obstacle...")
            time.sleep(0.4)
            print("-> Target pinned successfully.")
        elif action == 'f':
            print("\n-> Triggering cinematic QTE finisher sequence...")
            time.sleep(0.4)
            print("-> Clean takedown executed with zero commentary flow.")
        else:
            print("\n-> Advancing timeline seamlessly to next checkpoint...")
            time.sleep(0.3)
            
        input("\n[Press ENTER to proceed to next sequence segment...]")

    clear_screen()
    print("=" * 60)
    print("[SUCCESS] Walkthrough segment successfully executed!")
    print("=" * 60)

if __name__ == "__main__":
    play_game()
