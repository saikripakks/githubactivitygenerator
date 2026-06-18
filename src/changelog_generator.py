import os
import subprocess

def create_changelog():
    try:
        with open("CHANGELOG.md", "w") as f:
            subprocess.run(["git", "log", "--oneline"], stdout=f, check=True)
        print("CHANGELOG.md generated successfully.")
    except Exception as e:
        print(f"Error generating changelog: {e}")

if __name__ == "__main__":
    create_changelog()
