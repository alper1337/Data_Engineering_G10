import json
import os
import pickle
import sklearn


# make prediction
def predict_for(dataset):
    model_repo = os.environ['MODEL_REPO']
    if model_repo:
        file_path = os.path.join(model_repo, "model.sav")            
        model = pickle.load(open(file_path, 'rb'))       # load weights
        val_set2 = dataset.copy()
        result = model.predict(dataset)              # make prediction
        y_classes = result.argmax(axis=-1)
        val_set2['class'] = y_classes.tolist()
        dic = val_set2.to_dict(orient='records')
        return json.dumps(dic, indent=4, sort_keys=False)        # return prediction as json
    else:
        return json.dumps({'message': 'A model cannot be found.'},
                          sort_keys=False, indent=4)
