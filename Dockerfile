# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.3
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

RUN /bin/sh -c python3 src/manage.py migrate

USER appuser

EXPOSE 8000

CMD [ "python3","src/manage.py", "runserver", "127.0.0.1:8000" ]