import os
from app import app
from flask.cli import FlaskGroup

cli = FlaskGroup(app)

if __name__ == '__main__':
    try:
        import sys        
        sys.exit(cli())
    except Exception as e:
        import traceback
        traceback.print_exc()