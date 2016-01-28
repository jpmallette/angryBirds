# import module

import re
import nltk
import nltk.data
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
port = PorterStemmer()
lmtr = WordNetLemmatizer()

# read and modify data
text = open('C:\\Users\\jp\\Desktop\\HEC\\Automne 2015\\Analyse Textuelle\\angry_birds.csv')

# lists
mots_line = list()
lemanized_words_line = list()
result_full = list()

# Patterns
pattern_spacing = re.compile('\\\\n+')
pattern_non_word = re.compile('[^\w\s]+')
stops = set(stopwords.words("english"))

# Lemmatization
for line in text:
    # Nettoyage des lignes
    line = re.sub(pattern_spacing,' ',line)
    line = re.sub(pattern_non_word,' ',line)
    line = line.lower()
    mots_line = line.split()
    meaningful_words = [x for x in mots_line if not x in stops]
    #application de la lemmanization (methode porter), mais ne marche pas avec les verbes.
    for mot in meaningful_words:
        lemanized_words_line.append(lmtr.lemmatize(port.stem(mot),'v'))
    result_full.append(' '.join(lemanized_words_line))
    mots_line.clear()
    lemanized_words_line.clear()
