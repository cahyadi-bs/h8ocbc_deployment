import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True # this cause SQLAlchemy to echo SQL statements. Set this to False for production environments.
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dsfhljkiewizdw:e2a3e4140c2d74ebbaac01330dc93ad50a871af83e4be12c8c87aaa273de7b5c@ec2-52-204-72-14.compute-1.amazonaws.com:5432/d3hl3tcl1l3k7f'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)