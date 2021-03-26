# Predict Scores

![Build Status](https://github.com/gotoeveryone/predict-scores/workflows/Build/badge.svg)

## Requirements

- Python 3.6
- pipenv

## Setup

```console
$ pipenv install # When get dev-packages too, add `-d` option.
$ cp .env.example .env # Please edit the value.
```

## Run

```console
$ # batch
$ pipenv run generate_model
$ # api
$ pipenv run api
```
