FROM python:alpine
MAINTAINER omkar yadav 
#RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip install flask
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["app.py"]
