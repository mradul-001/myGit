import os
import time

def log():
    base = ".mygit"
    head = os.path.join(base, "HEAD")

    with open(head, 'r') as f:
        ref = f.read().strip()

    if ref.startswith("ref:"):
        ref_path = os.path.join(base, ref.split(":", 1)[1])
        with open(ref_path, 'r') as f:
            currentCommit = f.read().strip()
    else:
        # Detached HEAD mode
        currentCommit = ref

    while True:
        commitfile = os.path.join(base, "objects", currentCommit)
        if not os.path.exists(commitfile):
            break

        with open(commitfile, 'r') as f:
            lines = f.readlines()
            if len(lines) < 3:
                break
            parent = lines[0].strip().split()[1]
            message = lines[1].strip().split(" ", 1)[1]
            timestamp = int(lines[2].strip().split()[1])
            formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

            print(f"\n\x1b[1mcommit\x1b[0m {currentCommit}")
            print(f"Date:   {formatted_time}")
            print(f"\n    {message}")

        if not parent or parent.startswith("ref:"):
            break
        currentCommit = parent
