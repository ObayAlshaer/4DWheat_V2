import sys
from os import path
sys.path.insert(0, path.abspath(path.dirname(__file__)))
sys.path.append('/var/www/html/4DWheat_reno/ccd')
from ccd import app as application

