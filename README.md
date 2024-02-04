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

<img src="resources/architecture.png" alt="alt text" title="Architecture" width="720" height="700">

## Project Preparation Steps

1. **Create a Google Cloud Project**:
   - Start by creating a new project in Google Cloud if you haven't already.

2. **Update Project Names**:
   - In the project files, update the project name in the following locations:
     - `/cloud_functions/scraper/main.py` (Line 7)
     - `/app/main.py` (Line 12)
     - `main.tf` (Line 4)
   - Optionally, you can also modify the region in `main.tf` (Line 5) if needed.

3. **Create Service Account**:
   - In your Google Cloud project, create a service account and generate credentials.
   - Save the credentials as `credentials.json` and place them in your project directory.

4. **Compress Cloud Function Files**:
   - Compress all files in the `/cloud_functions/scraper` directory into a zip file named `scraper.zip`.

5. **Provision Cloud Infrastructure**:
   - From the project directory, execute the following commands to create the cloud infrastructure using Terraform:
     1. `terraform init`
     2. `terraform plan`
     3. `terraform apply`

6. **Install Python Dependencies**:
   - After creating the infrastructure, navigate to the `/app` directory and execute the following command to install Python dependencies:
     - `pip install -r requirements.txt`

7. **Run Flask Application**:
   - To start the Flask application, run the following command from the `/app` directory:
     - `python main.py`

With these steps completed, your project should be set up and ready for execution. Ensure that you've followed each step carefully to ensure the proper functioning of the application.

## Sample results

<img src="resources/sample_results.PNG" alt="alt text" title="Sample results" width="700" height="400">

