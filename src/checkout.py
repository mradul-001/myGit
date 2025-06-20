import os

def checkout(commit_hash):
    
    ROOT = '.mygit'
    objects = os.path.join(ROOT, 'objects')
    commit_file = os.path.join(objects, commit_hash)

    if not os.path.exists(commit_file):
        print("Invalid commit hash.")
        return

    with open(commit_file, 'r') as f:
        lines = f.readlines()

    # Skip metadata (first 3 lines)
    for line in lines[3:]:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        filename, file_hash = parts
        blob_path = os.path.join(objects, file_hash)
        if os.path.exists(blob_path):
            with open(blob_path, 'r') as bf:
                content = bf.read()
            with open(filename, 'w') as outf:
                outf.write(content)

    with open(os.path.join(ROOT, 'HEAD'), 'w') as f:
        f.write(commit_hash)

    print(f"Checked out to {commit_hash}")
