FROM python:3.8.5-buster
LABEL author="Richard Crouch"
LABEL description="Wunderground API connector daemon"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install joe

# Install Python dependencies
RUN pip3 install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy

# Copy application and files
RUN mkdir /app
COPY app/*.py /app/
WORKDIR /app

# run Python unbuffered so the logs are flushed
CMD ["python3", "-u", "main.py"]
#CMD ["tail", "-f", "/dev/null"]