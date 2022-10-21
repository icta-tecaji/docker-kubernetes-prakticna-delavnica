# Docker Reliability And Health Checks

## Self-healing containers with restart policies

It’s often a good idea to **run containers with a restart policy**. This is a form of self-healing that enables Docker to **automatically restart them after certain events or failures** have occurred.

> Docker recommends that you use restart policies, and avoid using process managers to start containers. [Start containers automatically](https://docs.docker.com/config/containers/start-containers-automatically/)

Restart policies are **applied per-container**, and can be configured imperatively on the command line as part of `docker container run` commands, or declaratively in YAML files for use with higher-level tools such as Docker Swarm, Docker Compose, and Kubernetes.

The following restart policies exist:
- `no`: Do not automatically restart the container. (the default)
- `on-failure[:max-retries]`: Restart the container if it exits due to an error, which manifests as a non-zero exit code. Optionally, limit the number of times the Docker daemon attempts to restart the container using the `:max-retries` option.
- `always`: Always restart the container if it stops. If it is manually stopped, it is restarted only when Docker daemon restarts or the container itself is manually restarted.
- `unless-stopped`: Similar to always, except that when the container is stopped (manually or otherwise), it is not restarted even after Docker daemon restarts.

Start a new interactive container, with the `--restart always` policy, and tell it to run a sleep process.
- `docker container run -d --name test-restart --restart always nginx:1.23-alpine`
- `docker ps`
- Show running processes in container: `docker exec test-restart ps -a`
- Kill the PID 1 process: `docker exec test-restart kill 1`
- Docker will automatically restart it because it has the `--restart always` policy. If you issue a `docker
ps` command, you’ll see that the container’s uptime is less than the time since it was created.
- `docker ps`
- `docker exec test-restart ps -a`
- Be aware that Docker has restarted the same container and not created a new one. In fact, if you inspect it with docker container inspect you can see the RestartCount has been incremented.
- `docker container inspect test-restart | grep RestartCount`
- `docker rm -f test-restart`

The main difference between the always and unless-stopped policies is that containers with the --restart unless-stopped policy will not be restarted when the daemon restarts if they were in the Stopped (Exited)
state.

Create the two new containers:
- `docker container run -d --name always --restart always  alpine sleep 1d`
- `docker container run -d --name unless-stopped --restart unless-stopped alpine sleep 1d`
- `docker container ls`
- Stop both containers: `docker container stop always unless-stopped`
- `docker container ls -a`
- Restart Docker: `sudo systemctl restart docker`
- `docker container ls -a`
- Notice that the “always” container has been restarted, but the “unlessstopped” container has not.
- `docker rm -f always unless-stopped`

Keep the following in mind when using restart policies:
- A restart policy only takes effect after a container starts successfully. In this case, starting successfully means that the container is up for at least 10 seconds and Docker has started monitoring it. This prevents a container which does not start at all from going into a restart loop.
- If you manually stop a container, its restart policy is ignored until the Docker daemon restarts or the container is manually restarted. This is another attempt to prevent a restart loop.

## Using restart policies in Docker Compose
- docker compose restart

version: "3"
services:
myservice:
<Snip>
restart_policy:
condition: always | unless-stopped | on-failure

Pokažemo kako kontejner pade, in kako ga lahko resetiramo
- odkomentiramo //process.exit(0)
- dodamao v docker-compose  restart: on-failure
- pokažemo različne stop kode (npr, 1,2)








## Understanding PID 1 in Docker containers

An init system is a program that’s used to launch and maintain the state of other programs. Any process with PID 1 is treated like an init process by the Linux kernel (even if it is not technically an init system). In addition to other critical functions, an init system starts other processes, restarts them in the event that they fail, transforms and forwards signals sent by the operating system, and prevents resource leaks.

A process running as PID 1 inside a container is treated specially by Linux: it ignores any signal with the default action. As a result, the process will not terminate on SIGINT or SIGTERM unless it is coded to do so.
- Move to folder: `cd ~/docker-k8s/09_Docker_Reliability_And_Health_Checks/examples/01_app_no_signal_handling`
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
- `cd ~/docker-k8s/09_Docker_Reliability_And_Health_Checks/examples/02_app_with_signal_handling`
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
- Move to folder: `cd ~/docker-k8s/09_Docker_Reliability_And_Health_Checks/examples/03_app_entrypoint_problem/`
- `docker compose up --build`
- In the logs we can see that the script is waiting for the database to start.
- Open a new terminal window:
    - `cd ~/docker-k8s/09_Docker_Reliability_And_Health_Checks/examples/03_app_entrypoint_problem/`
    - `docker ps -a`
    - Look at the processes in the contianer: `docker exec app ps -aux`.  The `entrypoint.sh` shell script has PID 1, and our `app.py` Python program will have another PID. PID 1 processes in Linux do not have any default signal handlers and as a result will not receive and propogate signals. They are also expected to take on certain responsibilities, such as adopting orphaned processes, and reaping zombie processes.
    - Stop: `docker compose down`. The proccess don't shutdown gracefully.

We can try with the following solution:
- `cd ~/docker-k8s/09_Docker_Reliability_And_Health_Checks/examples/04_app_entrypoint/`
- The `entrypoint.sh` script uses the exec Bash command so that the final running application becomes the container’s PID 1. This allows the application to receive any Unix signals sent to the container.
- `docker compose up --build`
- Open a new terminal window:
    - `cd ~/docker-k8s/09_Docker_Reliability_And_Health_Checks/examples/04_app_entrypoint/`
    - `docker ps -a`
    - Look at the processes in the contianer: `docker exec app ps -aux`
    - Stop: `docker compose down`. The proccess shutdown gracefully.

## Docker Resource Management

Physical system resources such as memory and time on the CPU are scarce. If the resource consumption of processes on a computer exceeds the available physical resources, the processes will experience performance issues and may stop running.

**By default, a container has no resource constraints and can use as much of a given resource as the host’s kernel scheduler allows**. Docker provides ways to control how much memory, or CPU a container can use.

> On Ubuntu or Debian hosts you may see messages similar to the following when working with an image: `Your kernel does not support cgroup swap limit capabilities`. Follow the instruction [here](https://docs.docker.com/engine/install/linux-postinstall/#your-kernel-does-not-support-cgroup-swap-limit-capabilities). Memory and swap accounting incur an overhead of about 1% of the total available memory and a 10% overall performance degradation, even if Docker is not running.

- https://docs.docker.com/config/containers/resource_constraints/
- https://tbhaxor.com/docker-resource-management-in-detail/




## Building health checks into Docker images

In production you’ll run your apps in a container platform like Docker Swarm or Kubernetes, and those **platforms have features that help you deploy self-healing apps**. You can package your containers with information the platform uses to **check if the application inside the container is healthy**. If the app stops working correctly, the platform can remove a malfunctioning container and replace it with a new one.


## Starting containers with dependency checks


## Defining health checks and dependency checks in Docker Compose









## OTHER


- running processes as pid 1


- Sharing memory
- Understanding users
    - Working with the run-as user
