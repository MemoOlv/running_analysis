FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    codecov \
    flake8 \
    gpxpy \
    matplotlib \
    mutmut \
    mypy \
    numpy \
    pandas \
    pytest \
    pytest-cov \
    seaborn \
    typer 

RUN pip install --editable .