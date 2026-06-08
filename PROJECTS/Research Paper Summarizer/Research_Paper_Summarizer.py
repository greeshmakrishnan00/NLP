import PyPDF2
import nltk
import yake
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict

# -------------------------------
# NLTK DOWNLOADS
# -------------------------------
nltk.download('punkt')
nltk.download('stopwords')

# -------------------------------
# PDF TEXT EXTRACTION
# -------------------------------

pdf_path = input("Enter PDF file path: ")

text = ""

try:
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

except Exception as e:
    print("Error reading PDF:", e)
    exit()

print("\nPDF Loaded Successfully!")
print("Total Pages:", total_pages)

# -------------------------------
# TEXT PROCESSING
# -------------------------------

sentences = sent_tokenize(text)
words = word_tokenize(text)

print("\nDOCUMENT STATISTICS")
print("---------------------")
print("Total Words:", len(words))
print("Total Sentences:", len(sentences))

# -------------------------------
# KEYWORD EXTRACTION
# -------------------------------

print("\nTOP KEYWORDS")
print("---------------------")

kw_extractor = yake.KeywordExtractor(lan="en", n=2, top=10)
keywords = kw_extractor.extract_keywords(text)

top_keywords = [kw for kw, score in keywords]

for kw in top_keywords:
    print("-", kw)

# -------------------------------
# STOPWORDS & WORD FREQUENCY
# -------------------------------

stop_words = set(stopwords.words("english"))
word_freq = defaultdict(int)

for word in words:
    word = word.lower()
    if word.isalnum() and word not in stop_words:
        word_freq[word] += 1

# -------------------------------
# OVERALL SUMMARY
# -------------------------------

sentence_scores = defaultdict(int)

for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_freq:
            sentence_scores[sentence] += word_freq[word]

overall_summary_sentences = sorted(
    sentence_scores,
    key=sentence_scores.get,
    reverse=True
)[:5]

overall_summary = " ".join(overall_summary_sentences)

print("\nOVERALL SUMMARY")
print("---------------------")
print(overall_summary)

# -------------------------------
# 🔥 TOPIC-BASED SUMMARY (NEW FEATURE)
# -------------------------------
# We group sentences under keywords (simple topic detection)

topic_sentences = defaultdict(list)

for sentence in sentences:
    sent_lower = sentence.lower()

    matched = False
    for kw in top_keywords:
        if kw.lower() in sent_lower:
            topic_sentences[kw].append(sentence)
            matched = True
            break

    if not matched:
        topic_sentences["Other"].append(sentence)

# -------------------------------
# FUNCTION: SUMMARIZE TOPIC
# -------------------------------

def summarize(sent_list):
    temp_scores = defaultdict(int)

    for sent in sent_list:
        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                temp_scores[sent] += word_freq[word]

    top_sents = sorted(temp_scores, key=temp_scores.get, reverse=True)[:3]
    return " ".join(top_sents)

# -------------------------------
# PRINT TOPIC SUMMARIES
# -------------------------------

print("\nTOPIC-WISE SUMMARY")
print("---------------------")

for topic, sent_list in topic_sentences.items():
    summary = summarize(sent_list)

    print(f"\nTopic: {topic}")
    print("-" * (len(topic) + 8))
    print(summary)

# -------------------------------
# RESEARCH INSIGHTS
# -------------------------------

print("\nRESEARCH INSIGHTS")
print("---------------------")

print("1. Total Words:", len(words))
print("2. Total Pages:", total_pages)
print("3. Total Topics Found:", len(topic_sentences))

print("\nTop Keywords:")
for kw in top_keywords[:5]:
    print("-", kw)

print("\nAnalysis Completed Successfully!")


