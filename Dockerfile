FROM python:3.6.9
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY . /app
# ENTRYPOINT ["streamlit", "run"] For local runs
ENTRYPOINT ["streamlit", "run", "--server.port $PORT"] # For deployment to Heroku
CMD ["app/app.py"]
