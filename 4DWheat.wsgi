##!/var/www/html/4Dwheat/venv/bin/python3
import sys
from os import path
sys.path.insert(0, path.abspath(path.dirname(__file__)))
#sys.path.insert(0,"/var/www/html/4DWheat/venv/lib/python3.6/site-packages")
sys.path.append('/var/www/html/4DWheat/ccd')
from ccd import app as application

