#  Docker Storage And Volumes

## Introduction to Docker Storage And Volumes

Containers are a **perfect runtime for stateless applications**. You can meet increased demand by running multiple containers on your cluster, knowing that every container will handle requests in the same way. You can release updates with an automated rolling upgrade, which keeps your app online the whole time.

But not all parts of your app will be stateless. There will be components that use disks to improve performance or for permanent data storage. And you can run those components in Docker containers too. **Stateful applications that persist data are becoming more and more important in the world of cloud-native** and
microservices applications.

There are two main categories of data — persistent and non-persistent.
- **Persistent** is the data you need to keep. 
    - Things like; customer records, financial data, research results, audit logs, and even some types of application log data. 
    - To deal with persistent data, a container needs to store it in a volume.
- **Non-persistent** is the data you don’t need to keep.
    - To deal with non-persistent data, every Docker container gets its own non-persistent storage. This is automatically created for every container and is tightly coupled to the lifecycle of the container. As a result, deleting the container will delete the storage and any data on it.

There’s a popular opinion that containers aren’t good for stateful applications that persist data. this was true a few years ago. However, things are changing, and technologies now exist that **make containers a viable choice for many stateful applications**.

## Containers and non-persistent data
Containers are designed to be immutable. It’s a best practice not to change the configuration of a container after it’s deployed. **You shouldn’t log into a running container and make configuration changes.**

Many applications require a read-write filesystem in order to simply run – they won’t even run on a read-only filesystem. This means it’s not as simple as making containers entirely read-only. Every Docker container is created by **adding a thin read-write layer on top of the read-only image** it’s based on.

![RW layer](./images/img01.png)
<!-- Vir: Docker Deep Dive, Nigel Poulton -->

The writable container layer exists in the filesystem of the Docker host, and you’ll hear it called various names. These include local storage, ephemeral storage, and graphdriver storage. It’s typically located on the Docker host in these locations: `/var/lib/docker/<storage-driver>/....`

This thin writable layer is an integral part of a container and enables all read/write operations. If you, or an application, update files or add new files, they’ll be written to this layer. This writable layer of local storage is managed on every Docker host by a storage driver.

Each container has its **own filesystem, independent of other containers**. You can run multiple containers from the same Docker image, and they will all start with the same disk contents. The application can **alter files in one container**, and that **won’t affect the files in other containers**.

The container writeable layer is created by Docker when the container is started, and it’s deleted by Docker when the container is removed. (Stopping a container doesn’t automatically remove it, so a stopped container’s filesystem does still exist.)

A container **can edit existing files from the image layers.** But image layers are read-only, so Docker does some special magic to make that happen. It uses a **copy-on-write process** to allow edits to files that come from read-only layers. When the container tries to edit a file in an image layer, Docker actually makes a copy of that file into the writable layer, and the edits happen there. It’s all seamless for the container and the application, but it’s the cornerstone of Docker’s super-efficient use of storage.

## Running containers with Docker volumes
A Docker volume is a unit of storage—you can think of it as a USB stick for containers. Volumes are the recommended way to persist data in containers. There are three major reasons for this:
- Volumes are **independent objects** that are not tied to the lifecycle of a container
- Volumes can be mapped to **specialized external storage** systems
- Volumes enable **multiple containers** on different Docker hosts to access and **share the same data**

At a high-level, you create a volume, then you create a container and mount the volume into it. The volume is mounted into a directory in the container’s filesystem, and anything written to that directory is stored in the volume. **If you delete the container, the volume and its data will still exist.**

![Volume](./images/img02.png)
<!-- Vir: Docker Deep Dive, Nigel Poulton -->

The /code directory is a Docker volume that can either be mapped to an external storage system or a directory on the Docker host. Either way, its lifecycle is decoupled from the container. All other directories in the container use the thin writable container layer in the local storage area on the Docker host.

NP - 191
ES - 80