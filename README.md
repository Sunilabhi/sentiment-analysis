Sentiment Analysis Streamlit App


Overview
This project is a sentiment analysis application built with Streamlit. It allows users to enter a comment and receive a sentiment prediction (e.g., positive, negative, or neutral). The application uses a pre-trained machine learning model to make predictions based on text input.



Features
User-friendly interface for entering text comments.
Predicts the sentiment of the input comment.
Displays the predicted sentiment.
Installation
Clone the repository:


git clone https://github.com/yourusername/sentiment-analysis-streamlit.git
cd sentiment-analysis-streamlit
Create and activate a virtual environment:


python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:


pip install -r requirements.txt

Usage

Ensure you have the model and vectorizer files:

sentiment_model.pkl

vectorizer.pkl

Run the Streamlit app:


streamlit run app.py
Interact with the app:

Open your browser to the URL provided by Streamlit.

Enter a comment in the text area.

Click the "Submit" button to see the predicted sentiment.

Project Structure

graphql

sentiment-analysis-streamlit/

├── data/
│   └── sentiment_model.pkl         # Pre-trained sentiment analysis model
│   └── vectorizer.pkl              # TfidfVectorizer for text transformation
├── app.py                          # Main Streamlit application script
├── requirements.txt                # Python dependencies
├── README.md                       # Project README file
└── .gitignore                      # Git ignore file


Model Training

The model used in this project is trained separately. It uses a TfidfVectorizer for text feature extraction and a LogisticRegression classifier for sentiment prediction. Below is a brief outline of the training process:

Preprocess the text data.

Transform the text data using TfidfVectorizer.

Train the model using LogisticRegression.

Save the model and vectorizer using pickle.

Contributing

Contributions are welcome! Please follow these steps to contribute:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make your changes.

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-branch).

Create a new Pull Request.

