FROM mcr.microsoft.com/devcontainers/python:0-3.11 AS production
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm requirements.txt

CMD ["sleep", "infinity"]


FROM production AS development
ARG PYLINTRC=~/.pylintrc
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt && \
    rm requirements-dev.txt && \
    pylint --generate-rcfile             > PYLINTRC && \
    echo "[MESSAGES CONTROL]"           >> PYLINTRC && \
    echo "disable = "                   >> PYLINTRC && \
    echo "missing-module-docstring"     >> PYLINTRC && \
    echo "missing-class-docstring"      >> PYLINTRC && \
    echo "missing-function-docstring\n" >> PYLINTRC
