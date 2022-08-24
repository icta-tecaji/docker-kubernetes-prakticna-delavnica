# Docker Networking

## Docker networking overview
Docker runs applications inside of containers, and applications need to communicate over lots of different networks. This means Docker needs strong networking capabilities.

One of the reasons Docker containers and services are so powerful is that you can **connect them together**, or **connect them to non-Docker workloads** and VLANs.

Docker **abstracts the underlying host-attached network from containers**. Doing so provides a degree of runtime environment agnosticism for the application, and allows infrastructure managers to adapt the implementation to suit the operating environment.

Docker also treats **networks as first-class entities**. This means that they have their own life cycle and are not bound to any other objects. You can define and manage them directly by using the `docker network` subcommands.

To get started with networks in Docker, examine the **default networks** that are available with every Docker installation. Running `docker network ls` will print a table of all the networks to the terminal.
- `sudo docker network ls`

By default, Docker includes three networks, and each is provided by a different driver.
- The network named **bridge** is the default network and provided by a bridge driver. The bridge driver provides intercontainer connectivity for all containers running on the same machine. 
- The **host** network is provided by the host driver, which instructs Docker not to create any special networking namespace or resources for attached containers. Containers on the host network interact with the host’s network stack like uncontained processes. 
- Finally, the **none** network uses the null driver. Containers attached to the none network will not have any network connectivity outside themselves.

## Docker network architecture (Advanced)
- NP-152


## Network drivers
Docker’s networking subsystem is pluggable, using drivers. Several drivers exist by default, and provide core networking functionality:
- **`bridge`**: The default network driver. If you don’t specify a driver, this is the type of network you are creating. Bridge networks are usually used when your applications run in standalone containers that need to communicate.
    - The default bridge network maintains compatibility with legacy Docker and cannot take advantage of modern Docker features including service discovery or load balancing. Using it is not recommended. So the first thing you should do is create your own bridge network.
    - User-defined bridge networks are best when you need multiple containers to communicate on the same Docker host.
- **`host`**: For standalone containers, remove network isolation between the container and the Docker host, and use the host’s networking directly.
    - Host networks are best when the network stack should not be isolated from the Docker host, but you want other aspects of the container to be isolated.
- https://docs.docker.com/network/#network-drivers

## Bridge networks
- https://docs.docker.com/network/bridge/
- https://docs.docker.com/network/network-tutorial-standalone/
- NP-155
- stara gradiva

## Host network
- https://docs.docker.com/network/host/
- https://docs.docker.com/network/network-tutorial-host/

## Overlay networks
- Na hitro povemo, se ne spuščamo globoko
- https://docs.docker.com/network/overlay/
- https://docs.docker.com/network/network-tutorial-overlay/

## Connecting to existing networks (Advanced)
- NP- 163
- https://docs.docker.com/network/macvlan/
- https://docs.docker.com/network/ipvlan/
- https://docs.docker.com/network/network-tutorial-macvlan/

## Disable networking for a container
If you want to completely disable the networking stack on a container, you can use the `--network none` flag when starting the container. Within the container, **only the loopback device is created**. 
- `sudo docker run --rm -dit --network none --name no-net-alpine alpine:latest ash`

Check the container’s network stack, by executing some common networking commands within the container. 
- `sudo docker exec no-net-alpine ip link show` (Notice that no `eth0` was created.)
- `sudo docker exec no-net-alpine ip route` (The command returns empty because there is no routing table.)
- `docker stop no-net-alpine`

## Service discovery (Advanced)
- NP - 169
- https://docs.docker.com/config/containers/container-networking/#dns-services

## Docker and iptables (Advanced)
- https://docs.docker.com/network/iptables/#restrict-connections-to-the-docker-host
- pokažemo ufw da ne blokira, kako blokiramo promet
- https://docs.docker.com/network/proxy/ (dodatno samo napišemo)