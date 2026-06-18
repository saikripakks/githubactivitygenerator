import os
from datetime import datetime

# Path relative to project root
readme_path = "README.md"

def update_readme():
    try:
        with open(readme_path, "a") as f:
            f.write(f"\n\nLast updated: {datetime.now()}")
        print("README.md updated successfully.")
    except Exception as e:
        print(f"Error updating README.md: {e}")

if __name__ == "__main__":
    update_readme()
