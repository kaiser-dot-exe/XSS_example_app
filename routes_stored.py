from flask import Blueprint, request, render_template, redirect, url_for
from markupsafe import escape

bp = Blueprint("stored", __name__)

comments = []

# XSS (zafiyetli)
@bp.route("/comment", methods=["GET", "POST"])
def comment_vulnerable():
    global comments
    if request.method == "POST":
        text = request.form.get("text", "")
        comments.append(text)  # Filtre yok
        return redirect(url_for("stored.comment_vulnerable"))

    return render_template("comment.html", comments=comments)

# XSS (güvenli)
@bp.route("/safe_comment", methods=["GET", "POST"])
def comment_safe():
    global comments
    if request.method == "POST":
        text = request.form.get("text", "")
        comments.append(text)
        return redirect(url_for("stored.comment_safe"))

    escaped_comments = [escape(c) for c in comments]
    return render_template("safe_comment.html", comments=escaped_comments)
