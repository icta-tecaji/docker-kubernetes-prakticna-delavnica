# Praktična delavnica Docker & Kubernetes

## Prerequisites
- Clone this repository: `git clone https://github.com/icta-tecaji/docker-kubernetes-prakticna-delavnica.git`


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
- Building and Testing Multi-Arch Images (Advanced)
- Building Wasm Images (Advanced)
- Generate the SBOM for Docker images (Advanced)

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
- Advanced Compose features (Advanced)

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
- Podman
- Run the Docker daemon as a non-root user - Rootless mode (Advanced)
- Controlling HTTP traffic to containers with a reverse proxy

- Asynchronous communication with a message queue
- https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504

## [Del 15: Docker Exercises](./15_Docker_Exercises/README.md)
- praktični primeri realnih aplikaciji

## [Del 16: Container orchestration and microservices](./16_Container_orchestration_and_microservices/README.md)
- Traditional applications
- Microservices
- Moving from monolithic apps to microservices
- 12 Factor Apps
- Container Orchestration
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
- Deploying your first application

## [Del 18: Kubernetes Pods](./18_Kubernetes_Pods/README.md)
- Pod theory
- Understanding pods
- Sidecar containers
- Creating pods
- Viewing application logs
- Copying files to and from containers
- Executing commands in running containers
- Running multiple containers in a pod
- Running init containers
- Deleting pods and other objects

## [Del 19: Managing the lifecycle of the Pod](./19_Managing_the_lifecycle_of_the_Pod/README.md)
- Understanding the pod's status
- Understanding pod conditions
- Understanding the status of the containers
- Keeping containers healthy
- Liveness probes
- Startup probes
- Lifecycle hooks

## Del 20: Replication controllers

## Del 21: Kubernetes Deployments
- Performing a rolling update
- Managing app releases with rollouts and rollbacks

## [Del 22: Services, Load Balancing, and Networking](./22_Services_Load_Balancing_and_Networking/README.md)
- Understanding how pods communicate
- Introducing services
- Accessing Services from outside the cluster with NodePort Service
- Accessing Services from outside the cluster with LoadBalancer Service
- Ingress
- Service Mesh (Advanced)

## Del 23: Storing data in Kubernetes
- Volumes
- Storage Providers

## [Del 24: Configuring applications with ConfigMaps and Secrets](./24_Configuring_applications_with_ConfigMaps_and_Secrets/README.md)
- Configuring containerized applications
- Using environment variables in Kubernetes
- Creating configmaps using the kubectl
- Storing and using configuration files in ConfigMaps

## Del 25: Scaling applications

## Del 26: StatefulSets and Jobs

## Del 27: Centralized logging and monitoring applications

## Del 28: Packaging and managing apps with Helm

## Del 29: Deploying application on a cluster

## Del 30: Kubernetes security
- Securing applications with policies, contexts, and admission control

## Del 31: Advanced Kubernetes
- running private images



- https://realpython.com/build-a-python-url-shortener-with-fastapi/



## Gradiva
- [Docker Official Samples](https://docs.docker.com/samples/#tutorial-labs)
- [Github: Microservices Demo](https://github.com/microservices-demo)
- [Docker Tips, Tricks and Tutorials](https://nickjanetakis.com/blog/tag/docker-tips-tricks-and-tutorials)
- [Collabnix](https://collabnix.com/)
- [Articles: Production-ready Docker packaging for Python developers](https://pythonspeed.com/docker/)
- [Awesome Docker](https://github.com/veggiemonk/awesome-docker)
- [Learning Containers, Kubernetes, and Backend Development with Ivan Velichko](https://iximiuz.com/en/)
- https://iximiuz.com/en/posts/learn-by-doing-platforms/


## Kubernetes
- https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/

