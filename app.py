import os
from flask import Flask
from config import config
from model import db

# flask
# add initial process
class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path, static_folder=None)

        # init configration
        config['root_path'] = root_path

        # read  db configration
        self.config.from_pyfile('config/db_config.py')
        # config DB
        db.init_app(self)
        
# flask object
# specify the path of template
app = Application(__name__, template_folder=os.getcwd() + '/view/template', root_path=os.getcwd())


   
