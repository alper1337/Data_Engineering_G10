import json
import os
import pickle
import sklearn


# make prediction
def predict_for(dataset):
    model_repo = os.environ['MODEL_REPO']
    if os.path.isdir(model_repo):
        file_path = os.path.join(model_repo, "trained_model.sav")            
        with open(file_path, 'rb') as file:
            model = pickle.load(file)
        prediction = model.predict(dataset)
        fmnist_classes = {0:"T-shirt/top", 1: "Trouser", 2: "Pullover", 3: "Dress", 4: "Coat", 5: "Sandal", 
                  6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle boot"}
        prediction = [fmnist_classes[predict] for predict in prediction]
        return json.dumps(prediction, indent=4, sort_keys=False)        # return prediction as json
    else:
        return json.dumps({'message': 'A model cannot be found.'},
                          sort_keys=False, indent=4)
