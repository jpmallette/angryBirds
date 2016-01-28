
Python script #2: TF-IDF
Exécution du TF-IDF:

for i in range(len(country)):
    print("Top words in document {}".format(i + 1))
    # read in pandas the file 
    # subset for all the row of one country s[s > 0]
    # delete the column with the country
    
    document = # should be all the comments of one country
    scores = {word: tfidf(word, document, merge_file) for word in document.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for word, score in sorted_words[:3]:
    print("Word: {}, TF-IDF: {}".format(word, round(score, 2)))

Function TF-IDF calculation

# tf idf calculation
# thanks to:  http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/
from __future__ import division, unicode_literals
import math
from textblob import TextBlob as tb

# document
document_list = clean_train_reviews

def tf(word, document):
   return document.words.count(word) / len(document.words)

def n_document_containing_word(word, document_list):
   return sum(1 for document in document_list if word in document)

def idf(word, document_list):
   return math.log(len(document_list) / (1 + n_document_containing_word(word, document_list)))

def tfidf(word, document, document_list):
   return tf(word, document) * idf(word,document_list)

for i in range(len(document_list)):
   print("Top words in document {}".format(i + 1))
   document = tb(document_list[i])
   print(document)
   scores = {word: tfidf(word, document, document_list) for word in document.words}
   sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
   for word, score in sorted_words[:3]:
       print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))

