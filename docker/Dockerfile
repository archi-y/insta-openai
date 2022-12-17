#Latest Python
FROM python:3.9-slim
#Get and install Requirements
COPY requirements.txt requirements.txt

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:s$PATH"

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

ADD instagpt_docker.py /
#Files generated with login.py
ADD login.json /
ADD openai.key / 
#OpenAI prompt context txt
ADD context_base.txt /

CMD [ "python", "./instagpt_docker.py" ]
