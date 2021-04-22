# docker image build --file ./webapp/Dockerfile -t webapp:0.1.0 .
FROM python:3.7
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "./webapp/run.py"]