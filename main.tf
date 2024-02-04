provider "google" {
  credentials = file("credentials.json")
  project     = "cryptosentiment-413216"
  region      = "europe-west1"
}

resource "google_pubsub_topic" "crypto_news_topic" {
  name = "crypto-news-topic"
}

resource "google_cloud_scheduler_job" "crypto_news_scheduler" {
  name     = "crypto-news-scheduler-every-minute"
  schedule = "*/1 * * * *"

  pubsub_target {
    topic_name = google_pubsub_topic.crypto_news_topic.id
    data       = base64encode("{\"message\": \"Triggered every minute\"}")
  }
}

resource "google_storage_bucket" "function_source" {
  name     = "crypto-news-function-source-${random_id.bucket_suffix.hex}"
  location = "EU"
}

resource "random_id" "bucket_suffix" {
  byte_length = 2
}

resource "google_storage_bucket_object" "function_source_object" {
  name   = "source.zip"
  bucket = google_storage_bucket.function_source.name
  source = "./cloud_functions/scraper/scraper.zip"
}

resource "google_cloudfunctions_function" "crypto_news" {
  name                  = "crypto-news-function"
  description           = "Function for publish Crypto Data"
  runtime               = "python39"
  available_memory_mb   = 128
  source_archive_bucket = google_storage_bucket.function_source.name
  source_archive_object = google_storage_bucket_object.function_source_object.name
  entry_point           = "publish_crypto_news"
  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource   = google_pubsub_topic.crypto_news_topic.id
  }
}
