FROM python:3


# Set the working directory to /ripo_tweet_flask
WORKDIR /ripo_tweet_flask

# Copy the current directory contents into the container 
COPY . /ripo_tweet_flask
ADD RF_tweet_clas.py /
ADD app.py /

RUN apt-get update
RUN apt install -y python3-pip
RUN pip3 install virtualenv

RUN virtualenv venv 
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt
RUN apt-get -y install git-core

CMD python3 RF_tweet_clas.py;python3 app.py

