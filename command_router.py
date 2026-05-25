import subprocess
import os
from rapidfuzz import fuzz


def similar(a, b):
    return fuzz.partial_ratio(a, b) > 70


# -----------------------------
# COMMAND FUNCTIONS
# -----------------------------

def clear_screen():
    print("✓ Clearing screen...")
    os.system("cls")


def list_files():
    print("✓ Listing files...")
    subprocess.run("dir", shell=True)


def open_vscode():
    print("✓ Opening VS Code...")
    subprocess.run("code .", shell=True)


def show_directory():
    print("✓ Showing current directory...")
    subprocess.run("cd", shell=True)


def git_status():
    print("✓ Checking git status...")
    subprocess.run("git status", shell=True)


def install_flask():
    print("✓ Installing Flask...")
    subprocess.run("pip install flask", shell=True)


def run_python_file():
    print("✓ Running calculator.py...")
    subprocess.run("python calculator.py", shell=True)


def create_folder():
    print("✓ Creating folder 'backend'...")
    os.makedirs("backend", exist_ok=True)


def commit_changes():
    print("✓ Committing changes...")

    commit_message = "voice-agent-auto-commit"

    subprocess.run("git add .", shell=True)

    subprocess.run(
        f'git commit -m "{commit_message}"',
        shell=True
    )


# -----------------------------
# COMMAND MAP
# -----------------------------

COMMANDS = {
    "exit": None,

    "clear screen": clear_screen,
    "clear": clear_screen,

    "list files": list_files,
    "show files": list_files,

    "open vscode": open_vscode,
    "open vs code": open_vscode,
    "open editor": open_vscode,

    "show current directory": show_directory,

    "git status": git_status,

    "install flask": install_flask,

    "run file": run_python_file,
    "run app": run_python_file,

    "create folder": create_folder,

    "commit changes": commit_changes,
}


# -----------------------------
# MAIN ROUTER
# -----------------------------

def handle_command(text):

    text = text.lower().strip()

    print(f"\nProcessed command: {text}")

    for command in COMMANDS:

        if similar(text, command):

            if command == "exit":
                print("✓ Exiting assistant...")
                return False

            action = COMMANDS[command]

            if action:
                action()

            return True

    # If no command matched
    print("\n🤖 Sending to AI coding agent:")
    print(text)

    return True