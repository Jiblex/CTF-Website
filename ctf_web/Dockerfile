FROM ubuntu:latest

# copy current directory into app and make it work directory
COPY . /app
WORKDIR /app

# run update, python, pip, and libmagic-dev needed for python-magic
RUN apt-get update 
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip
RUN apt-get install -y libmagic-dev

# install all python packages
RUN pip install --no-cache-dir -r requirements.txt

# run the website 
CMD ["python3", "run.py"]