#  Docker Storage And Volumes

## Introduction to Docker Storage And Volumes

Consider what it might look like to run a database program inside a container.
You would package the software with the image, and when you start the container,
it might initialize an empty database. 
- When programs connect to the database and enter data, where is that data stored? 
- Is it in a file inside the container? 
- What happens to that data when you stop the container or remove it? 
- How would you move your data if you wanted to upgrade the database program? 
- What happens to that storage on a cloud machine when it is terminated?

Consider another situation where you’re running a couple of different web applications
inside different containers. 
- Where would you write log files so that they will outlive the container? 
- How would you get access to those logs to troubleshoot a problem?
- How can other programs such as log digest tools get access to those files?

---

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

> [About storage drivers](https://docs.docker.com/storage/storagedriver/): Storage drivers are optimized for space efficiency, but (depending on the storage driver) write speeds are lower than native file system performance, especially for storage drivers that use a copy-on-write filesystem. Write-intensive applications, such as database storage, are impacted by a performance overhead, particularly if pre-existing data exists in the read-only layer. Use Docker volumes for write-intensive data, data that must persist beyond the container’s lifespan, and data that must be shared between containers.

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

The `/code` directory is a Docker volume that can either be mapped to an external storage system or a directory on the Docker host. Either way, its lifecycle is decoupled from the container. All other directories in the container use the thin writable container layer in the local storage area on the Docker host.

## Creating and managing Docker volumes

Volumes are **first-class citizens** in Docker. Among other things, this means they are their own object in the API and have their own `docker volume` sub-command. 

There are two ways to use volumes with containers: 
- you can manually create volumes and attach them to a container
- you can use a VOLUME instruction in the Dockerfile (more in chapter 6).

Use the following command to **create a new volume** called myvol.
- `sudo docker volume create myvol`

By default, Docker creates new volumes with the **built-in local driver**. As the name suggests, volumes created with the local driver are only available to containers on the same node as the volume. You can use the `-d` flag to specify a different driver.

Third-party volume drivers are available as plugins. These provide Docker with seamless access external storage systems such as cloud storage services and on-premises storage systems including SAN or NAS.

> [More](https://docs.docker.com/storage/volumes/#use-a-volume-driver) about third party volme drivers.

![Third-party volume](./images/img03.png)
<!-- Vir: Docker Deep Dive, Nigel Poulton -->

Now that the volume is created, you can see it with the `docker volume ls` command and inspect it with the `docker volume inspect` command.
- `sudo docker volume ls`
- `sudo docker volume inspect myvol`

Notice that the `Driver` and `Scope` are both local. This means the volume was created with the local driver and is only available to containers on this Docker host. 

The `Mountpoint` property tells us where in the Docker host’s filesystem the volume exists. All volumes created with the local driver get their own directory under `/var/lib/docker/volumes` on Linux. This means you can see them in your Docker host’s filesystem. You can even **access them directly from your Docker host, although this is not normally recommended**.

There are two ways to delete a Docker volume:
- `sudo docker volume prune` will delete all volumes that are not mounted into a container or service replica.
- `sudo docker volume rm` lets you specify exactly which volumes you want to delete. 

Neither command will delete a volume that is in use by a container or service replica.

## Demonstrating volumes with containers and services

**If you start a container with a volume that does not yet exist, Docker creates the volume for you**. 

There are 2 options to use volumes with containers. In general, `--mount` is more explicit and verbose. The biggest difference is that the `-v` syntax combines all the options together in one field, while the `--mount` syntax separates them. If you need to specify volume driver options, you must use `--mount`.

> [Choose the -v or --mount flag](https://docs.docker.com/storage/volumes/#choose-the--v-or---mount-flag). As opposed to bind mounts, all options for volumes are available for both `--mount` and `-v` flags.

Use the following command to create a new standalone container that mounts a volume:
- `sudo docker run -d --name dev-server --mount source=server-data,target=/app nginx:latest`

or
- `sudo docker run -d --name dev-server -v server-data:/app nginx:latest`

Use docker inspect devtest to verify that the volume was created: `sudo docker volume inspect server-data` and mounted correctly: `sudo docker inspect dev-server` (Mounts section)

Although containers and volumes have separate lifecycle’s, you cannot delete a volume that is in use by a container: `sudo docker volume rm server-data`

The volume is brand new, so it doesn’t have any data. Let’s exec onto the container and write some data to it.
- `sudo docker container exec -it dev-server sh`
- `ls -lah`
- `echo "Test volume" > /app/file1`
- `ls -l /app`
- `cat /app/file1`

Type `exit` to return to the shell of your Docker host, and then delete the container with the following command: `sudo docker container rm -f dev-server`

Even though the container is deleted, the volume still exists: `sudo docker container ls -a` and `sudo docker volume ls`.

Because the volume still exists, you can look at its mount point on the host to check if the data is still there. Run the following commands from the terminal of your Docker host. The first one will show that the file still exists, the second will show the contents of the file.
- `sudo ls -l /var/lib/docker/volumes/server-data/_data/`
- `sudo cat /var/lib/docker/volumes/server-data/_data/file1`

It’s even possible to mount the volume into a new service or container.
- `sudo docker run -d --name dev-server-2 --mount source=server-data,target=/app nginx:latest`

Exec onto the container and check that the data is present:
- `sudo docker container exec -it dev-server-2 sh`
- `cat /app/file1`
- `exit`

Excellent, the volume has preserved the original data and made it available to a new container.

Stop the container and remove the volume. Note volume removal is a separate step.
- `sudo docker container stop dev-server-2`
- `sudo docker container rm dev-server-2`
- `sudo docker volume rm server-data`

## Populate a volume using a container
- https://docs.docker.com/storage/volumes/#populate-a-volume-using-a-container

## Use a read-only volume
- https://docs.docker.com/storage/volumes/#use-a-read-only-volume

## Share data between Docker containers
- Potential data corruption NP - 198

## Use a third party volume driver (Advanced)
- NP - 196 (Sharing storage across cluster nodes)

## Running containers with filesystem mounts (Bind mounts)

Docker also provides a **more direct way of sharing storage** between containers and hosts using **bind mounts**.

A bind mount **makes a directory on the host available as a path on a container**. The bind mount is transparent to the container—it’s just a directory that is part of the container’s filesystem. But it means you can access host files from a container and vice versa, which unlocks some interesting patterns.

- https://docs.docker.com/storage/bind-mounts/
- https://docs.docker.com/storage/bind-mounts/#use-a-read-only-bind-mount
- ES 85
- primer z NGINX iz starih gradiv

## Limitations of filesystem mounts
- https://docs.docker.com/storage/bind-mounts/#mount-into-a-non-empty-directory-on-the-container
- ES 88

## Understanding how the container filesystem is built (Advanced)
 - ES - 92

## Use tmpfs mounts (Advanced)
- https://docs.docker.com/storage/tmpfs/

## Choose the right type of mount
- https://docs.docker.com/storage/

## Example: Run a PostgreSQL database
- https://hub.docker.com/_/postgres/
- ES - 93 Lab

