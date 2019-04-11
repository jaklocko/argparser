import sys

'''This is a simply argument parser, for training purposes'''

version = 0.1

def parse_opts(opts):
    opts = sorted(opts)
    for opt in opts:
        if opt == "--help" or opt == "-h":
            print("""Help Info\n------\nThis program is a simple argument parser\n\n""")
        elif opt == "--version" or opt == "-v":
            print("""Version Info\n------\napp.py""")
            print("v{}\n\n".format(version))

def parse_args(args):
    for arg in args:
        print("Argument:", arg)

def main(args):
    options = []
    arglist = []
    for arg in args:
        if arg.startswith("--") or arg.startswith("-"):
            options.append(arg)
        else:
            arglist.append(arg)

    # print("Options:", options)
    # print("Arguments:", arglist)
    parse_opts(options)
    parse_args(arglist)

if __name__ == '__main__':
    main(sys.argv[1:])
