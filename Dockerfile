# Use an official Python runtime as a parent image
# FROM arm32v7/python:3.6-slim
# https://hub.docker.com/r/resin/raspberrypi3-python/tags/
#
# run the following command to build a rpi image
# docker run --rm --privileged multiarch/qemu-user-static:register --reset
 
FROM xmayeur/rpi-python:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
ENV NAME HomeCtrl

# Run app.py when the container launches
ENTRYPOINT ["python", "HomeCtrl.py"]


