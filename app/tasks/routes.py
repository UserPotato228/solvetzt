# import blueprint
import json
import os.path
from app.tasks import bp
from flask import render_template, session, redirect, request, make_response, jsonify
from app.extensions import db
from app.models.tasks import Tasks

@bp.route('/tasks')
def tasks():
    items = db.session.query(Tasks).all()
    return render_template("tasks.html", items=items)

@bp.route('/tasks/set_done', methods=["POST"])
def set_done():
    id = json.loads(request.data).get("id" or None) or None

    if not id:
        return make_response("invalid request", 200)

    task = db.session.query(Tasks).filter(Tasks.id==id).one()
    db.session.delete(task)
    db.session.commit()

    return make_response("ok", 200)

@bp.route('/tasks/get_count')
def get_count():
    items = db.session.query(Tasks).all()
    count = len(items)
    return jsonify(count=count)