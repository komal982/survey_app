from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def survey():
    return render_template('index.html', thank_you=False)

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    question1_answer = request.form['question1']
    question2_answer = request.form['question2']

    # Process or store the answers (e.g., save to database)
    print("Answer to Question 1:", question1_answer)
    print("Answer to Question 2:", question2_answer)

    # Show thank you message after submission
    return render_template('index.html', thank_you=True)

if __name__ == '__main__':
    app.run(debug=True)
