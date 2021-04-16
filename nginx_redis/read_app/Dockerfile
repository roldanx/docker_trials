FROM python:alpine
RUN pip3 install flask
RUN pip3 install redis
CMD ["python3","app.py"]
COPY python-redis-read.py /app.py
