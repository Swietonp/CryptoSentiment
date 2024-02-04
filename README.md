# CryptoSentiment
This project provides a comprehensive solution for collecting, analyzing, and visualizing sentiment data from cryptocurrency news using various Google Cloud services and technologies. To set up and run this project, you will need a Google Cloud Account, Terraform, Python, and pip.

## Project Objectives

The primary objectives of this project are as follows:

1. **Create Google Cloud Pub/Sub Topic**: This project creates a Google Cloud Pub/Sub Topic to act as a message broker for cryptocurrency news updates.

2. **Create Google Cloud Pub/Sub Subscription**: A corresponding Google Cloud Pub/Sub Subscription is created to subscribe to the cryptocurrency news updates published to the topic.

3. **Create Google Cloud Scheduler Job**: A Google Cloud Scheduler job is set up to trigger every minute, ensuring regular updates and data collection.

4. **Create Bucket for Storing News Data**: A Google Cloud Storage Bucket is established to store the news articles collected from various RSS feeds.

5. **Deploy Scraping Code as a Cloud Function**: The code responsible for scraping news articles is deployed as a Google Cloud Function, ensuring scalable and reliable data collection.

6. **Web Application with Flask for Message Reception**: Develop a web application using Flask that receives messages from the Pub/Sub Subscription.

7. **Web Application with Flask for Cloud Natural Language API Integration**: Extend the Flask web application to send messages to the Google Cloud Natural Language API and receive sentiment analysis data.

8. **Web Application with Flask for HTML Table Generation**: Enhance the Flask web application to create an HTML table displaying the sentiment analysis results.

## Project Architecture

