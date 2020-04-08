from flask import Blueprint , render_template

home_views = Blueprint("home_views" , __name__, static_folder="static" ,
                                                template_folder="templates" ,
                                                static_url_path='home_views')


@home_views.route("/")
def home_index():
    return render_template("home_index.html")