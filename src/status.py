import os

def status():

    ROOT = '.mygit'
    if not os.path.exists(ROOT):
        print("myGit repository not found.")
        return

    indexFile = os.path.join(ROOT, 'index')

    if not os.path.exists(indexFile):
        print("No index file found.")
        return

    with open(indexFile, 'r') as f:
        lines = f.readlines()

    if not lines:
        print("There are no staged changes to commit")
        return

    print("Staged files:")
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 1:
            filename = parts[1]
            print(f" - {filename}")