from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hi'


if __name__ == '__main__':
    app.run(debug=True)
# import random
# from flask import Flask, request, redirect, send_from_directory, render_template, make_response, make_response, Response
# import json

# import pymysql
# app = Flask(__name__)

# resp = Response()
# resp.headers['Access-Control-Allow-Origin'] = '*'


# @app.route('/topics', defaults={'topic_id': None}, methods=['GET', 'POST'])
# @app.route('/topics/<topic_id>', methods=['PUT', 'GET', 'DELETE'])
# def topics(topic_id):
#     try:
#         db = pymysql.connect(
#             user='root',
#             passwd='111111',
#             host='127.0.0.1',
#             db='mydb',
#             charset='utf8',
#             autocommit=True
#         )
#         cursor = db.cursor(pymysql.cursors.DictCursor)

#         if request.method == 'GET':
#             if topic_id == None:
#                 sql = "SELECT * FROM topic"
#                 cursor.execute(sql)
#                 topics = cursor.fetchall()
#                 output = []
#                 for topic in topics:
#                     output.append({'id': topic['id'], 'title': topic['title'],
#                                    'created': topic['created'].strftime('%Y-%m-%d %H:%M:%S')})
#                 resp.set_data(json.dumps(output))
#                 return resp
#             else:
#                 sql = "SELECT * FROM topic WHERE id = "+str(topic_id)
#                 cursor.execute(sql)
#                 print('sql', sql)
#                 topic = cursor.fetchone()
#                 output = json.dumps({'id': topic['id'], 'title': topic['title'], 'description': topic['description'],
#                                      'created': topic['created'].strftime('%Y-%m-%d %H:%M:%S')})
#                 resp.set_data(output)
#                 return resp
#         elif request.method == 'POST':
#             form = request.get_json()
#             print('form', form)
#             sql = """
#                 INSERT INTO topic (title, description, created)
#                 VALUES(
#                     '%(title)s',
#                     '%(description)s',
#                     NOW()
#                 )
#                 """ % {'title': form['title'], 'description': form['description']}
#             cursor.execute(sql)
#             output = json.dumps(
#                 {'id': cursor.lastrowid, 'title': form['title'], 'description': form['description']})
#             resp.set_data(output)
#             return resp
#         elif request.method == 'PUT':
#             form = request.get_json()
#             sql = """
#                 UPDATE topic SET
#                     title = '%(title)s',
#                     description = '%(description)s'
#                 WHERE id = '%(topic_id)s'
#                 """ % {'topic_id': topic_id, 'title': form['title'], 'description': form['description']}
#             cursor.execute(sql)
#             output = json.dumps(
#                 {'id': topic_id, 'title': form['title'], 'description': form['description']})
#             resp.set_data(output)
#             return resp
#         elif request.method == 'DELETE':
#             sql = """
#                 DELETE FROM topic WHERE id = %(id)s
#                 """ % {'id': topic_id}
#             cursor.execute(sql)
#             output = json.dumps({'id': topic_id})
#             resp.set_data(output)
#             return resp
#     finally:
#         cursor.close()
#         db.close()


# @app.route('/static/<path:path>')
# def static_files(path):
#     return send_from_directory('static', path)


# @app.route('/', defaults={'path': None})
# @app.route('/<path>')
# def index(path):
#     resp.set_data(render_template('index.html'))
#     return resp


# if __name__ == '__main__':
# 	app.run(debug=True)
