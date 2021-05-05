# Code Structure
* ml: Is the place from everything related Machine Learning will live. Inside it you can find the /chatbot and /nlp folders. This folder (ml) is intended to be independent from the client interface, so other projects can make use of it.
* webapp: Hold a Flask application for a restaurant. It will use the tools from the /ml folder in order to integrate the chatbot with the flaskapp.

# Contributing
Note that we have 2 base branches: *master* and *base*
* master: Intended to hold the production code
* base: Intended to be the starting point from which the student clone the repository. It should provide the base things in order to let her/him starts with the course.

## Running Jupyter Locally
* Docker: https://www.docker.com/get-started
* Docker Compose: https://docs.docker.com/compose/install/
### Prerequisites

In the root of the repository you will find a Dockerfile, this Dockerfile be use by the **docker-compose.yml** file to trigger jupyter. So the only thing you will need to do is to run the next command:

1. ```docker-compose up``` (preferable choice)
or
2. ```docker-compose up -d``` (if you want to run it as a background process)

Then, you will be able to open jupyter by going to ```www.localhost:8888```. But, you better just run the *1st* command as it displays the direct link to the notebooks.

**IMPORTANT**: 
If you want to map the notebooks of the jupyter container to your file system (or in other words, to see and edit the notebooks from your host computer or from inside the container), you should change the volume in the *docker-compose.yaml* file by adding your absolute path to the ```/wwc``` repo in the ```/ml/nlp``` folder

```
...
    volumes:
      - /your/absolute/path/to-wwc-repo/wwc/ml/nlp:/usr/src/wwc/ml/nlp
```
