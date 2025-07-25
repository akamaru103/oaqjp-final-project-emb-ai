''' 
Initiates the Emotion Detection application
to be executed over the Flask channel and 
deployed on localhost:5000.
'''

# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request

# Import the emotion detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' 
    Receives the text from the HTML interface and 
    runs emotion detection on it using the emotion_detector() function. 
    The output returned shows a list of emotions detected along with their score,
    and a summary of the dominant emotion detected in the text supplied.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Make a list of the emotions minus the dominant one at the end
    emotions = list(response.items())[:-1]
    # get the value of the dominant emotion separately
    dominant = response['dominant_emotion']

    # Check if the dominant emotion is None, indicating an error or invalid input
    if dominant is None:
        return "Invalid input! Try again."

    # Start the result string
    result = "For the given statement, the system response is "

    # Unpack the list of emotions, add all but last to the result,
    # then add the last to the result with the word 'and' before it
    *initial, last = emotions
    for key, value in initial:
        result += f"'{key}': {value}, "
    result += f"and '{last[0]}': {last[1]}. "

    # Finally, add the dominant emotion to the result string with its value in bold
    result += f"The dominant emotion is <strong>{dominant}</strong>."

    # Return a formatted string with the list of emotions and dominant emotion
    return result


@app.route("/")
def render_index_page():
    '''
    Renders the HTML index page of the web app
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
