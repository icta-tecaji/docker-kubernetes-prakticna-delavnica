# Docker Reliability And Health Checks


## Self-healing containers with restart policies
Docker monitors the health of your app at a basic level every time you run a container. Containers run a specific process when they start and Docker **checks that the process is still running**, and if it stops, the container goes into the exited state. That gives you a basic health check that works across all environments. Developers can see that their app is unhealthy if the process fails and the container exits.

It’s often a good idea to **run containers with a restart policy**. This is a form of self-healing that enables Docker to **automatically restart them after certain events or failures** have occurred.

> Docker recommends that you use restart policies, and avoid using process managers to start containers. [Start containers automatically](https://docs.docker.com/config/containers/start-containers-automatically/)

Restart policies are **applied per-container**, and can be configured imperatively on the command line as part of `docker container run` commands, or declaratively in YAML files for use with higher-level tools such as Docker Swarm, Docker Compose, and Kubernetes.

The following restart policies exist:
- `no`: Do not automatically restart the container. (the default)
- `on-failure[:max-retries]`: Restart the container if it exits due to an error, which manifests as a non-zero exit code. Optionally, limit the number of times the Docker daemon attempts to restart the container using the `:max-retries` option.
- `always`: Always restart the container if it stops. If it is manually stopped, it is restarted only when Docker daemon restarts or the container itself is manually restarted.
- `unless-stopped`: Similar to always, except that when the container is stopped (manually or otherwise), it is not restarted even after Docker daemon restarts.

Start a new interactive container, with the `--restart always` policy, and tell it to run a sleep process.
- `sudo docker container run -d --name test-restart --restart always nginx:1.23-alpine`
- `sudo docker ps`
- Show running processes in container: `sudo docker exec test-restart ps -a`
- Kill the PID 1 process: `sudo docker exec test-restart kill 1`
    - Docker will automatically restart it because it has the `--restart always` policy. If you issue a `docker
ps` command, you’ll see that the container’s uptime is less than the time since it was created.
- `sudo docker ps`
- `sudo docker exec test-restart ps -a`
- Be aware that Docker has restarted the same container and not created a new one. In fact, if you inspect it with docker container inspect you can see the RestartCount has been incremented.
- `sudo docker container inspect test-restart | grep RestartCount`
- `sudo docker rm -f test-restart`

The main difference between the always and unless-stopped policies is that containers with the --restart unless-stopped policy will not be restarted when the daemon restarts if they were in the Stopped (Exited)
state.

Create the two new containers:
- `sudo docker container run -d --name always --restart always  alpine sleep 1d`
- `sudo docker container run -d --name unless-stopped --restart unless-stopped alpine sleep 1d`
- `sudo docker ps`
- Stop both containers: `sudo docker container stop always unless-stopped`
- `sudo docker ps -a`
- Restart Docker: `sudo systemctl restart docker`
- `sudo docker ps -a`
    - Notice that the “always” container has been restarted, but the “unlessstopped” container has not.
- `sudo docker rm -f always unless-stopped`

Keep the following in mind when using restart policies:
- A restart policy only takes effect after a container starts successfully. In this case, starting successfully means that the container is up for at least 10 seconds and Docker has started monitoring it. This prevents a container which does not start at all from going into a restart loop.
- If you manually stop a container, its restart policy is ignored until the Docker daemon restarts or the container is manually restarted. This is another attempt to prevent a restart loop.

## Using restart policies in Docker Compose

Docker Compose allows us to configure restart policies to manage multiple containers by using the restart keyword. `restart` defines the policy that the platform will apply on container termination.
- `no`: The default restart policy. Does not restart a container under any circumstances.
- `always`: The policy always restarts the container until its removal.
- `on-failure`: The policy restarts a container if the exit code indicates an error.
- `unless-stopped`: The policy restarts a container irrespective of the exit code but will stop restarting when the service is stopped

Try the following:
- Move to folder: `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/00_restart_polcy`
- Check the `docker-compose.yml` file.
- Run the app: `docker compose up --build`
    - The container restarts after the error.
- Stop the app: `docker compose down`
- Change the `restart` filed to `on-failure` in the `docker-compose.yml` file.
- Run the app: `docker compose up --build`
- Check: `docker compose ps` and `docker compose logs -f`.
    - The app is restarting
- Stop the app: `docker compose down`
- Uncomment the `sys.exit(0)` line in the `app.py` file.
- Run the app: `docker compose up --build`
- Check: `docker compose ps` and `docker compose logs`.
    - The container exited and stopped (no restart).
- Stop the app: `docker compose down`

## Understanding PID 1 in Docker containers

An init system is a program that’s used to launch and maintain the state of other programs. Any process with PID 1 is treated like an init process by the Linux kernel (even if it is not technically an init system). In addition to other critical functions, an init system starts other processes, restarts them in the event that they fail, transforms and forwards signals sent by the operating system, and prevents resource leaks.

A process running as PID 1 inside a container is treated specially by Linux: it ignores any signal with the default action. As a result, the process will not terminate on SIGINT or SIGTERM unless it is coded to do so.
- Move to folder: `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/01_app_no_signal_handling`
- Build the image: `docker build -t pid-01 .`
- Run: `docker run -d --name pid-01 pid-01`
- Look at the logs: `docker logs pid-01 -f`
- `docker ps`
- We are running Python as PID 1: `docker exec pid-01 ps -a`
- Send a SIGTERM (15) signal to a process: `docker exec pid-01 kill -15 1` (the process will not terminate)
- `docker ps`
- Try to stop the container: `docker stop pid-01`. It's takes 10s to stop the contianer. The main process inside the container will receive `SIGTERM`, and after a grace period, `SIGKILL`. The default grace period (seconds to wait for stop before killing it) is 10s. It's can be changed with the `-t` flag.
- `docker rm pid-01`

We added some signal handling in the next example: 
- `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/02_app_with_signal_handling`
- Build the image: `docker build -t pid-02 .`
- Run: `docker run -d --name pid-02 pid-02`
- `docker ps`
- We are running Python as PID 1: `docker exec pid-02 ps -a`
- Run the logs in a **different terminal window**: `docker logs pid-02 -f`
- Send a SIGTERM (15) signal to a process: `docker exec pid-02 kill -15 1` (the proccess shutdown gracefully)
- `docker ps -a`
- `docker rm pid-02`
- Run: `docker run -d --name pid-02 pid-02`
- Run the logs in a **different terminal window**: `docker logs pid-02 -f`
- Try to stop the container: `docker stop pid-02` (the container shutdown immediately)
- `docker rm pid-02`

The ENTRYPOINT instruction can also be used in combination with a helper script, allowing it to function in a similar way to the command above, even when starting the tool may require more than one step. For example we can use the `entrypoint.sh` to verify that Postgres is up and healthy before creating our app. 
- Move to folder: `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/03_app_entrypoint_problem/`
- `docker compose up --build`
- In the logs we can see that the script is waiting for the database to start.
- Open a new terminal window:
    - `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/03_app_entrypoint_problem/`
    - `docker ps -a`
    - Look at the processes in the contianer: `docker exec app ps -aux`.  The `entrypoint.sh` shell script has PID 1, and our `app.py` Python program will have another PID. PID 1 processes in Linux do not have any default signal handlers and as a result will not receive and propogate signals. They are also expected to take on certain responsibilities, such as adopting orphaned processes, and reaping zombie processes.
    - Stop: `docker compose down`. The proccess don't shutdown gracefully.

We can try with the following solution:
- `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/04_app_entrypoint/`
- The `entrypoint.sh` script uses the exec Bash command so that the final running application becomes the container’s PID 1. This allows the application to receive any Unix signals sent to the container.
- `docker compose up --build`
- Open a new terminal window:
    - `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/04_app_entrypoint/`
    - `docker ps -a`
    - Look at the processes in the contianer: `docker exec app ps -aux`
    - Stop: `docker compose down`. The proccess shutdown gracefully.

## Docker Resource Management (Advanced)

Physical system resources such as memory and time on the CPU are scarce. If the resource consumption of processes on a computer exceeds the available physical resources, the processes will experience performance issues and may stop running.

**By default, a container has no resource constraints and can use as much of a given resource as the host’s kernel scheduler allows**. Docker provides ways to control how much memory, or CPU a container can use.

Many of these features require your kernel to support Linux capabilities.

> On Ubuntu or Debian hosts you may see messages similar to the following when working with an image: `Your kernel does not support cgroup swap limit capabilities`. Follow the instruction [here](https://docs.docker.com/engine/install/troubleshoot/#kernel-cgroup-swap-limit-capabilities). Memory and swap accounting incur an overhead of about 1% of the total available memory and a 10% overall performance degradation, even if Docker is not running.

- [Runtime options with Memory, CPUs, and GPUs](https://docs.docker.com/config/containers/resource_constraints/)
- [resources](https://docs.docker.com/compose/compose-file/deploy/#resources) configures physical resource constraints for container to run on platform.
- [Docker Resource Management in Detail](https://tbhaxor.com/docker-resource-management-in-detail/)


## Building health checks into Docker images

In production you’ll run your apps in a container platform like Docker Swarm or Kubernetes, and those **platforms have features that help you deploy self-healing apps**. You can package your containers with information the platform uses to **check if the application inside the container is healthy**. If the app stops working correctly, the platform can remove a malfunctioning container and replace it with a new one.

Checking if the container exits it’s a very basic check — it ensures the process is running, but **not that the app is actually healthy**. A web app in a container could hit maximum capacity and start returning HTTP 503 “Service Unavailable” responses to every request, but as long as the process in the container is still running, Docker thinks the container is healthy, even though the app is stalled.

> The health check is an ongoing test that helps the container platform keep your application running.

Docker gives you a neat way to build a real application health check right into the Docker image, just by adding logic to the Dockerfile. We’ll do that with a simple API container, but first we’ll run it without any health checks to be sure we understand the problem.

Run a container that hosts a simple REST API that returns a random number. The app has a bug, so after few calls to the API, it becomes unhealthy and every subsequent call fails.
- Move to: `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/05_rnd_number`
- Look at the files
- Build the image: `docker build -t random-number-api .`
- Run the app: `docker container run -d --name rnd-api -p 80:5000 random-number-api`
- Check the container status: `docker ps`
- Run it multiple time from terminal: 
    - `curl -i http://localhost/health`
    - `curl -i http://localhost/rng` (run 5x)
    - `curl -i http://localhost/health`
    - The API behaves correctly for the first five calls, and then it returns an HTTP 500 “Internal Server Error” response.
- Check the container status: `docker ps`
    - In the container list, the API container has the status Up.
    - The process inside the container is still running, so it looks good as far as Docker is concerned. The container runtime has no way of knowing what’s happening inside that process and whether the app is still behaving correctly.
- Stop and remove the app: `docker rm -f rnd-api`

Enter the `HEALTHCHECK` instruction, which you can add to a Dockerfile to tell the runtime exactly how to check whether the app in the container is still healthy. The `HEALTHCHECK` instruction **specifies a command for Docker to run inside the container**, which will return a status code—the command can be anything you need to check if your app is healthy. Docker will run that command in the container at a timed interval. 
- If the status code says everything is good, then the container is healthy.
- If the status code is a failure several times in a row, then the container is marked as unhealthy.

> [The `HEALTHCHECK`](https://docs.docker.com/engine/reference/builder/#healthcheck) instruction tells Docker how to test a container to check that it is still working. This can detect cases such as a web server that is stuck in an infinite loop and unable to handle new connections, even though the server process is still running.

Add the `HEALTHCHECK` command in a new Dockerfile for the random
number API. This health check uses a curl command like I did on my host, but this time it runs inside the container. The `/health` URL is another endpoint in the application that checks if the bug has been triggered; it will return a 200 “OK” status code if the app is working and a 500 “Internal Server Error” when it’s broken.

The health check makes an HTTP call to the /health endpoint, which the API provides to test if the app is healthy. Using the `--fail` parameter means the curl command will pass the status code on to Docker — if the request succeeds, it returns the number 0, which Docker reads as a successful check. If it fails, it returns a number other than 0, which means the health check failed.

You can configure how often the health check runs and how many failed checks mean the app is unhealthy. The default is to run every 30 seconds, and for three failures in a row to trigger the unhealthy status.
The options that can appear before CMD are:
- `--interval=DURATION` (default: 30s): The health check will first run interval seconds after the container is started, and then again interval seconds after each previous check completes.
- `--timeout=DURATION` (default: 30s): If a single run of the check takes longer than timeout seconds then the check is considered to have failed.
- `--start-period=DURATION` (default: 0s): start period provides initialization time for containers that need time to bootstrap. Probe failure during that period will not be counted towards the maximum number of retries.
- `--retries=N` (default: 3): It takes retries consecutive failures of the health check for the container to be considered unhealthy.

Run the same test but using the new image:
- Look at the files
- Build the app: `docker build -t random-number-api-health -f Dockerfile.health .`
- Run the app: `docker container run -d --name rnd-api-health -p 80:5000 random-number-api-health`
- Wait 30 seconds or so and list the containers: `docker ps`
    - You can see that the new version of the API container initially shows a healthy status.
- Run it multiple time from terminal: 
    - `curl -i http://localhost/health`
    - `curl -i http://localhost/rng` (run 5x)
    - `curl -i http://localhost/health`
- Run: `docker ps`
    - That **unhealthy status** is published as an event from Docker’s API, so the platform running the container is notified and can take action to fix the application.
- Docker also records the result of the most recent health checks, which you can see when you inspect the container: `docker container inspect rnd-api-health`
- Stop and remove the app: `docker rm -f rnd-api-health`

The health check is doing what it should: testing the application inside the container and flagging up to Docker that the app is no longer healthy.

**Why hasn’t Docker restarted or replaced that container?** 
- Docker can’t safely do that, because the Docker Engine is running on a single server. 
- Docker could stop and restart that container, but that would mean downtime for your app while it was being recycled. Or Docker could remove that container and start a new one from the same setup, but maybe your app writes data inside the container, so that would mean downtime and a loss of data.
- Docker can’t be sure that taking action to fix the unhealthy container won’t make the situation worse, so it broadcasts that the container is unhealthy but leaves it running.
- Health checks **become really useful in a cluster with multiple servers running Docker being managed by Docker Swarm or Kubernetes**.

## Starting containers with dependency checks

Running across a cluster brings new challenges for distributed apps, because you can no longer **control the startup order for containers that may have dependencies on each other**.

In a clustered container platform, however, **you can’t dictate the startup order** of the containers, so for example the web app might start before the API is available. What happens then depends on your application.

Then run the web app container and browse to it. The container is up and the app is available, but you’ll find it doesn’t actually work.
- Move to folder: `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/06_rnd_number_web`
- Build the web container: `docker build -t random-number-web .`
- Create a network: `docker network create --attachable rnd-net`
- Run the web container: `docker run -d -p 80:5000 --network rnd-net --name rnd-number-web random-number-web`
- `docker ps`
- Try to open the webpage. You’ll see a simple web app that looks OK, but the number service is unavailable.
    - This is exactly what you don’t want to happen. The container looks fine, but the app is unusable because its key dependency is unavailable. Some apps may have logic built into them to verify that the dependencies they need are there when they start, but most apps don’t, and the random number web app is one of those. It assumes the API will be available when it’s needed, so it doesn’t do any dependency checking.
- Stop the container: `docker rm -f rnd-number-web`

You can add that **dependency check inside the Docker image**. A dependency
check is different from a health check — **it runs before the application starts and makes sure everything the app needs is available.**
    - If everything is there, the dependency check finishes successfully and the app starts. 
    - If the dependencies aren’t there, the check fails and the container exits
    
Docker doesn’t have a built-in feature like the `HEALTHCHECK` instruction for dependency checks, but you can put that logic in the startup command.
- Look at the `Dockerfile.check` file.
- Build the image: `docker build -t random-number-web-check -f Dockerfile.check .`
- Run the container: `docker run -p 80:5000 --network rnd-net --name rnd-number-web-check random-number-web-check`
- `docker ps -a`
- The CMD instruction runs when a container starts, and it makes an HTTP call to the API, which is a simple check to make sure it’s available. 
    - If the API is available, the curl command will succeed and the application gets launched.
    - If the API is unavailable, the curl command will fail, the command won’t run, and nothing happens in the container so it exits.
- `docker rm -f rnd-number-web-check`
- `docker network rm rnd-net`

It’s counterintuitive, but in this scenario it’s **better to have an exited container than a running container.**

This is fail-fast behavior, and it’s what you want when you’re running at scale. When a container exits, the platform can schedule a new container to come up and replace it.

Curl is a very useful tool for testing web apps and APIs. Any extra tools increase the image size, and they also increase the frequency of updates and the security attack surface. So although curl is a great tool for getting started with container checks, it’s better to **write a custom utility for your checks using the same language that your application uses.**

There are a whole lot of advantages to this:
- You reduce the software requirements in your image
- You can use more complex conditional logic in your checks
- Your utility can use the same application configuration that your app uses
- You can execute any tests you need
- It makes your image portable between different container platforms

## Defining health checks and dependency checks in Docker Compose

Docker Compose can go some of the way toward repairing unreliable applications, but it won’t replace unhealthy containers for the same reasons that Docker Engine won’t: you’re running on a single server, and the fix might cause an outage. But it can **set containers to restart if they exit**, and it can **add a health check if there isn’t one already in the image**.

Specifying health check parameters in a Docker Compose file:
- Move to: `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/07_number_compose/`
- Check the `docker-compose.yml` file
    - You have fine-grained control over the health check. 
    - You can also add a health check in your Compose file for containers that don’t have one declared in the image.
    - It’s good to add a health check to all containers, but this example comes together with the dependency check in the image and the `restart: on-failure` setting, which means that if the container exits unexpectedly, Docker will restart it.
- Start the app: `docker compose up -d`
    - Compose creates both containers at the same time, because no dependencies are specified.
    - You can see in my logs that the HTTP check returns a success code.
    - The web service is configured to restart on failure, so that same container gets started again.
- `docker compose ps`
- `docker compose logs -f`
- `docker compose ps`
- Stop the app: `docker compose down`

Why bother **building a dependency check into the container startup when Docker Compose can do it for you with the `depends_on` flag**?
- Compose can only manage dependencies on a single machine, and the startup behavior of your app on a production cluster is far less predictable.

> Building your app as a distributed system with lots of small components increases your flexibility and agility, but it does make management more complicated.

You do need to be **careful with your checks** though. Health checks run **periodically**, so they shouldn’t do too much work. You need to find the **balance** so checks are testing that key parts of your app are working without taking too long to run or **using too much compute resource**.

