import boto3

comprehend = boto3.client('comprehend')

text = """By the turnstile beckons a damsel fair
The face of Melinda 'neath blackened hair
No joy would flicker in her eyes
Brooding sadness came to a rise"""

sentiment = comprehend.detect_sentiment(Text=text, LanguageCode='en')

print(f"Text sentiment: {sentiment['Sentiment']}")