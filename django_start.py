#!/Users/grosnet-/.brew/bin/python3
#!/usr/bin/python3

import os, argparse, json
from importlib import import_module
from re import sub, search

def make_project(name):
    os.system("pip3 install -r requirements.txt")
    os.system("python3 -m django startproject {}".format(name))
    with open("{}/{}/settings.py".format(name, name), "a") as file:
        file.write("\nimport sys\n")
        file.write("\nPROJECT_DIR = os.path.dirname(os.path.realpath(__file__))\nROOT_DIR = os.path.dirname(PROJECT_DIR)\nAPPS_DIR = os.path.realpath(os.path.join(ROOT_DIR, 'apps'))\nsys.path.append(APPS_DIR)\n")
        file.write("\nfrom .additionals import ADD_APPS\nINSTALLED_APPS += ADD_APPS\n")
    os.mkdir("{}/apps".format(name))
    with open("{}/{}/additionals.py".format(name, name), "a") as f:
        f.write("ADD_APPS = ")
        json.dumps(["commands"], f, indent=4)
    os.mkdir("{}/apps/commands".format(name))
    os.system("python3 -m django startapp commands {}/apps/commands".format(name))
    os.makedirs("{}/apps/commands/management/commands".format(name))
    os.system("touch {}/apps/commands/management/__init__.py {}/apps/commands/management/commands/__init__.py".format(name, name))
    os.system("mv add_app.py {}/apps/commands/management/commands".format(name))

def make_wdir_app(proj, name):
    os.system("python3 {}/manage.py add_app {}".format(proj, name))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apps", nargs='+', default=[], help="List of project applications")
    parser.add_argument("-p", "--project", required=True, help="Project name")
    args = parser.parse_args()
    if len(args.project) > 0:
        make_project(args.project)
        for app in args.apps:
            make_wdir_app(args.project, app)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
