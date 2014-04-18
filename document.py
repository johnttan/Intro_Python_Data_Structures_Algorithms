from subprocess import call
import glob
import os
import shutil
from template import template, template2

templatefile = open('docs/index.html', 'w')
templatestring = str(template)
templatestring2 = str(template2)
for file in glob.glob("**/*.py"):
    print('Doccoing {}'.format(file))
    templatestring = templatestring + """<li><a href="{0}.html">{1}</a></li>""".format(os.path.basename(file)[:-3], file)
    os.system('pycco ' + file)
templatestring += templatestring2
print(templatestring)
templatefile.write(templatestring)
srcfile = 'pycco.css'
dest = './docs'
shutil.copy(srcfile, dest)

os.system('docco-central ' + '*.py')