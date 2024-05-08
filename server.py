from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "Earn all the gold!!"

def random_gold(num1, num2):
    gold = random.randint(num1, num2)
    return gold

@app.route('/')
def home():
    max_gold = 150
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template('index.html', max_gold = max_gold)

@app.route('/process_money', methods=['POST'])
def process_money():
    print("recieved")
    if request.form['money'] == 'farm':
        gold_found = random_gold(10,20)
        session['gold'] += gold_found
        color = 'success'
    elif request.form['money'] == 'cave':
        gold_found = random_gold(5,10)
        session['gold'] += gold_found
        color = 'success'
    elif request.form['money'] == 'house':
        gold_found = random_gold(2,5)
        session['gold'] += gold_found
        color = 'success'
    else:
        gold_found = random_gold(-50,50)
        session['gold'] += gold_found
        if gold_found < 0:
            color = 'danger'
        else: color = 'success'
    session['activity'].insert(0,[f'Earned {gold_found} gold from the {request.form["money"]} - {datetime.now().strftime("%Y/%m/%d %I:%M %p")}', color])
    print(session['gold'])
    return redirect('/')































if __name__=="__main__":
    app.run(debug=True)