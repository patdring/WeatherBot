FROM rasa/rasa:3.2.10

WORKDIR '/app'
COPY . /app
COPY requirements.txt requirements.txt
USER root
RUN pip install --verbose -r requirements.txt
COPY ./data /app/data
RUN  rasa train --config config_2.yml
VOLUME /app
VOLUME /app/data
VOLUME /app/models
CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints_docker.yml", "--debug"]

EXPOSE 5005
