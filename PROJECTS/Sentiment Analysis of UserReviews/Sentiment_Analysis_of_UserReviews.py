from textblob import TextBlob
from datetime import datetime

print("=" * 50)
print("      NLP SENTIMENT ANALYSIS SYSTEM")
print("=" * 50)

review = input("\nEnter your review: ")

# Text Analysis
analysis = TextBlob(review)

polarity = analysis.sentiment.polarity
subjectivity = analysis.sentiment.subjectivity

# Basic Statistics
word_count = len(review.split())
char_count = len(review)

# Sentiment Classification
if polarity > 0:
    sentiment = "Positive 😊"
elif polarity < 0:
    sentiment = "Negative 😞"
else:
    sentiment = "Neutral 😐"

# Sentiment Percentage
sentiment_percentage = abs(polarity) * 100

# Display Results
print("\n========== ANALYSIS REPORT ==========")
print("Review:", review)
print("Word Count:", word_count)
print("Character Count:", char_count)
print("Polarity Score:", round(polarity, 2))
print("Subjectivity Score:", round(subjectivity, 2))
print("Sentiment Strength:", round(sentiment_percentage, 2), "%")
print("Sentiment:", sentiment)

# Save Result to File
with open("sentiment_history.txt", "a", encoding="utf-8") as file:
    file.write(f"\n{'='*50}\n")
    file.write(f"Date: {datetime.now()}\n")
    file.write(f"Review: {review}\n")
    file.write(f"Polarity: {polarity}\n")
    file.write(f"Subjectivity: {subjectivity}\n")
    file.write(f"Sentiment: {sentiment}\n")

print("\nResult saved to sentiment_history.txt")