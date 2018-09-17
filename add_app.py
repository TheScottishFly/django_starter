from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    args = '<app_name>'

    def handle(self, *args, **kwargs):
        with open("{}/{}/additionals.py".format(settings.BASE_DIR, settings.BASE_DIR.split("/")[-1]), "w+") as f:
            for line in f.readlines():
                if ']' in line:
                    f.write("    {}\n".format(args[0]))
                f.write(line)
