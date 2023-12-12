import os
from flask import Flask
from config import CONFIG
from db import DB

# flask
# add initial process
class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path, static_folder=None)

        # init configration
        CONFIG['root_path'] = root_path

        # read  db configration
        self.config.from_pyfile('config/db_config.py')
        # config DB
        DB.init_app(self)

# flask object
app = Application(__name__, template_folder=os.getcwd() + '/web/template', root_path=os.getcwd())