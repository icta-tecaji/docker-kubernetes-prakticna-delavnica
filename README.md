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
- Run containers as non-root user
- Best practices for writing Dockerfiles
- Example: Build a Python application
- Use multi-stage builds
- More best practices for writing Dockerfiles (Advanced) 
- Building Docker images from a container (Advanced)
- Build images with BuildKit (Advanced)

## [Del 7: Sharing Docker Images](./07_Sharing_Docker_Images/README.md)
- Working with registries, repositories, and image tags
- Create a repo on Docker Hub
- Pushing your own images to Docker Hub
- Run the image on a new instance
- Introducing self-hosted registries
- Running and using your own Docker registry
- Using image tags effectively
- Configure the credentials store (Advanced)

## [Del 8: Running Multi-container Apps With Docker Compose](./08_Running_Multi_container_Apps_With_Docker_Compose/README.md)
- Overview of Docker Compose and installation
- Compose background
- Running a application with Compose: counter-app
- Development with Compose
- Production deployment with Compose: counter-app
- Scaling and Load Balancing using Compose

## [Del 9: Docker Reliability And Health Checks](./09_Docker_Reliability_And_Health_Checks/README.md)
- Self-healing containers with restart policies
- Using restart policies in Docker Compose
- Understanding PID 1 in Docker containers
- Docker Resource Management (Advanced)
- Building health checks into Docker images
- Starting containers with dependency checks
- Defining health checks and dependency checks in Docker Compose

## [Del 10: Managing Application Logs](./10_Managing_Application_Logs/README.md)
- https://sematext.com/guides/docker-logs/
- https://docs.docker.com/config/containers/logging/configure/

## [Del 11: Monitoring](./11_Monitoring/README.md)
- Portainer

## [Del 12: Docker Configuration Management](./12_Docker_Configuration_Management/README.md)
- env variables ES-34
- use secret config 

## [Del 13: Docker Security](./13_Docker_Security/README.md)
- Container security
- Container scanning
- Understanding users
    - Working with the run-as user
- https://docs.docker.com/network/iptables/#restrict-connections-to-the-docker-host
- https://docs.docker.com/security/

## [Del 14: Advanced Docker](./14_Advanced_Docker/README.md)
- Controlling HTTP traffic to containers with a reverse proxy
- Multi-architecture images (NP - 67)
- Asynchronous communication with a message queue
- https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504

## [Del 15: Docker Exercises](./15_Docker_Exercises/README.md)
- praktični primeri realnih aplikaciji

## [Del 16: Container orchestration and microservices](./16_Container_orchestration_and_microservices/README.md)
- Kubernetes vs Docker Swarm

## [Del 17: Introduction to Kubernetes](./17_Introduction_to_Kubernetes/README.md)
- About Kubernetes
- Kubernetes history
- Understanding Kubernetes
- The benefits of using Kubernetes
- Kubernetes architecture
- Kubernetes versions
- Install Kubernetes
- Should you even use Kubernetes?
- How Kubernetes runs an application

## Del 18: Kubernetes Pods
- multicontainer Pods
- self-healing apps

## Del 19: Replication controllers

## Del 20: Kubernetes Deployments
- Performing a rolling update
- Managing app releases with rollouts and rollbacks

## Del 21: Services, Load Balancing, and Networking

## Del 22: Storing data in Kubernetes
- Volumes
- Storage Providers

## [Del 23: Configuring applications with ConfigMaps and Secrets](./23_Configuring_applications_with_ConfigMaps_and_Secrets/README.md)
- Configuring containerized applications
- Using environment variables in Kubernetes
- Creating configmaps using the kubectl
- Storing and using configuration files in ConfigMaps

## Del 24: Scaling applications

## Del 25: StatefulSets and Jobs

## Del 26: Centralized logging and monitoring applications

## Del 27: Packaging and managing apps with Helm

## Del 28: Kubernetes security
- Securing applications with policies, contexts, and admission control

## Del 29: Advanced Kubernetes
- running private images

## Del 30: Developer workflows and CI/CD

## Gradiva
- [Docker Official Samples](https://docs.docker.com/samples/#tutorial-labs)
- [Github: Microservices Demo](https://github.com/microservices-demo)
- [Docker Tips, Tricks and Tutorials](https://nickjanetakis.com/blog/tag/docker-tips-tricks-and-tutorials)
- [Collabnix](https://collabnix.com/)
- [Articles: Production-ready Docker packaging for Python developers](https://pythonspeed.com/docker/)










## Kubernetes
- https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/