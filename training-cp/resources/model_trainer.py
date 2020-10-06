# simple svm classification on fminst data set available at openml
import json
import os
from sklearn import svm
from sklearn.metrics import accuracy_score
import pandas
import pickle

def train(dataset):
    # split into input (X) and output (Y) variables and store tiny portion for evalution
    X,Y = dataset[dataset.columns[:-1]], dataset[dataset.columns[-1]]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, stratify=Y, 
                                       train_size=0.9, random_state=1)
    # define model
    model = svm.SVC(C=1, gamma=1e-7, kernel='linear')
    # Fit the model
    model.fit(X_train, Y_train)
    # evaluate the model
    Y_pred = model.predict(X_test)
    text_out = {
        "accuracy:": accuracy_score(Y_test, Y_pred)
    }
    # Save model in location of env variable
    model_repo = os.environ['MODEL_REPO']
    # check if directory exists
    if os.path.isdir(model_repo):
        with open(os.path.join(model_repo, 'trained_model.sav'), 'wb') as file:
            pickle.dump(model, file)
    else:
        os.mkdir(model_repo)
        with open(os.path.join(model_repo, 'trained_model.sav'), 'wb') as file:
            pickle.dump(model, file)

    print("Saved the model to disk in path {path}".format(path=model_repo))
    return json.dumps(text_out, sort_keys=False, indent=4)
