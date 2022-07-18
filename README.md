# Praktična delavnica Docker & Kubernetes

## [Del 1: Intro To Docker](./01_Intro_To_Docker/README.md)
- Docker overview
- Why are containers and Docker so important?
- Installing Docker
- Running Hello World in a container
- Example: Running multiple NGINX instances
- Docker Architecture
- The Docker Engine (Advanced)

## [Del 2: Containers](./02_Containers/README.md)
- Containers History
- Containers vs Virtual Machines
- What is a container?
- Starting a simple container
- Container processes
- Web server example
- Container lifecycle

## Del 3: Images
- About images
- Commands

## Del 4: Docker Storage And Volumes
- https://docs.docker.com/storage/storagedriver/

## Del 5: Docker Networking

## Del 6: Building Images
- Best practices for writing Dockerfiles
- Optimizing your Docker images

## Del 7: Sharing Docker Images

## Del 8: Running Multi-container Apps With Docker Compose
- razlika med verzijami composa in kako se inštwlira

## Del 9: Docker Reliability And Health Checks
- Resource control
- NP DDD - 84: Self-healing containers with restart policies

## Del 10: Managing Application Logs

## Del 11: Monitoring
- Portainer

## Del 12: Docker Configuration Management

## Del 13: Docker Security

## Del 14: Advanced Docker
- Controlling HTTP traffic to containers with a reverse proxy
- Asynchronous communication with a message queue

## Del 15: Docker Exercises 


## Gradiva
- [Docker Official Samples](https://docs.docker.com/samples/#tutorial-labs)
- [Github: Microservices Demo](https://github.com/microservices-demo)

- https://nickjanetakis.com/blog/tag/docker-tips-tricks-and-tutorials
- https://collabnix.com/

- https://github.com/sixeyed/diamol


# Docker
- zakaj docker (lažja inštalacija) - se pokaže primer
- kaj je docker
- namestitev
- hello world image
	- tukaj se nariše shema kaj se zgodi, malo pokaže komponente, dockerhub
- kaj je container
	- namespacing
	- control group
- kako je image povezan z kontejnerjem
- docker run command, overrinding defoult commands
- docker ps, busybox, docker ps --all
- docker run = docker create + docker start
- lifecycle of a docker conatiner
- docker system prune -> zbrišemo vse neuborabljene zdeve u dockerju
- docker container prune
- docker rm 
- docker getting logs
- docker stop, kill
- docker exec -it
- container isolation

## Storage and volumes
- File trees and mount points
- Bind mounts
- In-memory storage
- Docker volumes
    - Volumes provide container-independent data management
    - 

## Single host networking
- Docker container networking
    - Network drivers
- Bridge networks
    - Differences between user-defined bridges and the default bridge
    - Manage a user-defined bridge
    - Exploring a bridge network
- Host and none network



## Resource controls
- Setting resource allowances
    - Memory limits
    - CPU
    - Access to devices
- Sharing memory
- Understanding users
    - Working with the run-as user

## Kubernetes
- https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/