import os
import sys
import json
import shutil

def load_config():
    config_path = os.path.join(os.getcwd(), ".claude", "config.json")
    if not os.path.exists(config_path):
        print("Error: .claude/config.json not found. Run project_init.py first.")
        sys.exit(1)
    with open(config_path) as f:
        return json.load(f)

def push(files=None):
    # Placeholder: implement push logic to Claude Project
    print(f"Pushing files: {files if files else 'all in project/'}")
    # ...

def pull(files=None):
    # Placeholder: implement pull logic from Claude Project
    print(f"Pulling files: {files if files else 'all in project/'}")
    # ...

def main():
    if len(sys.argv) < 2:
        print("Usage: project_sync.py [push|pull] [file1 file2 ...]")
        sys.exit(1)
    command = sys.argv[1]
    files = sys.argv[2:] if len(sys.argv) > 2 else None
    load_config()  # Ensure config exists
    if command == "push":
        push(files)
    elif command == "pull":
        pull(files)
    else:
        print("Unknown command. Use push or pull.")
        sys.exit(1)

if __name__ == "__main__":
    main()import os
import sys
import json
import shutil

def load_config():
    config_path = os.path.join(os.getcwd(), ".claude", "config.json")
    if not os.path.exists(config_path):
        print("Error: .claude/config.json not found. Run project_init.py first.")
        sys.exit(1)
    with open(config_path) as f:
        return json.load(f)

def push(files=None):
    # Placeholder: implement push logic to Claude Project
    print(f"Pushing files: {files if files else 'all in project/'}")
    # ...

def pull(files=None):
    # Placeholder: implement pull logic from Claude Project
    print(f"Pulling files: {files if files else 'all in project/'}")
    # ...

def main():
    if len(sys.argv) < 2:
        print("Usage: project_sync.py [push|pull] [file1 file2 ...]")
        sys.exit(1)
    command = sys.argv[1]
    files = sys.argv[2:] if len(sys.argv) > 2 else None
    load_config()  # Ensure config exists
    if command == "push":
        push(files)
    elif command == "pull":
        pull(files)
    else:
        print("Unknown command. Use push or pull.")
        sys.exit(1)

if __name__ == "__main__":
    main()
