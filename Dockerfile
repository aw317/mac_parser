FROM python:3
WORKDIR /usr/src/rest_parsers
COPY . .
RUN pip install -r requirements.txt
CMD ["mac_parser.py"]
ENTRYPOINT ["python3"]