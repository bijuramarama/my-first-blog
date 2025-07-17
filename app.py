from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
import os
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017/"))
db = client.film_crew
crew_collection = db.crew
trips_collection = db.trips
locations_collection = db.locations
shooting_plans_collection = db.shooting_plans
footage_collection = db.footage
studio_workflow_collection = db.studio_workflow

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

@app.route('/trips')
def trips():
    all_trips = trips_collection.find()
    return render_template('trips.html', trips=all_trips)

@app.route('/add_trip', methods=['POST'])
def add_trip():
    trip = {
        'name': request.form.get('name'),
        'destination': request.form.get('destination'),
        'status': 'upcoming'
    }
    trips_collection.insert_one(trip)
    return redirect(url_for('trips'))

@app.route('/edit_trip/<trip_id>', methods=['GET', 'POST'])
def edit_trip(trip_id):
    if request.method == 'POST':
        trips_collection.update_one(
            {'_id': ObjectId(trip_id)},
            {'$set': {
                'name': request.form.get('name'),
                'destination': request.form.get('destination'),
                'status': request.form.get('status')
            }}
        )
        return redirect(url_for('trips'))
    else:
        trip = trips_collection.find_one({'_id': ObjectId(trip_id)})
        return render_template('edit_trip.html', trip=trip)

@app.route('/delete_trip/<trip_id>')
def delete_trip(trip_id):
    trips_collection.delete_one({'_id': ObjectId(trip_id)})
    return redirect(url_for('trips'))

@app.route('/locations')
def locations():
    all_locations = locations_collection.find()
    return render_template('locations.html', locations=all_locations)

@app.route('/add_location', methods=['POST'])
def add_location():
    location = {
        'name': request.form.get('name'),
        'country': request.form.get('country'),
        'visa_requirements': request.form.get('visa_requirements'),
        'permits': request.form.get('permits')
    }
    locations_collection.insert_one(location)
    return redirect(url_for('locations'))

@app.route('/edit_location/<location_id>', methods=['GET', 'POST'])
def edit_location(location_id):
    if request.method == 'POST':
        locations_collection.update_one(
            {'_id': ObjectId(location_id)},
            {'$set': {
                'name': request.form.get('name'),
                'country': request.form.get('country'),
                'visa_requirements': request.form.get('visa_requirements'),
                'permits': request.form.get('permits')
            }}
        )
        return redirect(url_for('locations'))
    else:
        location = locations_collection.find_one({'_id': ObjectId(location_id)})
        return render_template('edit_location.html', location=location)

@app.route('/delete_location/<location_id>')
def delete_location(location_id):
    locations_collection.delete_one({'_id': ObjectId(location_id)})
    return redirect(url_for('locations'))

@app.route('/shooting_plans')
def shooting_plans():
    all_shooting_plans = shooting_plans_collection.find()
    return render_template('shooting_plans.html', shooting_plans=all_shooting_plans)

@app.route('/add_shooting_plan', methods=['POST'])
def add_shooting_plan():
    shooting_plan = {
        'name': request.form.get('name'),
        'schedule': request.form.get('schedule'),
        'team_assignments': request.form.get('team_assignments'),
        'equipment_logistics': request.form.get('equipment_logistics')
    }
    shooting_plans_collection.insert_one(shooting_plan)
    return redirect(url_for('shooting_plans'))

@app.route('/edit_shooting_plan/<shooting_plan_id>', methods=['GET', 'POST'])
def edit_shooting_plan(shooting_plan_id):
    if request.method == 'POST':
        shooting_plans_collection.update_one(
            {'_id': ObjectId(shooting_plan_id)},
            {'$set': {
                'name': request.form.get('name'),
                'schedule': request.form.get('schedule'),
                'team_assignments': request.form.get('team_assignments'),
                'equipment_logistics': request.form.get('equipment_logistics')
            }}
        )
        return redirect(url_for('shooting_plans'))
    else:
        shooting_plan = shooting_plans_collection.find_one({'_id': ObjectId(shooting_plan_id)})
        return render_template('edit_shooting_plan.html', shooting_plan=shooting_plan)

@app.route('/delete_shooting_plan/<shooting_plan_id>')
def delete_shooting_plan(shooting_plan_id):
    shooting_plans_collection.delete_one({'_id': ObjectId(shooting_plan_id)})
    return redirect(url_for('shooting_plans'))

@app.route('/footage')
def footage():
    all_footage = footage_collection.find()
    return render_template('footage.html', footage=all_footage)

@app.route('/add_footage', methods=['POST'])
def add_footage():
    new_footage = {
        'name': request.form.get('name'),
        'location': request.form.get('location'),
        'camera': request.form.get('camera'),
        'team': request.form.get('team')
    }
    footage_collection.insert_one(new_footage)
    return redirect(url_for('footage'))

@app.route('/edit_footage/<footage_id>', methods=['GET', 'POST'])
def edit_footage(footage_id):
    if request.method == 'POST':
        footage_collection.update_one(
            {'_id': ObjectId(footage_id)},
            {'$set': {
                'name': request.form.get('name'),
                'location': request.form.get('location'),
                'camera': request.form.get('camera'),
                'team': request.form.get('team')
            }}
        )
        return redirect(url_for('footage'))
    else:
        footage_item = footage_collection.find_one({'_id': ObjectId(footage_id)})
        return render_template('edit_footage.html', footage_item=footage_item)

@app.route('/delete_footage/<footage_id>')
def delete_footage(footage_id):
    footage_collection.delete_one({'_id': ObjectId(footage_id)})
    return redirect(url_for('footage'))

@app.route('/studio_workflow')
def studio_workflow():
    all_studio_workflow = studio_workflow_collection.find()
    return render_template('studio_workflow.html', studio_workflow=all_studio_workflow)

@app.route('/add_studio_workflow', methods=['POST'])
def add_studio_workflow():
    new_studio_workflow = {
        'footage_name': request.form.get('footage_name'),
        'status': 'arrived',
        'editing_progress': 'not_started',
        'approval': 'pending'
    }
    studio_workflow_collection.insert_one(new_studio_workflow)
    return redirect(url_for('studio_workflow'))

@app.route('/edit_studio_workflow/<studio_workflow_id>', methods=['GET', 'POST'])
def edit_studio_workflow(studio_workflow_id):
    if request.method == 'POST':
        studio_workflow_collection.update_one(
            {'_id': ObjectId(studio_workflow_id)},
            {'$set': {
                'footage_name': request.form.get('footage_name'),
                'status': request.form.get('status'),
                'editing_progress': request.form.get('editing_progress'),
                'approval': request.form.get('approval')
            }}
        )
        return redirect(url_for('studio_workflow'))
    else:
        studio_workflow_item = studio_workflow_collection.find_one({'_id': ObjectId(studio_workflow_id)})
        return render_template('edit_studio_workflow.html', studio_workflow_item=studio_workflow_item)

@app.route('/delete_studio_workflow/<studio_workflow_id>')
def delete_studio_workflow(studio_workflow_id):
    studio_workflow_collection.delete_one({'_id': ObjectId(studio_workflow_id)})
    return redirect(url_for('studio_workflow'))

if __name__ == '__main__':
    app.run(debug=True)
