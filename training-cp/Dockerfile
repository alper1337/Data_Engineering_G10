# python 3.7 full image
FROM python:3.7.7-buster
WORKDIR /usr/src/myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000

ENV MODEL_REPO  /usr/src/myapp/models
ENV TRAIN_DB_API  http://training-db:5000/training-db/fminst

CMD ["python3","app.py"]
