FROM python:3.9

WORKDIR /code

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:$PATH"

# Install dependences
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false &&\
    poetry install --no-interaction --no-ansi