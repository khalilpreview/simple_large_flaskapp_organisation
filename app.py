from flask import Flask , render_template , redirect , url_for , request 

from home.home_views import home_views
from dashboard.dashboard_views import dashboard_views
from admin.admin_views import admin_views


# Flask app initialisation
app = Flask(__name__)


app.config.from_pyfile('config.py')

# Calling blueprints 
app.register_blueprint(admin_views , url_prefix="/admin")
app.register_blueprint(dashboard_views , url_prefix="/dashboard")
app.register_blueprint(home_views , url_prefix="/home")




@app.route('/')
def home():
    return 'Welcome Home from app.py'




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
