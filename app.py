from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import pickle
import pandas as pd
from pymongo import MongoClient
from bson.int64 import Int64

app = Flask(__name__)
app.secret_key = '4c6a2b6f1a234e6a2f4f25bfbf8a1f1e'

# Load the trained models and feature columns
PKL_PATH = r'model_suggested_data_XG.pkl'
with open(PKL_PATH, 'rb') as f:
    model1, model2, model3, package_mapping, feature_columns = pickle.load(f)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client['SHIGA-2006']
users_collection = db['signup']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = users_collection.find_one({'Name': name, 'Password': password})
        
        if user:
            session['name'] = name  # Store user's name in session
            return redirect(url_for('profile'))
        else:
            flash("Invalid username or password.", "error")
            return render_template('login.html')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        
        # Check if user already exists
        existing_user = users_collection.find_one({'Name': name})
        if existing_user:
            flash("User already exists! Please login.", "error")
            return redirect(url_for('login'))
        
        try:
            # Get all form data
            user_data = {
                'Name': name,
                'Age': int(request.form['age']),
                'Mobile_Number': Int64(int(request.form['phone_no'])),
                'Password': request.form['password'],
                'Occupation': request.form['occupation'],
                'Location': request.form['location'],
                'Daily_Usage_GB': float(request.form['Daily_Usage_GB']),
                'Daily_Usage_MB': float(request.form['Daily_Usage_MB']),
                'Monthly_Usage_GB': float(request.form['Monthly_Usage_GB']),
                'Device_Type': request.form['Device_Type'],
                'Preferred_Network': request.form['Preferred_Network'],
                'SIM_Type': request.form['SIM_Type'],
                'Network_Package': request.form['Network_Package'],
                'Data_Limit_GB': float(request.form['Data_Limit_GB']),
                'Package_Cost': float(request.form['Package_Cost'])
            }
            
            # Insert into MongoDB
            users_collection.insert_one(user_data)
            
            flash("Signed up successfully! Please login.", "success")
            return redirect(url_for('login'))
            
        except ValueError as e:
            flash("Invalid input. Please check your data.", "error")
            return render_template('signup.html')
            
    return render_template('signup.html')

@app.route('/profile')
def profile():
    if 'name' not in session:
        return redirect(url_for('login'))
    
    user = users_collection.find_one({'Name': session['name']})
    if not user:
        session.clear()
        return redirect(url_for('login'))
    
    return render_template('profile.html', user=user)

@app.route('/edit_details', methods=['GET', 'POST'])
def edit_details():
    if 'name' not in session:
        return redirect(url_for('login'))
    
    user = users_collection.find_one({'Name': session['name']})
    
    if request.method == 'POST':
        try:
            updated_data = {
                'Daily_Usage_GB': float(request.form['Daily_Usage_GB']),
                'Daily_Usage_MB': float(request.form['Daily_Usage_MB']),
                'Monthly_Usage_GB': float(request.form['Monthly_Usage_GB']),
                'Device_Type': request.form['Device_Type'],
                'Preferred_Network': request.form['Preferred_Network'],
                'SIM_Type': request.form['SIM_Type'],
                'Network_Package': request.form['Network_Package'],
                'Data_Limit_GB': float(request.form['Data_Limit_GB']),
                'Package_Cost': float(request.form['Package_Cost'])
            }
            
            users_collection.update_one(
                {'Name': session['name']},
                {'$set': updated_data}
            )
            
            flash('Details updated successfully!', 'success')
            return redirect(url_for('profile'))
            
        except ValueError:
            flash('Invalid input. Please check your data.', 'error')
            return render_template('edit_details.html', user=user)
    
    return render_template('edit_details.html', user=user)

@app.route('/user_details', methods=['GET', 'POST'])
def user_details():
    if 'name' not in session:
        return redirect(url_for('home'))
    
    name = session['name']

    if request.method == 'POST':
        daily_usage_gb = request.form['Daily_Usage_GB']
        daily_usage_mb = request.form['Daily_Usage_MB']
        monthly_usage_gb = request.form['Monthly_Usage_GB']
        device_type = request.form['Device_Type']
        preferred_network = request.form['Preferred_Network']
        sim_type = request.form['SIM_Type']
        network_package = request.form['Network_Package']
        data_limit_gb = request.form['Data_Limit_GB']
        package_cost = request.form['Package_Cost']
        
        # Update top-level fields with network details
        users_collection.update_one(
            {"Name": name},
            {
                "$set": {
                    'Daily_Usage_GB': float(daily_usage_gb),
                    'Daily_Usage_MB': float(daily_usage_mb),
                    'Monthly_Usage_GB': float(monthly_usage_gb),
                    'Device_Type': device_type,
                    'Preferred_Network': preferred_network,
                    'SIM_Type': sim_type,
                    'Network_Package': network_package,
                    'Data_Limit_GB': float(data_limit_gb),
                    'Package_Cost': float(package_cost)
                }
            }
        )
        
        user = users_collection.find_one({"Name": name})
        return render_template('display_details.html', name=name, details=user)
    return render_template('details.html')

@app.route('/suggest_plan', methods=['POST'])
def suggest_plan():
    if 'name' not in session:
        return redirect(url_for('login'))
    
    name = request.form['name']
    user = users_collection.find_one({"Name": name})
    
    # Your existing suggestion logic here
    user_input = {
        'Daily_Usage_GB': user['Daily_Usage_GB'],
        'Daily_Usage_MB': user['Daily_Usage_MB'],
        'Monthly_Usage_GB': user['Monthly_Usage_GB'],
        'Data_Limit_GB': user['Data_Limit_GB'],
        'Package_Cost': user['Package_Cost']
    }
    
    input_df = pd.DataFrame([user_input])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    suggested_data_limit = model1.predict(input_df)[0]
    suggested_package_idx = int(model2.predict(input_df)[0])
    suggested_package = package_mapping[suggested_package_idx]
    suggested_cost = model3.predict(input_df)[0]

    suggested_data_limit_display = "Unlimited" if suggested_data_limit > 2.5 else f"{suggested_data_limit:.2f} GB"

    return render_template('suggested_plan.html',
                         name=name,
                         initial=name[0],
                         data_limit=suggested_data_limit_display,
                         package=suggested_package,
                         cost=f"₹{suggested_cost:.2f}")

@app.route('/submit-complaint', methods=['POST'])
def submit_complaint():
    data = request.get_json()
    print(f"Received complaint: {data}")
    return jsonify({'message': 'Complaint received successfully!'})

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ... (rest of your existing routes remain the same)

if __name__ == '__main__':
    app.run(debug=True)