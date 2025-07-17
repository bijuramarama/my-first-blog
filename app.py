from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
import os
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017/"))
db = client.film_crew
crew_collection = db.crew

@app.route('/')
def index():
    crew = crew_collection.find()
    return render_template('index.html', crew=crew)

@app.route('/add', methods=['POST'])
def add_member():
    member = {
        'name': request.form.get('name'),
        'role': request.form.get('role'),
        'country': request.form.get('country')
    }
    crew_collection.insert_one(member)
    return redirect(url_for('index'))

@app.route('/edit/<member_id>', methods=['GET', 'POST'])
def edit_member(member_id):
    if request.method == 'POST':
        crew_collection.update_one(
            {'_id': ObjectId(member_id)},
            {'$set': {
                'name': request.form.get('name'),
                'role': request.form.get('role'),
                'country': request.form.get('country')
            }}
        )
        return redirect(url_for('index'))
    else:
        member = crew_collection.find_one({'_id': ObjectId(member_id)})
        return render_template('edit.html', member=member)

@app.route('/delete/<member_id>')
def delete_member(member_id):
    crew_collection.delete_one({'_id': ObjectId(member_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
