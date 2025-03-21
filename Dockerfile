FROM python:3.11

WORKDIR /code/crud_api_fast/

COPY src pyproject.toml README.md /code/crud_api_fast/

RUN python -m pip install .

ENTRYPOINT [ "python", "-m", "crud_api_fast", "--port", "8000" ]