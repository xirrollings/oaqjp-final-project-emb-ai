"""
Flask web application for emotion detection.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Handle emotion detection requests.

    Accepts JSON input with a 'text' field, passes it to the emotion_detector
    function, and returns a formatted response string. If the dominant emotion
    is None, returns an error message.
    """
    data = request.json
    text_to_analyze = data.get("text", "")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
