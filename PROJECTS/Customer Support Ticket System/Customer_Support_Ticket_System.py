import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Sample Dataset
data = {
    "Ticket": [
        "My internet is not working",
        "Unable to login to my account",
        "Payment deducted twice",
        "Need information about your services",
        "Website is showing an error",
        "Forgot my password",
        "Incorrect bill amount charged",
        "What are your business hours?",
        "App keeps crashing",
        "I want to update my account details"
    ],
    "Category": [
        "Technical Issue",
        "Account Issue",
        "Billing Issue",
        "General Inquiry",
        "Technical Issue",
        "Account Issue",
        "Billing Issue",
        "General Inquiry",
        "Technical Issue",
        "Account Issue"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Labels
X = df["Ticket"]
y = df["Category"]

# NLP + ML Pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# Train Model
model.fit(X, y)

print("=" * 50)
print("CUSTOMER SUPPORT TICKET CLASSIFICATION")
print("=" * 50)

# User Input
ticket = input("\nEnter Customer Ticket: ")

# Predict Category
prediction = model.predict([ticket])

print("\nPredicted Category:", prediction[0])

priority_keywords = {
    "High": ["crash", "error", "failed", "urgent"],
    "Medium": ["slow", "issue", "problem"],
    "Low": ["information", "details", "hours"]
}

ticket_lower = ticket.lower()

priority = "Medium"

for level, words in priority_keywords.items():
    if any(word in ticket_lower for word in words):
        priority = level
        break

print("Priority Level:", priority)