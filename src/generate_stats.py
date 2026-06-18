import os

def generate_stats():
    files = 0
    for root, dirs, filenames in os.walk("."):
        # Exclude .git directory
        if ".git" in root:
            continue
        files += len(filenames)

    with open("stats.md", "w") as f:
        f.write(f"Total files: {files}\n")
    print("Project statistics generated.")

if __name__ == "__main__":
    generate_stats()
