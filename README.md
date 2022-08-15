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
- Exploring the container filesystem and the container lifecycle
- Stopping containers gracefully

## [Del 3: Docker Images](./03_Docker_Images/README.md)
- About Docker Images
- Images are usually small
- Pulling images
- Image registries
- Image naming and tagging
- Filtering the images on the host
- Images and layers
- Deleting Images

## [Del 4: Docker Storage And Volumes](./04_Docker_Storage_And_Volumes/README.md)
- Introduction to Docker Storage And Volumes
- Containers and non-persistent data
- Running containers with Docker volumes




- https://docs.docker.com/storage/storagedriver/
- https://docs.docker.com/storage/volumes/

## Del 5: Docker Networking

## Del 6: Building Images
- Best practices for writing Dockerfiles
- Optimizing your Docker images
- https://docs.docker.com/develop/develop-images/build_enhancements/

## Del 7: Sharing Docker Images
- https://docs.docker.com/get-started/04_sharing_app/
- Searching Docker Hub from the CLI (NP-59)
- Pulling images by digest (NP - 65)

## Del 8: Running Multi-container Apps With Docker Compose
- razlika med verzijami composa in kako se inštwlira

## Del 9: Docker Reliability And Health Checks
- Resource control
- NP DDD - 84: Self-healing containers with restart policies

## Del 10: Managing Application Logs
- https://sematext.com/guides/docker-logs/

## Del 11: Monitoring
- Portainer

## Del 12: Docker Configuration Management

## Del 13: Docker Security

## Del 14: Advanced Docker
- Controlling HTTP traffic to containers with a reverse proxy
- Multi-architecture images (NP - 67)
- Asynchronous communication with a message queue
- https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504


## Del 15: Docker Exercises 


## Gradiva
- [Docker Official Samples](https://docs.docker.com/samples/#tutorial-labs)
- [Github: Microservices Demo](https://github.com/microservices-demo)

- https://nickjanetakis.com/blog/tag/docker-tips-tricks-and-tutorials
- https://collabnix.com/

- https://github.com/sixeyed/diamol


# Docker
- zakaj docker (lažja inštalacija) - se pokaže primer

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