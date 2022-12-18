                                
'''                                                                             
CONFIG                                                                          
'''

#SQLALCHEMY_DATABASE_URI = 'mysql://root:Xyh@1999@localhost/ccd?charset=utf8'
SQLALCHEMY_DATABASE_URI = 'mysql://root:!QAZ2wsx@127.0.0.1/ccd?charset=utf8'   # need to change to web address in the production mode
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False

HOST = 'localhost'  # need to change to the web address in the production mode
PORT = 5000 # 5000 if dev mode; 7000 if prod mode                               

DEBUG = False # True if dev mode; False if prod mode                            
ENABLE_CACHE = True # False if dev mode; True if prod mode                      

SECRET_KEY = 'this-is-the-secret-key'





