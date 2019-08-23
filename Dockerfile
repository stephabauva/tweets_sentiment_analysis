FROM ubuntu:latest


# Set the working directory to /ripo_tweet_flask
WORKDIR /ripo_tweet_flask

# Copy the current directory contents into the container at /app
COPY . /ripo_tweet_flask
RUN apt-get update
RUN apt install -y python3-pip
RUN pip3 install virtualenv

RUN virtualenv venv 
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt
RUN apt-get -y install git-core

ENTRYPOINT ["python3"]
CMD ["RF_tweet_clas.py"]
CMD ["app.py"]