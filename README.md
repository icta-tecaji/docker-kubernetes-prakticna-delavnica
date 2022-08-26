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
- Creating and managing Docker volumes
- Demonstrating volumes with containers and services
- Populate a volume using a container
- Use a read-only volume
- Share data between Docker containers
- Use a third party volume driver (Advanced)
- Running containers with filesystem mounts (Bind mounts)
- Limitations of filesystem mounts
- Understanding how the container filesystem is built (Advanced)
- Use tmpfs mounts (Advanced)
- Choose the right type of mount
- Example: Run a PostgreSQL database

## [Del 5: Docker Networking](./05_Docker_Networking/README.md)
- Docker networking overview
- Docker network architecture (Advanced)
- Network drivers
- Bridge networks
- Host network
- Overlay networks
- Connecting to existing networks (Advanced)
- Disable networking for a container
- Port Mapping
- Service discovery (Advanced)
- Docker and iptables (Advanced)

## [Del 6: Building Images](./06_Building_Images/README.md)
- Containerizing an app - overview
- Building your first container image
- Understanding Docker images and image layers
- Understanding the image layer cache
- Understand how CMD and ENTRYPOINT interact
- Difference between the COPY and ADD commands
- Using the VOLUME command inside Dockerfiles
- Best practices for writing Dockerfiles
- Example: Build a Python application
- Use multi-stage builds
- More best practices for writing Dockerfiles (Advanced) 
- Building Docker images from a container (Advanced)
- Build images with BuildKit (Advanced)

## [Del 7: Sharing Docker Images](./07_Sharing_Docker_Images/README.md)
- https://docs.docker.com/get-started/04_sharing_app/
- Searching Docker Hub from the CLI (NP-59)
- Pulling images by digest (NP - 65)
- reteg a image
- NP 96

## [Del 8: Running Multi-container Apps With Docker Compose](./08_Running_Multi_container_Apps_With_Docker_Compose/README.md)
- razlika med verzijami composa in kako se inštwlira

## [Del 9: Docker Reliability And Health Checks](./09_Docker_Reliability_And_Health_Checks/README.md)
- running processes as pid 1
- Resource control
- Setting resource allowances
    - Memory limits
    - CPU
    - Access to devices
- Sharing memory
- Understanding users
    - Working with the run-as user
- NP DDD - 84: Self-healing containers with restart policies

## [Del 10: Managing Application Logs](./10_Managing_Application_Logs/README.md)
- https://sematext.com/guides/docker-logs/

## [Del 11: Monitoring](./11_Monitoring/README.md)
- Portainer

## [Del 12: Docker Configuration Management](./12_Docker_Configuration_Management/README.md)
- env variables ES-34

## [Del 13: Docker Security](./13_Docker_Security/README.md)
- Container security
- Container scanning
- https://docs.docker.com/network/iptables/#restrict-connections-to-the-docker-host

## [Del 14: Advanced Docker](./14_Advanced_Docker/README.md)
- Controlling HTTP traffic to containers with a reverse proxy
- Multi-architecture images (NP - 67)
- Asynchronous communication with a message queue
- https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504

## [Del 15: Docker Exercises](./15_Docker_Exercises/README.md)
- praktični primeri realnih aplikaciji

## Del 16: Container orchestration and microservices
- Kubernetes vs Docker Swarm


## Del 17: Introduction to Kubernetes
- Kubernetes history
- Kubernetes principles of operation
- Kubernetes architecture

## Del 18: Kubernetes Pods

## Del 19: Replication controllers

## Del 20: Kubernetes Deployments



## Gradiva
- [Docker Official Samples](https://docs.docker.com/samples/#tutorial-labs)
- [Github: Microservices Demo](https://github.com/microservices-demo)
- [Docker Tips, Tricks and Tutorials](https://nickjanetakis.com/blog/tag/docker-tips-tricks-and-tutorials)
- [Collabnix](https://collabnix.com/)











## Kubernetes
- https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/