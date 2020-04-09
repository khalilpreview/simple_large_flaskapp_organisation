# simple_large_flaskapp_organisation

Flask Project (large app organisation using bleuprint) (not for extra_large app)
* This project containe an organisation that help you to build extensible projects.
* Easy to Deploy on Heroku

# Simlpe structure :
====================
* yourapp/
--- __init__.py
--- admin/
------- __init__.py
------- views.py
------- static/
------- templates/
--- home/
------- __init__.py
------- views.py
------- static/
------- templates/
--- control_panel/
------- __init__.py
------- views.py
------- static/
------- templates/
--- __init__.py
--- models.py <p>Model file containe all db classes for flask-saqlalchemy. </p>
--- forms.py <p>Form file containe all form classes for flask-wtf.</p>
--- app.py <p>your flask app run from this file.</p>
--- run_app.py <p>this file let you testing your app live with debug mode=True(don't deploy your project with this file).</p>
--- requirements.txt <p>All pip packages that you need for the project.</p>
--- Procfile <p>That file handel the gunicorn webserver , configration to deploying.</p>



