# base image
FROM python:3.7.7-buster
# working directory
WORKDIR /usr/src/myapp
# Copy dependency versions
COPY requirements.txt .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy all files in training-db local host directory to /usr/src/myapp in Docker container
COPY . .
# Expose the port that our app runs in
EXPOSE 5000
# Enviroment Variables
ENV MODEL_REPO  /usr/src/myapp/models
# Run our App
CMD ["python3","app.py"]
