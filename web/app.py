from flask import Flask, render_template
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.config import Config
from database.models import db, Property

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    properties = Property.query.order_by(Property.created_at.desc()).limit(10).all()
    return render_template('index.html', properties=properties)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
