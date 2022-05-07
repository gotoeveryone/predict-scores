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

## Run (Kubernetes at local)

Need next tool if use kubernetes.

- minikube
- kubectl

```console
$ eval $(minikube docker-env)
$ docker buildx build --target production -t gotoeveryone/predict-scores-api:latest -f Dockerfile .
$ minikube start
$ kubectl apply -f manifests
$ kubectl port-forward {pod_name} 5000:5000
```
