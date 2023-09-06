# WeatherBot

This [Rasa](http://rasa.com)-based bot answers questions about temperature, cloudiness, and wind 
speed and gives predictions about minimum and maximum daily temperature and 
cloudiness. The style of the answers is polite, factual, and neutral.

## Version
1.0

## Files and folder structure, where to find what?

in **WeatherBot/**
- **actions/actions.py** contains subclasses of the Rasa SDK Action class (Custom Actions)
- **actions/DOCKERFILE** contains commands/instructions to use the Docker platform to generate a Action-Server container automatically
- **actions/requirements.txt** contains a list of items to be installed by pip, when using pip install
- **actions/weather.py** contains a class that retrieves weather data from google.com 
- **data/nlu.yml** contains the training data based on examples of defined intents 
- **data/rules.yml** contains the set of rules (intent-action assignment) for dialog management and its policies
- **data/stories.yml** contains training stories for the the policies (dialog management)
- **evaluation_120220237/\*** contains nlu & policies test results
- **models/** contains archived trained model (based on config_2.yml)
- **tests/test_stories.yml** contains end-to-end (E2E) test stories for (dialog management) validation
- **config_1.yml** contains the model configuration without language model usage. **ALTERNATIVE**
- **config_2.yml** contains the model configuration with language model usage. **USED IN FINAL SOLUTION**
- **credentials.yml** contains the WebSocketIO credentials 
- **docker-compose.yml** contains the configuration to run docker containers (Action and Rasa Server).
- **DOCKERFILE**  contains commands/instructions to use the Docker platform to generate a Rasa-Server container automatically
- **domain.yml** contains the domain description (weather) for this assistant
- **endpoints.yml** contains the webhook configuration for the custom actions
- **endpoints_docker.yml** contains the webhook configuration (custom actions) for docker compose
- **requirements.txt** contains a list of items to be installed by pip, when using pip install

in **WeatherBotUI/**
- **WeatherBotUI.html** contains the User Interface (UI) to WeatherBot

## How to install WeatherBot? 

The following steps are necessary for the installation of the 
[Python](https://www.python.org/downloads/) runtime environment for WeatherBot:

### Prerequisites
Option 1: Python installed in Version >=3.9 x64 (tested with 3.9.16, pip 22.3.1 and 3.9.0, pip 20.2.3) and packages python3-pip, python3-venv 
OR
Option 2: Installed Docker (Tested on Windows 10 Pro (19045.2486): Docker version 20.10.22, build 3a2c30b, Docker Compose version v2.15.1;
                            Tested on Ubuntu 18.04.05 LTS: Docker version 20.10.23, build 7155243, docker-compose version 1.29.2, build unknown)

### Option 1         

Change to *WeatherBot/*

Create a (empty) virtual enviroemnt (i.e. venv)
#### Windows Powershell (tested on Windows 10 Pro (19045.2486))
```
python -m venv venv
```

#### Linux bash (tested on Ubuntu 18.04.05 LTS)
```
python3 -m venv venv
```

Activate the virtual enviroment (venv)
#### Windows Powershell
```
.\venv\Scripts\activate
```
#### Linux bash 
```
source ./venv/bin/activate
```

Install the list of items needed by WeatherBot into the virtual enviroment (venv)

#### Windows Powershell 
```
pip install -r requirements.txt
```

#### Linux bash 
```
pip3 install -r requirements.txt
```

## How to use WeatherBot?

### Windows (Powershell)

Change to or open *WeatherBot/* 

if not yet activated, activate the virtual environment (venv) with
```
.\venv\Scripts\activate
```

To run a Rasa server and Rasa action server (SDK), run (in two diff. terminals)
```
rasa run actions
rasa run -m  models --enable-api --cors "*"
```

To chat with WeatherBot open follwing file in your browser (tested on Microsoft Edge Version 109.0.1518.55)

Open folder *WeatherBotUI/*
```
double-click on WeatherBotUI.html
```

### Linux (bash)
Change to or open *WeatherBot/* 

if not yet activated, activate the virtual environment (venv) with
```
source ./venv/bin/activate
```

To run a Rasa server and Rasa action server (SDK), run
```
rasa run actions &
rasa run -m  models --enable-api --cors "*"
```

To chat with WeatherBot open follwing file in your browser (tested on Microsoft Edge Version 109.0.1518.55)

Open folder *WeatherBotUI/*
```
double-click on WeatherBotUI.html
```

## How to (re-)train WeatherBot? (optional)

This step is only to be executed if parameters (parameter-tuning) or training data change!

### Windows and Linux (Powershell, bash)

Change to or open *WeatherBot/* 

if not yet activated, activate the virtual environment (venv).

To train a model, run
```
rasa train -c .\config_1.yml
```
or 
```
rasa train -c .\config_2.yml
```

## How to evaluate WeatherBot (optional)

This step is only to be executed if parameters or training data change and you want to (re-)evaluate your model(s)!

### Windows and Linux (Powershell, bash)

Change to or open *WeatherBot/* 

To cross-validate NLU pipelines, run
```
rasa test nlu -c .\config_1.yml .\config_2.yml --cross-validation
```

To evaluate your core model (dialog management, policies), train your models first via
```
rasa train core --config .\config_1.yml .\config_2.yml
```
to evaluate, run
```
rasa test core -s .\tests\test_stories.yml --evaluate-model-director -m .\models\
```

## Option 2    

Run docker (compose), full bootstrap (pip requirements, core training)
```
docker-compose up --build
```

To chat with WeatherBot open follwing file in your browser (tested on Microsoft Edge Version 109.0.1518.55)
```
double-click on WeatherBotUI.html
```

## Miscellaneous
A system-dependent server start-up time must be observed. A first communication with WheaterBot via *Hi* 
should show when he is ready to answer further questions. Also relaod the page if the widget is not showing up.

Rase SDK Action Server ready when:
```
2023-02-02 17:14:33 INFO     rasa_sdk.endpoint  - Action endpoint is up and running on http://0.0.0.0:5055
```

Rasa Server ready when:
```
2023-02-02 17:15:56 INFO     root  - Rasa server is up and running.`
```

For more information about the individual commands, please check out 
[documentation](http://rasa.com/docs/rasa/command-line-interface).



