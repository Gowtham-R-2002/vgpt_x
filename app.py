from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_input = data['user_input']
    print(user_input)
    
    # Use ChatGPT to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate engine
        prompt=user_input,
        max_tokens=50  # Adjust as needed
    )
    model_response = response.choices[0].text.strip()
    
    return jsonify({'model_response': model_response})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
