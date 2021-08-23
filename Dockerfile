FROM python:3.9-slim-buster
MAINTAINER chardrew <chardrew@outlook.com.au>


RUN apt-get update && apt-get upgrade

# check python environment
RUN python --version

# set working directory for containers
ARG CHORD_PROGRESSION_GENERATOR="chord-progression-generator"
ARG BASE_PATH="/usr/src/chord_progression_generator"

RUN mkdir $BASE_PATH $BASE_PATH/data
WORKDIR $BASE_PATH

# Install python dependencies
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt

# Copy files from the project’s root to the working directory
COPY $CHORD_PROGRESSION_GENERATOR/src/ $BASE_PATH/src/
COPY $CHORD_PROGRESSION_GENERATOR/model/ $BASE_PATH/model/
COPY data/lookups/ $BASE_PATH/data/lookups/

ENTRYPOINT bash