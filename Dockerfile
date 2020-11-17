From alpine:latest

RUN apk add --no-cache py-pip
RUN pip3 install --upgrade pip

COPY ./timeslotAPI /timeslotAPI
WORKDIR /timeslotAPI

RUN pip3 install -r requirements.txt

EXPOSE 5002

WORKDIR /timeslotAPI/timeslotAPI
ENTRYPOINT ["python3"]
CMD ["__init__.py"]