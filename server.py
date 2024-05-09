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
    max_gold = 500
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    if 'count' not in session:
        session['count'] = 0
    return render_template('index.html', max_gold = max_gold)


# without 4 conditionals
@app.route('/process_money', methods=['POST'])
def process_money():
    farming_dict = {
        'farm': [10,20],
        'cave': [5,10],
        'house': [2,5],
        'casino': [-50,50]
    }
    if request.form['money'] in farming_dict:
        gold_found = random_gold(farming_dict[request.form['money']][0], farming_dict[request.form['money']][1])
        if gold_found < 0:
            color = 'danger'
        else:
            color = 'success'
        session['gold'] += gold_found
        session['activity'].insert(0,[f'Earned {gold_found} gold from the {request.form["money"]} - {datetime.now().strftime("%Y/%m/%d %I:%M %p")}', color])
        session['count'] += 1
    return redirect('/')

# with 4 conditionals
# @app.route('/process_money', methods=['POST'])
# def process_money():
#     print("recieved")
#     count = 0
#     if request.form['money'] == 'farm':
#         gold_found = random_gold(10,20)
#         session['gold'] += gold_found
#         session['count'] += 1
#         color = 'success'
#     elif request.form['money'] == 'cave':
#         gold_found = random_gold(5,10)
#         session['gold'] += gold_found
#         session['count'] += 1
#         color = 'success'
#     elif request.form['money'] == 'house':
#         gold_found = random_gold(2,5)
#         session['gold'] += gold_found
#         session['count'] += 1
#         color = 'success'
#     else:
#         gold_found = random_gold(-50,50)
#         session['gold'] += gold_found
#         if gold_found < 0:
#             session['count'] += 1
#             color = 'danger'
#         else:
#             session['count'] += 1
#             color = 'success'

#     session['activity'].insert(0,[f'Earned {gold_found} gold from the {request.form["money"]} - {datetime.now().strftime("%Y/%m/%d %I:%M %p")}', color])
#     print(session['count'])
#     return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)