#-------------------------------------NLP(ANALYSATION OF WORDS)------------------------------------------------------
#-------------------------CLEANING PART OF THE WORDS----------------------
#string to remove other symbols
import string
from collections import Counter
import matplotlib.pyplot as plt 
# linking read file----- encoding so that other text can be placed from net -----
text= open('read.txt',encoding='utf-8').read()
print(text)
# Coverting letters to lower case--
lower_case=text.lower()
print(lower_case)
cleaned_text= lower_case.translate(str.maketrans ('','',string.punctuation))
print(cleaned_text)

#-------------------------Tokenization(breaking sentence into list)and Stop Words--------------------
tokenized_words= cleaned_text.split()
print(tokenized_words)

#---------------------------------stopwords(doesnt add meaning to sentences)-------------------------
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
Final_words=[]
#Removing stop words
for word in tokenized_words:
    if word not in stop_words:
        Final_words.append(word)
        
print(Final_words)

#----------------------------NLP EMOTION ALGORITHM------------------------------------------------------
 #--- 1st linking the emotion.ext file-----
emotion_list=[]
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
#-------------------------COunting Emotion-------------------------------
        if word in Final_words:
            emotion_list.append(emotion)
print(emotion_list)

#--------Counter to count how many emotions-----------
w=Counter(emotion_list)
print(w)

#--------------Plotting the graph of Emotions------------
fig, ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()