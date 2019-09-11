from flask import Blueprint

movie_bp = Blueprint('movie', __name__, url_prefix='/movie')


@movie_bp.route("/list/")
def profile():
    return '电影列表'


@movie_bp.route("/detail/")
def detail():
    return '电影详情'