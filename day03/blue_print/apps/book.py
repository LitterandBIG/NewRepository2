from flask import Blueprint

book_bp = Blueprint('book', __name__, url_prefix='/book')


@book_bp.route("/list/")
def profile():
    return '书籍列表'


@book_bp.route("/detail/")
def detail():
    return '书籍详情'