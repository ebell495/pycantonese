FROM python:3.10-bullseye
RUN pip3 install atheris

COPY . /pycantonese
WORKDIR /pycantonese
RUN python3 -m pip install . && chmod +x fuzz/fuzz.py