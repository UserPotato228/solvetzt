# import blueprint
import os.path
from app.index import bp
from flask import render_template, session, redirect, request
from app.extensions import db
from app.models.tasks import Tasks
from datetime import datetime

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        room = request.form.get("room", None) or None
        desc = request.form.get("desc", "Подойдите пожалуйста") or "Подойдите пожалуйста"
        time = datetime.now().strftime("%m/%d/%Y %H:%M")
        task = Tasks(room=room, desc=desc, time=time)
        db.session.add(task)
        db.session.commit()
        return "<script>alert(\"Ожидайте!\"); location.href=\"/\"</script>"