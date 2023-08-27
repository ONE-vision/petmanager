FROM python:3.9
EXPOSE 8000
ADD . /petmanager
WORKDIR /petmanager
RUN pip install -r requirements.txt
RUN pip install -v .
ENTRYPOINT ["/usr/local/bin/server"]
