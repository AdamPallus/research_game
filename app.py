from flask import Flask, render_template, request, jsonify

import markdown2
from utils import get_email_for_topic, get_description


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def application_form():
    original_proposal = "write an email!"
    if request.method == 'POST':
        original_proposal = request.form.get('researchTopic', 'sorry we lost your original proposal')
    return render_template('application_form.html', original_proposal=original_proposal)

@app.route('/submit_application', methods = ['POST'])
def response_page():
    blank_message= {
        "from": "",
        "to": "",
        "subject": "",
        "body": "Still waiting for a response..."}
    research_topic = request.form['researchTopic']
    return render_template('response_page.html', 
                           original_proposal=research_topic,
                            outcome="pending",
                            email_message=blank_message)

@app.route('/get_response', methods=['POST'])
def submit_application():
    # Here you can process the form data if needed
    # For now, it simply redirects to the response page
    print('triggering response')
    research_topic = request.form.get('researchTopic', 'Unknown research on how mice eat cheese even though they cannot make it')
    print(research_topic)
    print('anything?')
    email_json = get_email_for_topic(research_topic)
    print(email_json)
    outcome = email_json['outcome']
    email_message = email_json['email']
    print("$$$ EMAIL MESSAGE $$$$")
    print(email_message)
    email_message['body'] = markdown2.markdown(email_message['body'])
    return jsonify(outcome=outcome, email_message=email_message)


@app.route('/description', methods=['POST'])
def description_page():
    # Render the initial page with a placeholder
    original_proposal = request.form.get('researchTopic', 'Unknown research on how mice eat cheese even though they cannot make it')
    return render_template('dystopia.html', 
                           original_proposal=original_proposal,
                           description='Years later...')

@app.route('/get_description', methods=['POST'])
def get_description_api():
    original_proposal = request.form.get('researchTopic', 'Unknown research on how mice eat cheese even though they cannot make it')
    print('getting description...')
    print(original_proposal)
    description = get_description(original_proposal)
    print(description)
    description = markdown2.markdown(description)
    return description


@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)
