import os


def checkout(arg1, arg2=None):

    ROOT = ".mygit"

    if arg1 == "-b":
        # handle brach change
        bname = arg2
        bhead = os.path.join(ROOT, "refs", "heads", bname)

        if not os.path.exists(bhead):
            print(f"{bname} do not exists.")
            return
        else:
            with open(os.path.join(ROOT, "HEAD"), "w") as f:
                f.write(f"ref:refs/heads/{bname}")
            f.close()

    else:
        # handle commit switching
        objects = os.path.join(ROOT, "objects")
        commit_file = os.path.join(objects, arg1)

        if not os.path.exists(commit_file):
            print("Invalid commit hash.")
            return

        with open(commit_file, "r") as f:
            lines = f.readlines()

        for line in lines[3:]:

            parts = line.strip().split()
            if len(parts) != 2:
                continue

            file_hash, filename = parts
            blob_path = os.path.join(objects, file_hash)

            if os.path.exists(blob_path):
                content = ""
                with open(blob_path, "r") as bf:
                    for i, line in enumerate(bf):
                        if i < 2:
                            continue
                        content += line
                with open(filename, "w") as outf:
                    outf.write(content)

        # get the headfile of the current branch and change it
        with open(os.path.join(ROOT, "HEAD"), "r") as f:
            branchHEAD = f.read().strip().split(":")[1]
            with open(os.path.join(ROOT, branchHEAD), "w") as bh:
                bh.write(arg1)
            bh.close()
        f.close()

        print(f"Checked out to {arg1}")
