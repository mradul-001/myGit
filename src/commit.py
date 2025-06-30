import os
import hashlib
import time

def commit(message):
    ROOT = '.mygit'
    indexFile = os.path.join(ROOT, 'index')
    headFile = os.path.join(ROOT, 'HEAD')
    objects = os.path.join(ROOT, 'objects')

    if not os.path.exists(indexFile):
        print("Nothing to commit.")
        return

    with open(indexFile, 'r') as f:
        index_data = f.read()

    if index_data.strip() == '':
        print("Nothing to commit.")
        return

    with open(headFile, 'r') as f:
        branch = f.read().strip().split(":")[1]
    branchHead = os.path.join(ROOT, branch)

    parent = "ref:refs/heads/master"
    if os.path.exists(branchHead):
        with open(branchHead, 'r') as bf:
            parent = bf.read().strip()

    timestamp = str(int(time.time()))
    commit_content = f"parent {parent}\nmessage {message}\ntime {timestamp}\n{index_data}"
    commit_hash = hashlib.sha1(commit_content.encode()).hexdigest()

    with open(os.path.join(objects, commit_hash), 'w') as f:
        f.write(commit_content)

    with open(branchHead, 'w') as f:
        f.write(commit_hash)

    open(indexFile, 'w').close()
    print(f"Committed as {commit_hash}")
