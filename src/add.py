import os
import hashlib

def add(filename):
    
    ROOT = '.mygit'
    if not os.path.exists(ROOT):
        print("myGit repository not found.")
        return

    indexFile = os.path.join(ROOT, 'index')
    headFile  = os.path.join(ROOT, 'HEAD')
    objects   = os.path.join(ROOT, 'objects')

    with open(filename, 'r') as f:
        content = f.read()

    contentOfHash = 'blob ' + str(len(content)) + content
    hash = hashlib.sha1(contentOfHash.encode()).hexdigest()

    with open(os.path.join(objects, hash), 'w') as f:
        f.write(contentOfHash)

    update_index(indexFile, filename, hash)
    print(f"Added {filename}")


def update_index(indexFile, filename, hash):
    lines = []
    found = False

    if os.path.exists(indexFile):
        with open(indexFile, 'r') as f:
            for line in f:
                if line.strip().endswith(f"\t{filename}"):
                    lines.append(f"{hash}\t{filename}\n")
                    found = True
                else:
                    lines.append(line)

    if not found:
        lines.append(f"{hash}\t{filename}\n")

    with open(indexFile, 'w') as f:
        f.writelines(lines)
