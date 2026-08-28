"""Flask application for detecting emotions in user-provided text."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emt_detector():
    """Analyze text and return the detected emotion and emotion scores."""

    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_homepage():
    """Render homepage for client."""

    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000)
