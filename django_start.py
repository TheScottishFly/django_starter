#!/Users/grosnet-/.brew/bin/python3
#!/usr/bin/python3

import os, argparse

def make_app(name):
    os.system("pip3 install -r requirements.txt")
    os.system("python3 -m django startproject {}".format(name))
    os.mkdir("{}/apps".format(name))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("app_name", help="Application name")
    args = parser.parse_args()
    if len(args.app_name) > 0:
        make_app(args.app_name)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
