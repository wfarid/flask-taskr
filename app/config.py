'''
 Flask application configuration settings
'''
import os

base_directory = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'
WTF_CSRF_ENABLED = True
DATABASE_PATH = os.path.join(base_directory,DATABASE)