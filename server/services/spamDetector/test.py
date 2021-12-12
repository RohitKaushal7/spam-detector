import pickle
f1 = open("nb_spam_classifier.pickle", "rb")
spamClassifier = pickle.load(f1)
f2 = open('word_features.pickle', 'rb')
wf = pickle.load(f2)

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in wf:
        features['contains(%s)' % word] = (word in document_words)
    return features

inp = open("input.txt", "r")
text = inp.read()
outp = spamClassifier.classify(extract_features(text.split()))
out = open("output.txt", "w")
out.write(outp)
out.close()
