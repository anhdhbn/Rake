from flask import Flask, request, jsonify
import pickle
import rake
app = Flask(__name__)
# Load the model
# model = pickle.load(open('model.pkl','rb'))

@app.route('/',methods=['GET'])
def index():
    return 'OK!'

@app.route('/api/execute',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    text = data['text']
    lang = data['lang']
    min_char_length = int(data['min_char_length'])
    max_words_length = int(data['max_words_length'])
    min_keyword_frequency = int(data['min_keyword_frequency'])

    stoppath = "data/stoplists/{0}.txt".format(lang)
    rake_object = rake.Rake(stoppath, min_char_length, max_words_length, min_keyword_frequency)
    keywords = rake_object.run(text)

    # print(data)
    # Make prediction using model loaded from disk as per the data.
    # prediction = model.predict([[np.array(data['exp'])]])
    # # Take the first value of prediction
    # output = prediction[0]
    # return jsonify(output)
    return jsonify(keywords)
if __name__ == '__main__':
    app.run(port=5000, debug=True)