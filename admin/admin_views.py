from flask import Blueprint , render_template

admin_views = Blueprint("admin_views" , __name__, static_folder="static" ,
                                                template_folder="templates" ,
                                                static_url_path='admin_views')


@admin_views.route("/")
def admin_index():
    return render_template("admin_index.html")