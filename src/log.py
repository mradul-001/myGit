import os
import time

def log():
    base = ".mygit"
    head = os.path.join(base, "HEAD")

    with open(head, 'r') as f:
        currentCommit = f.read().strip()

    while True:
        commitfile = os.path.join(base, "objects", currentCommit)
        with open(commitfile, 'r') as f:
            lines = f.readlines()
            parent = lines[0].strip().split()[1]
            message = lines[1].strip().split(" ", 1)[1]
            timestamp = int(lines[2].strip().split()[1])
            formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

            print(f"\n\x1b[1mcommit\x1b[0m {currentCommit}")
            print(f"Date:   {formatted_time}")
            print(f"\n    {message}")

        if parent != "ref:refs/heads/master":
            currentCommit = parent
        else:
            break
