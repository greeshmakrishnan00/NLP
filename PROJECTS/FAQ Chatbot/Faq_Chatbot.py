import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# LOAD KNOWLEDGE BASE
# -------------------------------
with open("knowledge.txt", "r", encoding="utf-8") as file:
    data = file.read().lower()

# Split into sentences
sentences = data.split("\n")

# -------------------------------
# VECTORIZE SENTENCES
# -------------------------------
vectorizer = TfidfVectorizer()
sentence_vectors = vectorizer.fit_transform(sentences)

# -------------------------------
# CHATBOT FUNCTION
# -------------------------------
def chatbot(user_input):
    user_vec = vectorizer.transform([user_input.lower()])

    similarity = cosine_similarity(user_vec, sentence_vectors)

    index = np.argmax(similarity)

    if similarity[0][index] < 0.2:
        return "Sorry, I don't know about that."

    return sentences[index]

# -------------------------------
# CHAT LOOP
# -------------------------------
print("🤖 AI Chatbot Ready! Ask anything...\n(Type 'exit' to stop)\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Bye! 👋")
        break

    print("Bot:", chatbot(user))