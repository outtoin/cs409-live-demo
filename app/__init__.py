from flask import Flask

app = Flask(__name__)

# Setup the app with the config.py file
app.config.from_object('app.config')

# Setup the logger
from app.logger_setup import logger

# Setup the debug toolbar
from flask_debugtoolbar import DebugToolbarExtension
app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
toolbar = DebugToolbarExtension(app)

# Import the views
from app.views import main