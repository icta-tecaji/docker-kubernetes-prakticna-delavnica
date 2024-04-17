# Running Multi-container Apps With Docker Compose

## Overview of Docker Compose and installation
Compose is a tool for defining and running **multi-container Docker applications in single-engine mode**. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. 

> **Compose V2 and the new docker compose command**: Effective July 2023, Compose V1 stopped receiving updates and is no longer in new Docker Desktop releases. Compose V2 has replaced it and is now integrated into all current Docker Desktop versions. You can run Compose V2 by replacing the hyphen (-) with a space, using `docker compose`, instead of `docker-compose`. [Compose command compatibility with docker-compose](https://docs.docker.com/compose/cli-command-compatibility/).

![compose-v1-vs-v2](./images/v1-versus-v2.png)

[Compose installation scenarios](https://docs.docker.com/compose/install/):
- (Mac, Win, Linux) Docker Desktop: If you have Desktop installed then you already have the Compose plugin installed.
- Linux systems: To install the Docker CLI’s Compose plugins use one of these methods of installation:
    - Using the [convenience scripts](https://docs.docker.com/engine/install/#server) offered per Linux distro from the Engine install section.
    - Setting up [Docker’s repository](https://docs.docker.com/compose/install/compose-plugin/#install-using-the-repository) and using it to install the compose plugin package.

Use the following command to ckeck that Compose is installed: `docker compose version`

## Compose background
Most applications don’t run in one single component. Even large old apps are typically built as frontend and backend components, which are separate logical layers running in physically distributed components.

Modern cloud-native apps are made of **multiple smaller services** that interact to form a useful app. We call this pattern **“microservices”**. A simple example might be an app with the following seven services: Web front-end, Ordering, Catalog, Back-end database, Logging, Authentication, Authorization.
- Get all of these working together, and you have a useful application.
- **Deploying and managing lots of small microservices** like these can be hard. this is where Docker Compose comes in to play.
- Instead of gluing each microservice together with scripts and long docker commands, Docker Compose lets you describe an entire app in a **single declarative configuration file**, and deploy it with a single command.
- Once the app is deployed, you can **manage its entire lifecycle** with a simple set of commands. You can even store and manage the configuration file in a **version control system**.
- Very neat way of describing the setup for complex distributed apps in a small, clear file format.

Main features of Compose:
- **Multiple isolated environments on a single host**: Compose uses a project name to isolate environments from each other. It prevents different projects and service from interfering with each other.
- **Preserve volume data when containers are created**: Compose preserves all volumes used by your services.
- **Only recreate containers that have changed**: Compose caches the configuration used to create a container.
- **Variables and moving a composition between environments**: Compose supports variables in the Compose file. You can use these variables to customize your composition for different environments, or different users.
- **Portability**: Docker Compose lets you bring up a complete development environment with only one command. This allows us developers to keep our development environment in one central place and helps us to easily deploy our applications.

**The Docker Compose file describes the desired state of your app—what it should look like when everything’s running.**

## Running a application with Compose: icta_app_minimal

Compose uses YAML files to define multi-service applications. The default name for a Compose YAML file is `docker-compose.yml`. However, you can use the `-f` flag to specify custom filenames.

The following example shows a very simple Compose file that defines a small **FastApi app with two microservices** (icta-app-api and icta-app-redis). The app is a simple web server that **counts the number of visits to a web page** and stores the value in Redis.

The app files can be found here (check the files): 
  - `cd docker-kubernetes-prakticna-delavnica/`  
  - `cd 08_Running_Multi_container_Apps_With_Docker_Compose/examples/01_icta_app_minimal`
  - `ls -la`
  - `cat main.py` (the application code)
  - `cat Dockerfile` (describes how to build the image)
  - `cat requirements.txt` (lists the Python packages required for the app)
  - `cat docker-compose.yml` (the Compose file)

> The most current, and recommended [Compose Specification](https://docs.docker.com/compose/compose-file/).

<!-- # add https://docs.docker.com/compose/compose-file/04-version-and-name/#name-top-level-element -->
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
    > By default Compose sets up a single network for your app. Each container for a service joins the default network and is both reachable by other containers on that network, and discoverable by them at a hostname identical to the container name.
- `redis`
    - `image: redis:alpine`: this tells Docker to start a standalone container called redis based on the redis:alpine image. This image will be pulled from Docker Hub.
    - `networks`: The redis container will be attached to the counter-net network.
    - `volumes`: Tells Docker to mount the redis-data volume to /data inside the container. The redis-data volume needs to already exist, or be defined in the volumes top-level key at the bottom of the file.

The service name becomes the container name and the DNS name of the container, which other containers can use to connect on the Docker network. As both services will be deployed onto the same counter-net network, they **will be able to resolve each other by name**. This is important as the application is configured to communicate with the redis service by name.


> **Handling transient errors:** Note the way the get_hit_count function is written. This basic retry loop lets us attempt our request multiple times if the redis service is not available. This is useful at startup while the application comes online, but also makes our application more resilient if the Redis service needs to be restarted anytime during the app’s lifetime. In a cluster, this also helps handling momentary connection drops between nodes.

Compose will also use the name of the directory (01-counter-app) as the project name.

> You can override the project name with either the `--project-name` flag or the `COMPOSE_PROJECT_NAME` environment variable.

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
- `sudo docker compose logs`: Show the apps logs.
- `sudo docker compose logs -f`: Follow log output.
- `sudo docker compose stop`: Stop the app without deleting its resource
- `sudo docker compose ps`
- `sudo docker compose restart`: Restart the app
- `sudo docker compose ps`
- `sudo docker compose down -v`: Stop and delete the app and the volumes


<!-- # TODO: update https://docs.docker.com/compose/compose-application-model/ -->
<!-- https://docs.docker.com/compose/gettingstarted/ -->
<!-- https://docs.docker.com/compose/use-secrets/ -->

## Development with Compose

We can use Compose in the development stage for our apps:
- Move to: `cd ~/docker-k8s/08_Running_Multi_container_Apps_With_Docker_Compose/examples/02-counter-app-dev`
- Check the `docker-compose.dev.yml` file in your project directory.
  - The new volumes key mounts the project directory (current directory) on the host to `/code` inside the container, **allowing you to modify the code on the fly, without having to rebuild the image**. 
  - The environment key sets the `FLASK_ENV` environment variable, which tells flask run to run in development mode and **reload the code on change**. This mode should only be used in development.

From your project directory, type docker compose up to build the app with the updated Compose file, and run it.

    docker compose -f docker-compose.dev.yml up

Check the page in a web browser again, and refresh to see the count increment.

Because the application code is now mounted into the container using a volume, you can make changes to its code and see the changes instantly, without having to rebuild the image.

Change the greeting in app.py and save it. Refresh the app in your browser. The greeting should be updated, and the counter should still be incrementing.

Stop the service: `docker compose -f docker-compose.dev.yml down`

## Production deployment with Compose: counter-app

Moving along, for production environments, we need to add the following:
- Move to folder: `cd ~/docker-k8s/08_Running_Multi_container_Apps_With_Docker_Compose/examples/03-counter-app-prod`
- Add gunicorn (a production-grade WSGI server) to `requirements.txt`
- Let’s create a `wsgi.py` file that will serve as the entry point for our application. This will tell our Gunicorn server how to interact with the application.
- A new Dockerfile called `Dockerfile.prod` for use with production builds. We used a Docker multi-stage build to reduce the final image size. Essentially, builder is a temporary image that's used for building the Python wheels. The wheels are then copied over to the final production image and the builder image is discarded.
- Build the image: `sudo docker build -t leon11sj/counter -f ./Dockerfile.prod .`
- Create a new Compose file called `docker-compose.prod.yml` for production.
  - Add new networks
  - `depends_on` expresses startup and shutdown dependencies between services.
  - `entrypoint` overrides the default entrypoint for the Docker image.
  - Add Nginx into the mix to act as a reverse proxy for Gunicorn to handle client requests as well as serve up static files.
- Run the app: `docker compose -f docker-compose.prod.yml up`
- Stop the app: `docker compose -f docker-compose.prod.yml down -v`

## Scaling and Load Balancing using Compose

<!-- TODO: naredi skripto ki ful kliče endpinte -->

Each service defined in Docker compose configuration can be scaled. The `web-fe` service is effectively stateless, so you can scale it up to run on multiple containers. When the `nginx` container requests data from the `web-fe`, Docker will share those requests across the running `web-fe` containers.

In the same terminal session, use Docker Compose to increase the scale of the `web-fe` service, and then refresh the web page a few times and check the hostname of the containers:
- `docker compose -f docker-compose.prod.yml up -d`
- `docker compose -f docker-compose.prod.yml ps`
- Scale up: `docker compose -f docker-compose.prod.yml up -d --scale web-fe=3`
- `docker compose -f docker-compose.prod.yml ps`

Docker Compose is a client-side tool. It’s a command line that sends instructions to the Docker API based on the contents of the Compose file. Docker itself just runs containers; it isn’t aware that many containers represent a single application. Only Compose knows that, and Compose only knows the structure of your application by looking at the Docker Compose YAML file, so you need to have that file available to manage your app.

> It’s possible to get your application out of sync with the Compose file, such as when the Compose file changes or you update the running app. That can cause unexpected behavior when you return to manage the app with Compose.

Containers plugged into the same Docker network will get IP addresses in the same network range, and they connect over that network. Using DNS means that when your containers get replaced and the IP address changes, your app still works because the DNS service in Docker will always return the current container’s IP address from the domain lookup.

Connect to a session in the `nginx` container and perform a DNS lookup: `docker container exec -it 03-counter-app-prod-nginx-1 sh`
- `nslookup web-fe`
- `ping web-fe` 
- `ping web-fe` 
- `ping web-fe`

In the DNS lookup for the `web-fe`, you can see that three IP addresses are returned, one for each of the three containers in the service.

DNS servers can return multiple IP address for a domain name. Docker Compose uses this mechanism for simple load-balancing, returning all the container IP addresses for a service. It’s up to the application that makes the DNS lookup how it processes multiple responses; some apps take a simplistic approach of using the first address in the list. 

To try to **provide load-balancing across all the containers**, the Docker DNS returns the list in a different order each time. 
- `nslookup web-fe`
- `nslookup web-fe`
- `nslookup web-fe`
- `exit`

You’ll see that if you repeat the nslookup call - it’s a basic way of trying to spread traffic around all the containers.

Few more steps:
- Scale down: `docker compose -f docker-compose.prod.yml up -d --scale web-fe=1`
- `docker compose -f docker-compose.prod.yml ps`
- Stop the app: `docker compose -f docker-compose.prod.yml down -v`

## Advanced Compose features (Advanced)
More [here](./Advanced_Compose_features.md).
