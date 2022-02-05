import os
from app import create_app, db
from flask_migrate import Migrate, migrate
#
# app = create_app(os.getenv('FLASK_CONFIG'))
# migrate = Migrate(app, db)
app = create_app(os.getenv('FLASK_CONFIG'))
with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate=Migrate(app, db, render_as_batch=True)
    else:
         migrate=Migrate(app, db)