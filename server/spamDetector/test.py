import pickle

f1 = open("spamDetector/nb_spam_classifier.pickle", "rb")
spamClassifier = pickle.load(f1)
f2 = open('spamDetector/word_features.pickle', 'rb')
wf = pickle.load(f2)


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in wf:
        features['contains(%s)' % word] = (word in document_words)
    return features

def test_for_spam(input):
    outp = spamClassifier.classify(extract_features(input.split()))
    return outp
