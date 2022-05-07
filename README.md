# Predict Scores

![Build Status](https://github.com/gotoeveryone/predict-scores/workflows/Build/badge.svg)

## Requirements

- Docker

## Setup

```console
$ cp .env.example .env # Please edit the value.
```

## Run

```console
$ docker compose up
$
$ # generate model
$ docker compose api pipenv run generate_model
```
