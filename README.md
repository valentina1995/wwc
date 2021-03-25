# Contributing
Note that we have 2 base branches: *master* and *base*
* master: Intended to hold the production code
* base: Intended to be the starting point from which the student clone the repository. It should provide the base things in order to let her/him starts with the course.

# Code Structure
* ml: Is the place from everything related Machine Learning will live. Inside it you can find the analisis_sentiment and chatbot folders. This folder is intended to be independent from the client interface, so other projects can make use of it.
* webapp: Hold a Flask application for a restaurant. It will use the tools from the /ml folder in order to integrate the chatbot with the flaskapp.