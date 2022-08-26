# Sharing Docker Images



The image name is diamol/ch03-web-ping, and it’s stored on Docker Hub, which is
the default location where Docker looks for images. Image servers are called registries,
and Docker Hub is a public registry you can use for free. Docker Hub also has a
web interface, and you’ll find details about this image at https://hub.docker.com/r/
diamol/ch03-web-ping.

## Public and private software distribution
The methods included in the spectrum range from hosted registries such as Docker
Hub to totally custom distribution architectures or source-distribution methods. We
cover some of these subjects in more detail than others. We also place particular focus
on private registries because they provide the most balance between the two concerns.
### Publishing with hosted registries
As a reminder, Docker registries are **services that make repositories accessible to
Docker pull commands**. A registry hosts repositories. The simplest way to distribute
your images is by using **hosted registries**.
A hosted registry is a Docker registry service that’s owned and operated by a thirdparty
vendor. Docker Hub, Quay.io, and Google Container Registry are all examples
of hosted registry providers. By default, Docker publishes to Docker Hub. Docker
Hub and most other hosted registries provide both public and private registries, as
shown in figure 9.2.
#### Publishing with public repositories: “Hello World!” via Docker Hub
The simplest way to get started with public repositories on hosted registries is to push
a repository that you own to Docker Hub. To do so, all you need is a Docker Hub
account and an image to publish. If you haven’t done so already, sign up for a Docker
Hub account now.

Once you have your account, you need to create an image to publish. Create a new
Dockerfile named HelloWorld.df and add the following instructions:
    FROM busybox:latest
    CMD echo 'Hello World!'
Chapter 8 covers Dockerfile instructions. As a reminder, the FROM instruction tells the
Docker image builder which existing image to start the new image from. The CMD
instruction sets the default command for the new image. Containers created from this
image will display Hello World! and exit. Build your new image with the following
command:
    docker image build \
        -t leon11sj/hello-dockerfile \
        -f HelloWorld.df \
        .
Be sure to substitute your Docker Hub username in that command. Authorization to
access and modify repositories is based on the username portion of the repository
name on Docker Hub. If you create a repository with a username other than your
own, you won’t be able to publish it.

Publishing images on Docker Hub with the docker command-line tool requires
that you establish an authenticated session with that client. You can do that with the
login command:
    
    docker login
This command will prompt you for your username, email address, and password. Each
of those can be passed to the command as arguments using the --username, --email,
and --password flags. When you log in, the docker client maintains a map of your credentials
for the different registries that you authenticate with in a file. It will specifically
store your username and an authentication token, not your password.

You will be able to push your repository to the hosted registry after you’ve logged
in. Use the docker push command to do so:
    docker image push leon11sj/hello-dockerfile
The command output includes upload statuses and the resulting repository content
digest. The push operation will create the repository on the remote registry, upload
each of the new layers, and then create the appropriate tags.

Your public repository will be available to the world as soon as the push operation
is completed. Verify that this is the case by searching for your username and your new
repository. For example, use the following command to find the example owned by
the dockerinaction user:
    
    docker search leon11sj
Replace the dockerinaction username with your own to find your new repository on
Docker Hub. You can also log in to the Docker Hub website and view your repositories
to find and modify your new repository.
Having distributed your first image with Docker Hub, you should consider how
this method measures up to the selection criteria;
Public repositories on hosted registries are the best choice for owners of open source
projects or people who are just getting started with Docker. People should still be
skeptical of software that they download and run from the internet, so public repositories
that don’t expose their sources can be difficult for some users to trust. Hosted
(trusted) builds solve this problem to a certain extent.
### Private hosted repositories
Private repositories are similar to public repositories from an operational and product
perspective. Most registry providers offer both options, and any differences in provisioning
through their websites will be minimal. Because the Docker registry API
makes no distinction between the two types of repositories, registry providers that
offer both generally require you to provision private registries through their website,
app, or API.
The tools for working with private repositories are identical to those for working
with public repositories, with one exception. Before you can use docker image pull or
docker container run to install an image from a private repository, you need to
authenticate with the registry where the repository is hosted. To do so, you use the
docker login command just as you would if you were using docker image push to
upload an image.
### Introducing private registries
When you have a hard requirement on availability control, longevity control, or
secrecy, then running a private registry may be your best option. In doing so, you gain
control without sacrificing interoperability with Docker pull and push mechanisms or
adding to the learning curve for your environment. People can interact with a private
registry exactly as they would with a hosted registry.
Many free and commercially supported software packages are available for running a
Docker image registry. If your organization has a commercial artifact repository for
operating system or application software packages, it probably supports the Docker
image registry API. A simple option for running a nonproduction image registry is to
use Docker’s registry software. The Docker registry, called Distribution, is open source
software and distributed under the Apache 2 license. The availability of this software
and permissive license keep the engineering cost of running your own registry low. Figure
9.3 illustrates that private registries fall in the middle of the distribution spectrum.
The biggest trade-off when going from hosted registries to private registries is gaining
flexibility and control while requiring greater depth and breadth of engineering experience
to build and maintain the solution. Docker image registries often consume
large amounts of storage, so be sure to account for that in your analysis. The remainder
of this section covers what you need in order to implement all but the most complicated
registry deployment designs and highlights opportunities for customization
in your environment.