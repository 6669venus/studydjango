from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings
import time
import os
from subprocess import call

class Command(BaseCommand):
    help = 'Call collectstatic and then sassc'

    def handle(self, *args, **options):
        csspath =  os.path.join(os.path.join(settings.PROJECT_ROOT, 'static'), 'css')
        sasspath =  os.path.join(os.path.join(settings.PROJECT_ROOT, 'static'), 'sass')

        for file in os.listdir(sasspath):
            if file.endswith(".scss"):
                cmd1 = 'sass ' + os.path.join(sasspath, file) + ' > ' + os.path.join(csspath, os.path.splitext(file)[0] + '.css')
                print cmd1
                call(cmd1, shell=True)
                
                cmd2 = 'sass ' + os.path.join(sasspath, file) + ' --style compressed > ' + os.path.join(csspath, os.path.splitext(file)[0] + '.min.css')
                print cmd2
                call(cmd2, shell=True)
                
                # os.remove(os.path.join(sasspath, file))
        # os.rmdir(sasspath)
        
        call_command('collectstatic', verbosity=0, interactive=False)
                
        self.stdout.write(self.style.SUCCESS('Successfully'))
        