# LEARNINGLOG - logging your learning progress

## Table of contents
* [General info](#general-info)
* [Prerequisites](#rerequisites)
* [Technologies](#technologies)
* [Build and run](#build-and-run)

## General info
This project is created for all people who want to improve themselves. 
You can log all learning progress, time and development. 
If you want to do something, just learn and do it.

## Prerequisites
I assume you have installed Docker and it is running.

See the Docker website for installation instructions.

## Technologies
Project is created with:
* Python version: 3.8.10
* Django version: 3.2.9
* Git version: 2.25.1
* Docker version: 20.10.7, build 20.10.7-0ubuntu5~20.04.2

## Build and run
Steps to build a Docker image:

1. Clone this repo
```
$ git clone https://github.com/ewelinajablonska/learninglog.git
```

2. Build the image
```
$ docker build --tag="my_app" .
```

3. Run the image's default command, which should start everything up. (Note that the host will actually be a guest if you are using boot2docker, so you may need to re-forward the port in VirtualBox.)
```
$ docker run my_app
```

4. Once everything has started up, you should be able to access the webapp via http://localhost:8080/ on your host machine.
```
$ open: http://localhost:8080/
```

You can also login to the image and have a look around:
```
$ docker run -i -t my-app /bin/bash
```
