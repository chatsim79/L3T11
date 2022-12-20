FROM pypy:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
CMD python -u compulsory_task.py
