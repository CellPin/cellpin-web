FROM tensorflow/tensorflow:latest-gpu

RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN pip3 install tensorflow flask pillow keras numpy image

COPY . .

EXPOSE 80
ENTRYPOINT ["python"]
CMD ["app.py"]