from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/mountain')
def mountain():
    return render_template('mountain.html')

@app.route('/forest')
def forest():
    return render_template('forest.html')

@app.route('/falls')
def falls():
    return render_template('falls.html')

@app.route('/ferry')
def ferry():
    return render_template('ferry.html')

@app.route('/lake')
def lake():
    return render_template('lake.html')

@app.route('/park')
def park():
    return render_template('park.html')

if __name__ == '__main__':
    app.run(debug=True)

