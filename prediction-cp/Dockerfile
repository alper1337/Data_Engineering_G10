# base image
FROM python:3.7.7-buster
# working directory
WORKDIR /usr/src/myapp
# Copy dependency versions
COPY requirements.txt .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5002
# Env variable to mount volume to
ENV MODEL_REPO  /usr/src/myapp/models
# Run our App
CMD ["python3","app.py"]
