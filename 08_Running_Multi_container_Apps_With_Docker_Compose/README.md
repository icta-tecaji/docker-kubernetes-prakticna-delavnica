# Running Multi-container Apps With Docker Compose

## Overview of Docker Compose and installation
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. 

> **Compose V2 and the new docker compose command**: The new Compose V2, which supports the `compose` command as part of the Docker CLI, is now available. Compose V2 integrates compose functions into the Docker platform, continuing to support most of the previous `docker-compose` features and flags. You can run Compose V2 by replacing the hyphen (-) with a space, using `docker compose`, instead of `docker-compose`. [Compose command compatibility with docker-compose](https://docs.docker.com/compose/cli-command-compatibility/).

[Compose installation scenarios](https://docs.docker.com/compose/install/):
- (Mac, Win, Linux) Docker Desktop: If you have Desktop installed then you already have the Compose plugin installed.
- Linux systems: To install the Docker CLI’s Compose plugins use one of these methods of installation:
    - Using the [convenience scripts](https://docs.docker.com/engine/install/#server) offered per Linux distro from the Engine install section.
    - Setting up [Docker’s repository](https://docs.docker.com/compose/install/compose-plugin/#install-using-the-repository) and using it to install the compose plugin package.

## Compose background
- NP 110

## Running a single-container application with Compose

## Running a multi-container application with Compose