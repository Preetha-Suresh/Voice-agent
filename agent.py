from dotenv import load_dotenv
import subprocess
import os

load_dotenv()

def send_to_aider(prompt):

    print(f"\n🤖 Sending to aider: {prompt}")

    command = [
        "aider",
        "--model",
        "openrouter/openai/gpt-3.5-turbo",
        "--yes-always",
        "--message",
        prompt
    ]

    env = os.environ.copy()

    subprocess.run(command, env=env)