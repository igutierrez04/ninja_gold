from flask import Flask, render_template, request, redirect, session
import random

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
    return render_template('index.html', max_gold = max_gold)

@app.route('/process_money', methods=['POST'])
def process_money():
    print("recieved")
    return redirect('index.html')































if __name__=="__main__":
    app.run(debug=True)