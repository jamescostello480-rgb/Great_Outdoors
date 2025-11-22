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
    # Add a small list of related information to show in the subsection
    related_items = [
        {'title': 'Climb the Mountain', 'url': 'mountain.html'},
        {'title': 'Wander the Forest', 'url': 'forest.html'},
        {'title': 'See the Falls', 'url': 'falls.html'},
        {'title': 'Ride the Ferry', 'url': 'ferry.html'},          # added
        {'title': 'Walk Around the Lake', 'url': 'lake.html'},
        {'title': 'Read in the Park', 'url': 'park.html'},         # added
    ]
    return render_template('index.html', users=users, related_items=related_items)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

if __name__ == '__main__':
    app.run(debug=True)

