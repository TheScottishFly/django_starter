from django.core.management.base import BaseCommand
from django.conf import settings
import os, json

class Command(BaseCommand):
    args = '<app_name>'
    help = "App name to be added"

    def add_arguments(self, parser):
        parser.add_argument('app_name', nargs='+', type=str)

    def handle(self, *args, **kwargs):
        try:
            base = settings.BASE_DIR
            proj = settings.BASE_DIR.split("/")[-1]
            name = kwargs['app_name'][0]
        except:
            self.stdout.write("WARNING !!")
        with open("{}/{}/additionals.py".format(base, proj), "a+") as f:
            f.seek(0)
            input = "".join(f.readlines())
            input = input[11:]
            input = json.loads(input)
            input.append(name)
        with open("{}/{}/additionals.py".format(base, proj), "w+") as f:
            f.write("ADD_APPS = ")
            json.dump(input, f)
        os.mkdir("{}/apps/{}".format(base, name))
        os.system("python3 -m django startapp {} {}/apps/{}".format(name, base, name))
        with open("{}/apps/{}/urls.py".format(name, base, name), "a+") as f:
            f.write("from django.urls import path\n\nurlpatterns = [\n\n]\n")
        with open("{}/apps/{}/forms.py".format(name, base, name), "a+") as f:
            f.write("from django import forms\n\n")
        self.stdout.write("{} added !".format(name))
