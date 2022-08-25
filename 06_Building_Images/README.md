# Building Images

## Containerizing an app - overview
The process of taking an application and configuring it to run as a container is called “containerizing”.

The process of containerizing an app looks like this:
1. Start with your application code and dependencies
2. Create a `Dockerfile` that describes your app, its dependencies, and how to run it
3. Feed the `Dockerfile` into the docker image build command
4. Push the new image to a registry (optional)
5. Run container from the image

Once your app is containerized (made into a container image), you’re ready to share it and run it as a container.

![CNM](./images/img01.png)
<!-- Vir: Docker Deep Dive, Nigel Poulton -->





## VOLUME command
However, it’s also possible to deploy volumes via Dockerfiles using the VOLUME instruction. The format is VOLUME `<container-mount-point>`. Interestingly, you cannot specify a directory on the host when defining a volume in a Dockerfile. is is because host directories are different depending on what OS your Doer host is running
– it could break your builds if you specified a directory on a Doer host that doesn’t exist. As a result, defining
a volume in a Doerfile requires you to specify host directories at deploy-time.

Anonymous volumes have no specific source so when the container is deleted, instruct the Docker Engine daemon to remove them.
- https://docs.docker.com/storage/volumes/#remove-anonymous-volumes

When you mount a volume, it may be named or anonymous. Anonymous volumes are not given an explicit name when they are first mounted into a container, so Docker gives them a random name that is guaranteed to be unique within a given Docker host. Besides the name, named and anonymous volumes behave in the same ways.

## Best practices for writing Dockerfiles

[More here](./Best_practices_for_writing_Dockerfiles/Best_practices_for_writing_Dockerfiles.md).

- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#dockerfile-instructions