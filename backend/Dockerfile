<<<<<<< HEAD
FROM ubuntu:20.04

COPY . .

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN apt-get update && apt install -y python3.9 python3-pip
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000
=======
FROM ubuntu:20.04

COPY . .

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN apt-get update && apt install -y python3.9 python3-pip
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000
>>>>>>> 174f6ff28139d3a094fb431ff4392023432a03a1
CMD ["python3", "app.py"]