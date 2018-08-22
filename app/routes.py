from app import app,db,links
from flask import request

@app.route('/')
@app.before_request
def index():
    path = request.path
    x = path[1:]
    print(x)

    lk = links.query.order_by(links.url).all()

    op = list()
    for i in lk:
        op.append(i.url)

    # print(op)
    if x in op:
        return "False"
    else:
        return "True"
