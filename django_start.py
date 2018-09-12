#!/Users/grosnet-/.brew/bin/python3
#!/usr/bin/python3

import os, argparse

def make_project(name):
    os.system("pip3 install -r requirements.txt")
    os.system("python3 -m django startproject {}".format(name))
    os.mkdir("{}/apps".format(name))

def make_app(proj, name):
    os.mkdir("{}/apps/{}".format(proj, name))
    os.system("python3 -m django startapp {} {}/apps/{}".format(name, proj, name))

def write_app(proj, name):
    pass

def write_url()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apps", nargs='+', default=[], help="List of project applications")
    parser.add_argument("-p", "--project", required=True, help="Project name")
    args = parser.parse_args()
    if len(args.project) > 0:
        make_project(args.project)
        for app in args.apps:
            make_app(args.project, app)
            write_app(args.project, app)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
