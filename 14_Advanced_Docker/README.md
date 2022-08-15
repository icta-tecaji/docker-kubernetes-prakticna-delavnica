Containers and isolation features have existed for decades. Docker uses Linux namespaces
and cgroups, which have been part of Linux since 2007. 

Docker builds containers using 10 major system features. Part 1 of this book uses
Docker commands to illustrate how these features can be modified to suit the needs
of the contained software and to fit the environment where the container will run.
The specific features are as follows:
- PID namespace—Process identifiers and capabilities
- UTS namespace—Host and domain name
- MNT namespace—Filesystem access and structure
- IPC namespace—Process communication over shared memory
- NET namespace—Network access and structure
- USR namespace—User names and identifiers
- chroot syscall—Controls the location of the filesystem root
- cgroups—Resource protection
- CAP drop—Operating system feature restrictions
- Security modules—Mandatory access controls