

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib

app = Flask(__name__)

# Load the dataset
dataset = pd.read_csv("Odi_bating.csv")

# Load the trained model
model = joblib.load('model.pkl')

def get_recommendation(player_name, opposition_team):
    # Filter the dataset to get player performances against the specified opposition team
    player_performance = dataset[(dataset['Player Name'] == player_name) & (dataset['Opposition Team'] == opposition_team)]
    
    if player_performance.empty:
        return "No data available for the specified player and opposition team", ""
    
    
    recommended_player = dataset[dataset['Opposition Team'] == opposition_team].iloc[0]['Player Name']
    reason = "Highest average runs against the specified opposition team"
    
    return recommended_player, reason


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Retrieve form data
        player_name = request.form['player_name']
        opposition_team = request.form['opposition_team']
        
        # Perform prediction
        recommended_player, reason = get_recommendation(player_name, opposition_team)
        
        # Redirect to result page with prediction
        return redirect(url_for('result', player=recommended_player, reason=reason))
    return render_template('form.html')



@app.route('/result')
def result():
    player = request.args.get('player')
    reason = request.args.get('reason')
    return render_template('result.html', player=player, reason=reason)




