FROM tensorflow/tensorflow:2.1.0-py3
MAINTAINER atsushimiyamoto <atsushiflee@icloud.com>

COPY . /flask

# set the working directory
WORKDIR /flask

# copy all file to workdir
RUN pip install -r requirements.txt


EXPOSE 5000

# run app.py 
CMD ["python", "app.py"]



