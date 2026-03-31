import os
import json

def main():
    config_dir = os.path.join(os.getcwd(), ".claude")
    config_path = os.path.join(config_dir, "config.json")
    project_dir = os.path.join(os.getcwd(), "project")

    # Ensure .claude directory exists
    os.makedirs(config_dir, exist_ok=True)

    # Prompt for sessionKey
    session_key = input("Enter your Claude sessionKey: ").strip()
    if not session_key:
        print("Error: sessionKey cannot be empty.")
        return

    # Write config.json
    config = {"sessionKey": session_key}
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Created {config_path}")

    # Ensure project directory exists
    os.makedirs(project_dir, exist_ok=True)
    print(f"Ensured {project_dir} exists.")

    print("Initialization complete.")

if __name__ == "__main__":
    main()import os
import json

def main():
    config_dir = os.path.join(os.getcwd(), ".claude")
    config_path = os.path.join(config_dir, "config.json")
    project_dir = os.path.join(os.getcwd(), "project")

    # Ensure .claude directory exists
    os.makedirs(config_dir, exist_ok=True)

    # Prompt for sessionKey
    session_key = input("Enter your Claude sessionKey: ").strip()
    if not session_key:
        print("Error: sessionKey cannot be empty.")
        return

    # Write config.json
    config = {"sessionKey": session_key}
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Created {config_path}")

    # Ensure project directory exists
    os.makedirs(project_dir, exist_ok=True)
    print(f"Ensured {project_dir} exists.")

    print("Initialization complete.")

if __name__ == "__main__":
    main()
