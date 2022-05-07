FROM python:3.6.15-slim as development

ENV APP_ROOT /var/app
WORKDIR ${APP_ROOT}

RUN pip install --upgrade pip && \
  pip install pipenv

COPY Pipfile Pipfile.lock ${APP_ROOT}
RUN pipenv sync

FROM python:3.6.15-slim as production

ENV APP_ROOT /var/app
WORKDIR ${APP_ROOT}

RUN pip install --upgrade pip && \
  pip install pipenv

COPY Pipfile Pipfile.lock ${APP_ROOT}
RUN pipenv sync

COPY . ${APP_ROOT}
