#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, session
from flask_migrate import Migrate

from models import db, Article, User

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/clear')
def clear_session():
    session['page_views'] = 0
    return {'message': '200: Successfully cleared session data.'}, 200

@app.route('/articles/<int:id>', methods=['GET'])
def index_articles(id):
    article = Article.query.get(id)
    if not article:
        return make_response({'message': 'Article not found'}, 404)
    
        
    session['page_views'] = session.get('page_views', 0)+1

    if session['page_views'] <= 3:
        return make_response(jsonify({
            'author': article.author,
            'title': article.title,
            'content': article.content,
            'preview': article.preview,
            'minutes_to_read': article.minutes_to_read,
            'date': article.date,

        }), 200)
    else:
        return make_response({'message': 'Maximum pageview limit reached'}, 401)



    

@app.route('/articles/<int:id>')
def show_article(id):

    pass

if __name__ == '__main__':
    app.run(port=5555)













# #!/usr/bin/env python3

# from flask import Flask, make_response, jsonify, session
# from flask_migrate import Migrate

# from models import db, Article, User

# app = Flask(__name__)
# app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# migrate = Migrate(app, db)

# db.init_app(app)

# @app.route('/clear')

# def clear_session():
#     session['page_views'] = 0
#     return {'message': '200: Successfully cleared session data.'}, 200

# @app.route('/articles')
# def index_articles():

#     pass

# @app.route('/articles/<int:id>')
# def show_article(id):

#     pass

# if __name__ == '__main__':
#     app.run(port=5555)
