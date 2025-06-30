import os


def init():

    try:
        # path of hidden git directory
        ROOT = ".mygit"
        if os.path.exists(ROOT):
            print("Repository already initialized.")
            return

        # make refs and objects/ folder
        os.makedirs(os.path.join(ROOT, "refs", "heads"), exist_ok=True)
        os.makedirs(os.path.join(ROOT, "objects"), exist_ok=True)

        # make HEAD file
        with open(os.path.join(ROOT, "HEAD"), "w") as f:
            f.write("ref:refs/heads/master\n")

        # make index file
        open(os.path.join(ROOT, "index"), "w").close()
        print("Initialized empty repository.")
    except:
        print("Repository already initialized.")
