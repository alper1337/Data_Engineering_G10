# python 3.7 full image as the base image
FROM python:3.7.7-buster
# define workdir
WORKDIR /usr/src/myapp
# load requirements into workdir
COPY requirements.txt .
# Install all libs in requirements
RUN pip install --no-cache-dir -r requirements.txt
# Copy all files in local database component into docker workdir of container
COPY . .
# Open port
EXPOSE 5000
# Add label for more infos
LABEL training.db.api="0.0.1-beta"
# Run app.py script to start database 
CMD ["python3","app.py"]
