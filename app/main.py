import os
from google.cloud import pubsub_v1
from google.cloud import language_v1
import json
from datetime import datetime
from flask import Flask, render_template

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '././credentials.json'

client = language_v1.LanguageServiceClient()

project_id = "your_project_id"
subscription_name = "crypto-news-pull-subscription"
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_name)

response = subscriber.pull(
    request={"subscription": subscription_path, "max_messages": 10}
)

messages = []
for received_message in response.received_messages:
    message_data = received_message.message.data.decode("utf-8")
    message_id = received_message.message.message_id
    message_dict = json.loads(message_data)
    timestamp = message_dict["timestamp"]
    formatted_timestamp = datetime.fromisoformat(timestamp).strftime("%Y-%m-%d")
    message_title = message_dict["title"]
    message_info = {"timestamp": formatted_timestamp, "title": message_title}
    messages.append(message_info)

sentiments = []
for idx, message in enumerate(messages, start=1):
    text = message['title']
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={"document": document}).document_sentiment
    sentiment_score = sentiment.score  # Value from -1 (negative) to 1 (positive)
    # Rounding sentiment to one decimal place and scaling to a range from 1 to 10
    scaled_sentiment = round((sentiment_score + 1) * 5, 1)
    sentiments.append({"timestamp": message['timestamp'], "title": message['title'], "sentiment": scaled_sentiment})

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', sentymenty=sentiments)


if __name__ == '__main__':
    app.run(debug=True)
