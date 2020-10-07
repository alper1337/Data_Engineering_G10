# Data_Engineering_G10


gcloud compute firewall-rules create flask-port-2 --allow tcp:5001
gcloud compute firewall-rules create flask-port-3 --allow tcp:5002

sudo docker build -t training-db .
sudo docker run -p 5000:5000 -d --name=dbAPI training-db

sudo docker build -t training-cp .
sudo docker run -p  5001:5000 -v /home/models:/usr/src/myapp/models -e TRAIN_DB_API='http://dbAPI:5000/training-db/fmnist' -d --name=trainAPI training-cp

sudo docker network create mynetwork
sudo docker network connect mynetwork dbAPI
sudo docker network connect mynetwork trainAPI

sudo docker build -t prediction-cp .
sudo docker run -p  5002:5000 -v /home/models:/usr/src/myapp/models -d --name=predictionAPI prediction-cp
sudo docker network connect mynetwork predictionAPI
