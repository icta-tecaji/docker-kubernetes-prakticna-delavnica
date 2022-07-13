# Best practices for writing Dockerfiles

## Viri
- [https://docs.docker.com/develop/develop-images/dockerfile_best-practices/](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

## General guidelines and recommendations

Docker builds images automatically by reading the instructions from a **Dockerfile** -- a text file that contains all commands, in order, needed to build a given image. A Dockerfile adheres to a specific format and set of instructions.

A Docker image consists of read-only layers each of which represents a Dockerfile instruction. The layers are stacked and each one is a delta of the changes from the previous layer. Consider this Dockerfile:

```Dockerfile
# syntax=docker/dockerfile:1
FROM ubuntu:18.04
COPY . /app
RUN make /app
CMD python /app/app.py
```

Each instruction creates one layer:
- `FROM` creates a layer from the ubuntu:18.04 Docker image.
- `COPY` adds files from your Docker client’s current directory.
- `RUN` builds your application with make.
- `CMD` specifies what command to run within the container.

When you run an image and generate a container, you **add a new writable layer** (the “container layer”) on top of the underlying layers. All changes made to the running container, such as writing new files, modifying existing files, and deleting files, are written to this writable container layer.

### Create ephemeral containers
The image defined by your Dockerfile should generate containers that are as ephemeral as possible. By “ephemeral”, we mean that the container can be stopped and destroyed, then rebuilt and replaced with an absolute minimum set up and configuration.

### Understand build context
When you issue a docker build command, the current working directory is called the **build context**. By default, the Dockerfile is assumed to be located here, but you can specify a different location with the file flag (`-f`). Regardless of where the `Dockerfile` actually lives, all recursive contents of files and directories in the current directory are sent to the Docker daemon as the build context.

