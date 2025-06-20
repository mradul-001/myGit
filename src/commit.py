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

    if index_data == '':
        print("Nothing to commit")
        return

    parent = ''
    if os.path.exists(headFile):
        with open(headFile, 'r') as f:
            parent = f.read().strip()

    timestamp = str(int(time.time()))
    commit_content = f"parent {parent}\nmessage {message}\ntime {timestamp}\n{index_data}"
    commit_hash = hashlib.sha1(commit_content.encode()).hexdigest()

    with open(os.path.join(objects, commit_hash), 'w') as f:
        f.write(commit_content)

    with open(headFile, 'w') as f:
        f.write(commit_hash)
    
    open(indexFile, 'w').close()
    print(f"Committed as {commit_hash}")
