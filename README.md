# Final Project

An AI-based web application that analyzes customer feedback and identifies the emotions expressed in the provided text.

## Overview

This project was developed for an e-commerce company that wants to perform analytics on customer feedback for its signature products.

The application uses an **Emotion Detection system** to process customer feedback in text format and determine the emotions expressed in the text. It identifies scores for five emotions:

- **Anger**
- **Disgust**
- **Fear**
- **Joy**
- **Sadness**

The system also determines the **dominant emotion** based on the highest emotion score.

## Features

- Analyze customer feedback provided as text.
- Detect five different emotions:
  - Anger
  - Disgust
  - Fear
  - Joy
  - Sadness
- Determine the dominant emotion.
- Provide emotion scores for the analyzed text.
- Expose the emotion detection functionality through a Flask web application.
- Handle invalid requests and unsuccessful responses from the emotion detection service.
- Includes automated unit tests using Python's `unittest` framework.

## Technologies Used

- **Python**
- **Flask** — Web application framework
- **Requests** — HTTP requests to the emotion detection service
- **unittest** — Automated testing
- **JavaScript** — Client-side interaction with the Flask API
- **Pylint** — Code quality and style checking

## Project Structure

```text
.
├── EmotionDetection/
│   └── emotion_detection.py
├── server.py
├── test_emotion_detection.py
└── README.md
```

## How It Works

The application follows this general flow:

```text
Customer Feedback
       │
       ▼
Web Application
       │
       ▼
Emotion Detection Service
       │
       ▼
Emotion Scores
       │
       ├── Anger
       ├── Disgust
       ├── Fear
       ├── Joy
       └── Sadness
       │
       ▼
Dominant Emotion
       │
       ▼
Response to User
```
