from django.core.management.base import BaseCommand
from django.conf import settings
import os

class Command(BaseCommand):
    args = '<app_name>'
    help = "App name to be added"

    def handle(self, *args, **kwargs):
        try:
            base = settings.BASE_DIR
            proj = settings.BASE_DIR.split("/")[-1]
            name = args[0]
        except:
            self.stdout.write("WARNING !!")
        with open("{}/{}/additionals.py".format(base, proj), "w+") as f:
            for line in f.readlines():
                if ']' in line:
                    f.write("    {}\n".format(name))
                f.write(line)
        os.mkdir("{}/apps/{}".format(base, name))
        os.system("python3 -m django startapp {} {}/apps/{}".format(name, base, name))
        self.stdout.write("{} added !".format(name))
