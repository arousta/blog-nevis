FROM mcr.microsoft.com/devcontainers/python:0-3.11

COPY requirements.txt .
RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm requirements.txt

CMD ["sleep", "infinity"]
