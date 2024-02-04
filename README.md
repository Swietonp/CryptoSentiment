# CryptoSentiment
This project provides a comprehensive solution for collecting, analyzing, and visualizing sentiment data from cryptocurrency news using various Google Cloud services and technologies. To set up and run this project, you will need a Google Cloud Account, Terraform, Python, and pip.

# Project Objectives
The primary objectives of this project are as follows:

Create Google Cloud Pub/Sub Topic: This project creates a Google Cloud Pub/Sub Topic to act as a message broker for cryptocurrency news updates.

Create Google Cloud Pub/Sub Subscription: A corresponding Google Cloud Pub/Sub Subscription is created to subscribe to the cryptocurrency news updates published to the topic.

Create Google Cloud Scheduler Job: A Google Cloud Scheduler job is set up to trigger every minute, ensuring regular updates and data collection.

Create Bucket for Storing News Data: A Google Cloud Storage Bucket is established to store the news articles collected from various RSS feeds.

Deploy Scraping Code as a Cloud Function: The code responsible for scraping news articles is deployed as a Google Cloud Function, ensuring scalable and reliable data collection.

Web Application for Sentiment Analysis: An interactive web application is developed to retrieve data from the Pub/Sub Subscription, connect to the Google Natural Language Processing API to assess the sentiment of news articles on a scale of 1 to 10, and create a table to display the results.

Prerequisites
