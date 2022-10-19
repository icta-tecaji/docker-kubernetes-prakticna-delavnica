# Running Multi-container Apps With Docker Compose

## Overview of Docker Compose and installation
Compose is a tool for defining and running multi-container Docker applications in single-engine mode. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. 

> **Compose V2 and the new docker compose command**: The new Compose V2, which supports the `compose` command as part of the Docker CLI, is now available. Compose V2 integrates compose functions into the Docker platform, continuing to support most of the previous `docker-compose` features and flags. You can run Compose V2 by replacing the hyphen (-) with a space, using `docker compose`, instead of `docker-compose`. [Compose command compatibility with docker-compose](https://docs.docker.com/compose/cli-command-compatibility/).

[Compose installation scenarios](https://docs.docker.com/compose/install/):
- (Mac, Win, Linux) Docker Desktop: If you have Desktop installed then you already have the Compose plugin installed.
- Linux systems: To install the Docker CLI’s Compose plugins use one of these methods of installation:
    - Using the [convenience scripts](https://docs.docker.com/engine/install/#server) offered per Linux distro from the Engine install section.
    - Setting up [Docker’s repository](https://docs.docker.com/compose/install/compose-plugin/#install-using-the-repository) and using it to install the compose plugin package.

Use the following command to ckeck that Compose is installed: `docker compose version`

## Compose background
Modern cloud-native apps are made of **multiple smaller services** that interact to form a useful app. We call this pattern **“microservices”**. A simple example might be an app with the following seven services: Web front-end, Ordering, Catalog, Back-end database, Logging, Authentication, Authorization.
- Get all of these working together, and you have a useful application.
- **Deploying and managing lots of small microservices** like these can be hard. this is where Docker Compose comes in to play.
- Instead of gluing each microservice together with scripts and long docker commands, Docker Compose lets you describe an entire app in a **single declarative configuration file**, and deploy it with a single command.
- Once the app is deployed, you can **manage its entire lifecycle** with a simple set of commands. You can even store and manage the configuration file in a **version control system**.

## Running a application with Compose: counter-app

Compose uses YAML files to define multi-service applications. The default name for a Compose YAML file is `docker-compose.yml`. However, you can use the `-f` flag to specify custom filenames.

The following example shows a very simple Compose file that defines a small **Flask app with two microservices** (web-fe and redis). The app is a simple web server that **counts the number of visits to a web page** and stores the value in Redis.

The Compose file can be found here: `cat ~/docker-k8s/08_Running_Multi_container_Apps_With_Docker_Compose/examples/01_counter-app/docker-compose.yml`

> The most current, and recommended [Compose Specification](https://docs.docker.com/compose/compose-file/).

The first thing to note is that the file has 4 top-level keys:
- `version` (DEPRECATED): The version key was **mandatory**, and it’s **always the first line at the root of the file**. this defines the version of the
Compose file format (basically the API). You should normally use the latest version. It’s important to note that the versions key does not define the version of Docker Compose or the Docker Engine. [Compose file versions and upgrading](https://docs.docker.com/compose/compose-file/compose-versioning/). **NEW:** Top-level version property is defined by the specification for backward compatibility but is only informative.
- `services`: The top-level services key is where you define the different application microservices. This example defines two services; a web front-end called web-fe, and an in-memory database called redis. Compose will **deploy each of these services as its own container**. 
- `networks`: The top-level networks key tells Docker to create new networks. By default, Compose will create bridge networks. These are single-host networks that can only connect containers on the same Docker host.
- `volumes`: The top-level volumes key is where you tell Docker to create new volumes.

The example file we’ve listed uses the Compose version 3.8 file format, defines two services, defines a network called counter-net, and defines a volume called redis-data.

Each of these defines a service (container) in the app. It’s important to understand that Compose will deploy each of these as a container, and it will use the name of the keys as part of the container names. The services section has two second-level keys:
- `web-fe`
    - `build: .`: This tells Docker to build a new image using the instructions in the Dockerfile in the current directory (.). The newly built image will be used in a later step to create the container for this service.
    - `command: python app.py` this tells Docker to run a Python app called app.py as the main app in the container. The app.py file must exist in the image, and the image must contain Python. the Dockerfile takes care of both of these requirements. command **overrides the default command declared by the container image** (i.e. by Dockerfile’s CMD).
    > Note: Technically speaking, we don’t need the command: python app.py option. this is because the application’s Dockerfile already defines python app.py as the default app for the image. However, we’re showing it here so you know how it works. You can also use Compose to override CMD instructions set in Dockerfiles.
    - `ports`: Tells Docker to map port 5000 inside the container to port 80 on the host. This means that traffic sent to the Docker host on port 80 will be directed to port 5000 on the container. The app inside the container listens on port 5000.
    - `networks`: Tells Docker which network to attach the service’s container to. The network should already exist, or be defined in the networks top-level key.
- `redis`
    - `image: redis:alpine`: this tells Docker to start a standalone container called redis based on the redis:alpine image. This image will be pulled from Docker Hub.
    - `networks`: The redis container will be attached to the counter-net network.
    - `volumes`: Tells Docker to mount the redis-data volume to /data inside the container. The redis-data volume needs to already exist, or be defined in the volumes top-level key at the bottom of the file.

As both services will be deployed onto the same counter-net network, they **will be able to resolve each other by name**. This is important as the application is configured to communicate with the redis service by name.

Check the files (`cd ~/docker-k8s/08_Running_Multi_container_Apps_With_Docker_Compose/examples/01-counter-app`):
- `app.py`: is the application code (a Python Flask app)
- `requirements.txt`: lists the Python packages required for the app
- `Dockerfile`: describes how to build the image for the web-fe service

Compose will also use the name of the directory (01-counter-app) as the project name.

Let’s use Compose to bring the app up: `sudo docker compose up`. 
- It’ll take a few seconds for the app to come up, and the output can be quite verbose.
- Go to: `http://<IP>`

`docker compose up` is the most common way to bring up a Compose app (we’re calling a multi-container app defined in a Compose file a Compose app). It builds or pulls all required images, creates all required networks and volumes, and starts all required containers. By default, `docker compose up` expects the name of the Compose file to `docker compose.yml.` If your **Compose file has a different name**, you need to specify it with the `-f` flag.

`sudo docker compose down` will stop and delete a running Compose app. It deletes containers and networks, but not volumes and images. It’s important to note that the redis-data volume was not deleted.This is because volumes are intended to be long-term persistent data stores. As such, their lifecycle is entirely decoupled from the applications they serve. If you’d written any data to the volume, that data would still exist.
- `sudo docker volume ls`

It’s also common to use the `-d` flag to bring the app up in the background: `sudo docker compose up -d` (check the number of visits on the webpage). Now that the app is built and running, we can use normal docker commands to view the images, containers, networks, and volumes that Compose created.
- `sudo docker image ls`: We can see that three images were either built or pulled as part of the deployment.
- `sudo docker container ls`: The following container listing shows two running containers.
- `sudo docker network ls`
- `sudo docker volume ls`

Managing an app with Compose:
- `sudo docker compose ps`: Show the current state of the app
- `sudo docker compose top`: List the processes running inside of each service (The PID numbers returned are the PID numbers as seen from the Docker host (not from within the containers).)
- `sudo docker compose stop`: Stop the app without deleting its resource
- `sudo docker compose ps`
- `sudo docker compose restart`: Restart the app
- `sudo docker compose ps`
- `sudo docker compose down -v`: Stop and delete the app and the volumes


