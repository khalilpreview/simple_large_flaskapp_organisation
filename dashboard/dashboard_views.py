from flask import Blueprint , render_template

dashboard_views = Blueprint("dashboard_views" , __name__ , static_folder="static" ,
                                                           template_folder="templates" ,
                                                           static_url_path='dashboard_views')



@dashboard_views.route("/")
def dashboard_index():
    return render_template("dashboard_index.html")