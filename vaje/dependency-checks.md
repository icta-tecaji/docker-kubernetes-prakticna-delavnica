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
- Move to: `cd ~/docker-kubernetes-prakticna-delavnica/09_Docker_Reliability_And_Health_Checks/examples/06_number_compose/`
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