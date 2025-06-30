import os
import glob

def branch(bname = None):
    
    base = ".mygit"

    if bname:
        with open(os.path.join(base, "index"), 'r') as f:
            if f.read().strip() != '':
                print("There are changes that need to be committed before switching to a branch.")
                return

        new_branch = os.path.join(base, "refs", "heads", bname)
        if os.path.exists(new_branch):
            print("Branch already exists")
            return

        with open(os.path.join(base, "HEAD"), 'r') as f:
            ref = f.read().strip()
        current_branch = os.path.join(base, ref.split(":", 1)[1])


        with open(current_branch, 'r') as f:
            current_commit = f.read().strip()

        with open(new_branch, 'w') as f:
            f.write(current_commit)

        print(f"Branch '{bname}' created at {current_commit}")

    else:

        with open(os.path.join(base, "HEAD"), 'r') as f:
            cbranch = f.read().strip().split(":")[1].split("/")[-1]

        # list all branches
        for ele in glob.glob(os.path.join(base, "refs", "heads", "*")):
            b = ele.strip().split("/")[-1]
            if b == cbranch:
                print(b, end=" ")
                print("*")
            else:
                print(b)