# Praktična delavnica Docker & Kubernetes

## Del 1: Intro To Docker

## Del 2: Containers

## Del 3: Docker Storage And Volumes
- https://docs.docker.com/storage/storagedriver/

## Del 4: Docker Networking

## Del 5: Building Images
- Best practices for writing Dockerfiles
- Optimizing your Docker images

## Del 6: Sharing Docker Images

## Del 7: Running Multi-container Apps With Docker Compose

## Del 8: Docker Reliability And Health Checks
- Resource control

## Del 9: Managing Application Logs

## Del 10: Monitoring
- Portainer

## Del 11: Docker Configuration Management

## Del 12: Docker Security

## Del 13: Advanced Docker
- Controlling HTTP traffic to containers with a reverse proxy
- Asynchronous communication with a message queue

## Gradiva
- [Docker Official Samples](https://docs.docker.com/samples/#tutorial-labs)
- https://nickjanetakis.com/blog/tag/docker-tips-tricks-and-tutorials
- https://collabnix.com/



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