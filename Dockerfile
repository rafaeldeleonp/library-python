FROM python:3.7

WORKDIR /library-python

COPY . /library-python

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 3000

CMD [ "python", "run.py" ]