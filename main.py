import string
from collections import Counter
import plotly.express as px
text = open("read.txt", encoding="utf-8").read()
lower_text = text.lower()

cleaned_text = lower_text.translate(str.maketrans("", "", string.punctuation))

tokenized = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []

for word in tokenized:
    if word not in stop_words:
        final_words.append(word)



emotion_list = []
with open("emotions.txt","r") as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word,emotion = clear_line.split(":")
        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)
fig = px.bar(
    x=w.keys(),
    y=w.values(),
    labels={"x":"Emotions","y":"Frequency"},
    title="Emotion Frequency in Text",
    color=w.keys(),
)
fig.show()