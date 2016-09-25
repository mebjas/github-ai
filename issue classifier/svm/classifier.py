from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
import json
import os

categories = ['enhancement', 'bug', 'question', 'help wanted', 'wontfix', 'duplicate', 'invalid']
indices = {}

data = []
labels = []
CV = CountVectorizer()
TFIDF = TfidfTransformer()
clf = None

# init indices with values for faster processing
for i, c in zip(range(0, len(categories)), categories):
    indices[c] = i

def accuracy(datasetFileName, CV, TFIDF, clf):
    data = []
    labels = []
    with open(datasetFileName, encoding="utf8") as _d:
        _d = _d.read()
        _d = json.loads(_d)
        print ("Len of data set %d" % len(_d))
        for d in _d:
            data.append(d['issue'])
            labels.append(indices[d['label']])

        XNC = CV.transform(data)
        XNT = TFIDF.transform(XNC)
        predicted = clf.predict(XNT)
        total = len(data)
        correct = 0
        for l, _l in zip(labels, predicted):
            if l == _l:
                correct = correct + 1
        
        print(" Correct = %d, Total = %d" % (correct, total))
        print(" Accuracy = %f%%" % ((correct / total) * 100))


with open(os.path.dirname(os.path.abspath(__file__)) +'/../data/dataset.json', encoding="utf8") as _d:
    _d = _d.read()
    _d = json.loads(_d)
    print ("Len of data %d" % len(_d))
    for d in _d:
        data.append(d['issue'])
        labels.append(indices[d['label']])

    XTC = CV.fit_transform(data)
    XTT = TFIDF.fit_transform(XTC)

    # clf = MultinomialNB().fit(XTT, labels)
    clf = svm.SVC()
    clf.fit(XTT, labels)  
    accuracy('../data/testset.json', CV, TFIDF, clf)
    print(" testing with trained data ")
    accuracy('../data/dataset.json', CV, TFIDF, clf)
        
def classify(issue):
    XNC = CV.transform([issue])
    XNT = TFIDF.transform(XNC)
    predicted = clf.predict(XNT)
    return categories[predicted[0]]