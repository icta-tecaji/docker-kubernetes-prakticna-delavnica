# Building Images






https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#dockerfile-instructions


## VOLUME command
However, it’s also possible to deploy volumes via Doerfiles using the VOLUME instruction. The format is VOLUME `<container-mount-point>`. Interestingly, you cannot specify a directory on the host when defining a volume in a Dockerfile. is is because host directories are different depending on what OS your Doer host is running
– it could break your builds if you specified a directory on a Doer host that doesn’t exist. As a result, defining
a volume in a Doerfile requires you to specify host directories at deploy-time.

Anonymous volumes have no specific source so when the container is deleted, instruct the Docker Engine daemon to remove them.
- https://docs.docker.com/storage/volumes/#remove-anonymous-volumes

When you mount a volume, it may be named or anonymous. Anonymous volumes are not given an explicit name when they are first mounted into a container, so Docker gives them a random name that is guaranteed to be unique within a given Docker host. Besides the name, named and anonymous volumes behave in the same ways.

## Best practices for writing Dockerfiles

[More here](./Best_practices_for_writing_Dockerfiles/Best_practices_for_writing_Dockerfiles.md).