import os
from app import create_app, db
from flask_migrate import Migrate
#
app = create_app(os.getenv('FLASK_CONFIG'))
migrate = Migrate(app, db)
