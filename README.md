FER-pytorch web application
===========

The application is built using [Streamlit](https://streamlit.io/) framework. It has been deployed to Heroku service
using Docker and is available via the link:
https://ferpytorch-webapp.herokuapp.com/.

# How to run the app
The app can be run locally with the command:

` streamlit run app/app.py`

# Docker
Firstly, uncomment the line with entrypoint for local runs in Dockerfile. After that

1. Build the image:

`docker build -t fer-webapp:latest -f Dockerfile .`

2. Run the app:

`docker run -p 8501:8501 fer-webapp:latest`
