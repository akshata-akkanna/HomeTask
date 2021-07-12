# this is an official Python runtime, used as the parent image
FROM python:3.6.5-slim

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
COPY . /app

# execute everyone's favorite pip command, pip install -r

RUN pip3 install -r requirements.txt

RUN pip3 install pyarrow==0.9.0

# unblock port 5001 for the Flask app to run on
EXPOSE 5000

# execute the Flask app
CMD python3 task.py
