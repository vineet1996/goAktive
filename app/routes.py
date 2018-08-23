from flask import render_template,redirect
from app import app,db,links
from flask import Flask,request, url_for,jsonify



@app.route('/')
@app.route('/urlinfo/1/<path:arg>')
def home(arg):
    lk = links.query.order_by(links.url).all()

    op = list()
    for i in lk:
        op.append(i.url)

    if arg in op:
        return jsonify({'value':arg ,'success':False})
    else:
        return jsonify({'value':arg ,'success':True})

@app.route('/add/<path:arg2>')
def add(arg2):
    lk1 = links.query.order_by(links.url).all()

    op1 = list()
    for i in lk1:
        op1.append(i.url)

    if arg2 in op1:
        return jsonify({'value':arg2+' already present in database','success':False})
    else:
        me =  links(url=arg2)
        db.session.add(me)
        db.session.commit()
        return jsonify({'value':arg2+' added to database','success':True})
