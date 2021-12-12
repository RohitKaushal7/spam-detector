#importing libraries
import random
import nltk
import pandas as pd
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# FUNCTIONS -------------------------------------

#preprocessing function
def preprocess(document, stem=True):
    'changes document to lower case, removes stopwords and lemmatizes/stems the remainder of the sentence'

    # change sentence to lower case
    document = document.lower()

    # tokenize into words
    words = word_tokenize(document)

    # remove stop words
    words = [word for word in words if word not in stopwords.words("english")]

    if stem:
        words = [stemmer.stem(word) for word in words]
    else:
        words = [wordnet_lemmatizer.lemmatize(word, pos='v') for word in words]

    # join words to make sentence
    document = " ".join(words)

    return document

###creating a single list of all words in the entire dataset for feature list creation
def get_words_in_messages(messages):
    all_words = []
    for (message, label) in messages:
      all_words.extend(message)
    return all_words

#creating a final feature list using an intuitive FreqDist, to eliminate all the duplicate words
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features
 
 #creating a feature map
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
    

# MAIN ----------------------------------------

#using PorterStemmer for stemming data and wordnet_lemmatizer for lemmatization
stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

# load data
spam = pd.read_csv("dataset.csv", usecols = [0, 1], engine = 'python')
#spam.head() - to print first five rows of our dataset

#Converting the read dataset in to a list of tuples which is a list (message, label)
data_set = []
for index,row in spam.iterrows():
    data_set.append((row['message'], row['label']))


#Performing the preprocessing steps on all messages
messages_set = []
for (message, label) in data_set:
    words_filtered = [text.lower() for text in preprocess(message, stem=False).split() if len(text) >= 3]
    messages_set.append((words_filtered, label)) 
    

# creating the word features for the entire dataset
word_features = get_word_features(get_words_in_messages(messages_set))

#creating slicing index at 80% threshold which means 80% train set and 20% test set
sliceIndex = int((len(messages_set)*.8))

#shuffle the pack to create a random and unbiased split of the dataset
random.shuffle(messages_set)

#make train and test set
train_messages, test_messages = messages_set[:sliceIndex], messages_set[sliceIndex:]


#creating the feature map of train and test data
training_set = nltk.classify.apply_features(extract_features, train_messages)
testing_set = nltk.classify.apply_features(extract_features, test_messages)

#Training the classifier with NaiveBayes algorithm
spamClassifier = nltk.NaiveBayesClassifier.train(training_set)

#storing the classifier on disk for later usage
f = open('nb_spam_classifier.pickle', 'wb')
pickle.dump(spamClassifier,f)
f.close()
