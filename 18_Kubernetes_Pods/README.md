# Kubernetes Pods

## Pod theory
- The atomic unit of scheduling in the virtualization world is the **Virtual Machine (VM)**. This means deploying applications in the virtualization world is done by scheduling them on VMs.
- In the Docker world, the atomic unit is the **container**. This means deploying applications on Docker is done by scheduling them inside of containers.
- In the Kubernetes world, the atomic unit is the **Pod**. Ergo, deploying applications on Kubernetes means stamping them out in Pods.

A Pod is the **basic execution unit of a Kubernetes application–the smallest and simplest unit in the Kubernetes object model that you create or deploy**. - A Pod represents processes running on your Cluster.
- Kubernetes wraps the container in the Pod.
- A Pod is a unit of compute, which runs on a **single node** in the cluster.
- A Pod is a shared execution environment for **one or more containers**.


## Understanding pods
Pod is a co-located group of containers and the basic building block in Kubernetes.

You normally run a single container in a Pod, but you can run multiple containers in one Pod, which opens up some interesting deployment options.

When a pod has multiple containers, **all of them run on the same worker node — a single pod instance never spans multiple nodes**.

![All containers of a pod run on the same node. A pod never spans multiple nodes.](./images/img02.png)
<!-- Vir: https://livebook.manning.com/book/kubernetes-in-action-second-edition/chapter-5/v-14/12 -->


### One container shouldn’t contain multiple processes
Imagine an application that consists of several processes that communicate with each other via IPC (Inter-Process Communication) or shared files, which requires them to run on the same computer. You can run all the processes that make up an application in just one container, but that makes the container **very difficult to manage**.

Containers are **designed to run only a single process**, not counting any child processes that it spawns (problems - loggging to standard output, container runtime only restarts the container when the container’s root process dies). Both container tooling and Kubernetes were developed around this fact.
- Problems with logging to the standard output.
- Container runtime only restarts the container when the container’s root process dies.

### How a pod combines multiple containers
With a pod, you can run closely related processes together, giving them (almost) the same environment as if they were all running in a single container.

All containers in a pod **share the same Network namespace** and thus the network interfaces, **IP address(es) and port space** that belong to it.

![Containers in a pod share the same network interfaces](./images/img03.png)
<!-- Vir: https://livebook.manning.com/book/kubernetes-in-action-second-edition/chapter-5/v-14/12 -->

- Processes running in containers of the same pod can’t be bound to the same port numbers.
- All the containers in a pod also see the **same system hostname**, because they share the UTS namespace, and can **communicate through the usual IPC mechanisms** because they share the IPC namespace.
- A pod **can also be configured to use a single PID namespace** for all its containers, which makes them share a single process tree, but you must explicitly enable this for each pod individually.

> When containers of the same pod use separate PID namespaces, they can’t see each other or send
process signals like SIGTERM or SIGINT between them.

- Each container always has its own Mount namespace, giving it **its own file system**, but when two containers must share a part of the file system, you can add a volume to the pod and mount it into both containers

### Splitting a multi-tier application stack into multiple pods
- You typically run only one application in each pod.
- You never need to combine multiple applications in a single pod, as pods **have almost no resource overhead**.

Imagine a simple system composed of a **front-end web server and a back-end database**. You shouldn’t run them in the same pod:
- If you have a two-node cluster and only create this one pod, you are using only a single worker node and aren’t **taking advantage of the computing resources** available on the second node. This means wasted CPU, memory, disk storage and bandwidth.
- **Splitting into multiple pods to enable individual scaling**: A pod is a basic unit of scaling. Kubernetes doesn’t replicate containers within a pod. It replicates the entire pod. If a container has to be scaled separately from the other components, this is a clear indication that it must be deployed in a separate pod.

![Splitting an application stack into pods](./images/img04.png)
<!-- Vir: https://livebook.manning.com/book/kubernetes-in-action-second-edition/chapter-5/v-14/12 -->

## Sidecar containers
Placing several containers in a single pod is only appropriate if the application consists of a primary process and one or more processes that complement the operation of the primary process. **The container in which the complementary process runs is called a sidecar container**.

![A pod with a primary and sidecar container(s)](./images/img05.png)
<!-- Vir: https://livebook.manning.com/book/kubernetes-in-action-second-edition/chapter-5/v-14/12 -->

Examples:
- A reverse proxy that converts HTTPS traffic to HTTP
![A sidecar container that converts HTTPS traffic to HTTP](./images/img06.png)
<!-- Vir: https://livebook.manning.com/book/kubernetes-in-action-second-edition/chapter-5/v-14/12 -->
- A sidecar container that delivers content to the web server container via a volume. The other container in the pod is an agent that periodically downloads content from an external source and stores it in the web server’s webroot directory. 
![A sidecar container that delivers content to the web server container via a volume](./images/img07.png)
<!-- Vir: https://livebook.manning.com/book/kubernetes-in-action-second-edition/chapter-5/v-14/12 -->
- Other examples of sidecar containers are log rotators and collectors, data processors, communication adapters, and others.

When deciding whether to use the sidecar pattern and place containers in a single pod, or to place them in separate pods, ask yourself the following questions:
- Do these containers have to run on the same host?
- Do I want to manage them as a single unit?
- Do they form a unified whole instead of being independent components?
- Do they have to be scaled together?
- Can a single node meet their combined resource needs?

If the answer to all these questions is yes, put them all in the same pod. As a rule of thumb, **always place containers in separate pods unless a specific reason requires them to be part of the same pod.**

## Creating pods
Pods and other Kubernetes objects are usually created by creating a JSON or YAML manifest file and posting it to the Kubernetes API.

> The decision whether to use YAML or JSON to define your objects is yours. Most people prefer to use
YAML because it’s slightly more human-friendly and allows you to add comments to the object definition.

By using YAML files to define the structure of your application, you don’t need shell scripts to
make the process of deploying your applications repeatable, and you can **keep a history of all
changes** by storing these files in a VCS (Version Control System).

### Creating a YAML manifest for a pod
Now create an object manifest from scratch.
- `cd docker-k8s/18_Kubernetes_Pods/examples/`
- `cat 01_example.yaml`

After you’ve prepared the manifest file for your pod, you can now create the object by posting the file to the Kubernetes API.

When you post the manifest to the API, you are directing Kubernetes to apply the manifest to the cluster.
- `kubectl apply -f 01_example.yaml`

The `kubectl apply` command is used for creating objects as well as for making changes to existing objects.

> If you later decide to make changes to your pod object, you can simply edit the file and run the apply command again. Some of the pod’s fields aren’t mutable, so the update may fail, but you can always delete the pod and then create it again.
- `kubectl get pod myapp -o yaml`

Let’s use the basic kubectl commands to see how the pod is doing:
- `kubectl get pod`
- `kubectl get pod -o wide`
- `kubectl describe pod myapp`

The following listing shows all the events that were logged after creating the pod.
- `kubectl get events`

No warning events are displayed, so everything seems to be fine.

Let’s confirm that the application running in the container
responds to your requests.

For development, testing and debugging purposes, you may want to
communicate directly with a specific pod, rather than using a service that forwards connections to randomly selected pods.

You’ve learned that each pod is assigned its own IP address where it can be accessed by every other pod in the cluster. This IP address is typically internal to the cluster. You can’t access it from your local computer, except when Kubernetes is deployed in a specific way.
1. GETTING THE POD’S IP ADDRESS:
    - You can get the pod’s IP address by retrieving the pod’s full YAML and searching for the podIP field in the status section.
    - `kubectl get pod myapp -o wide`
2. GETTING THE PORT THE APPLICATION IS BOUND TO:
    - If I wasn’t the author of the application, it would be difficult for me to find out which port the application listens on. I could inspect its source code or the Dockerfile of the container image, as the port is usually specified there, but I might not have access to either.
    - Fortunately, you can specify a list of ports in the pod definition itself. It isn’t necessary to specify any ports, but it is a good idea to always do so.
    - The pod manifest says that the container uses port 8080, so you now have everything you need to talk to the application.
3. CONNECTING TO THE POD FROM THE WORKER NODES:
    - The Kubernetes network model dictates that each pod is accessible from any other pod and that each node can reach any pod on any node in the cluster.
    - Once you have logged into the node, use the curl command with the pod’s IP and port to access your application.
    - `curl <IP>:8080`
    - Normally you don’t use this method to talk to your pods, but you may need to use it if there
are communication issues and you want to find the cause by first trying the shortest possible
communication route.
4. CONNECTING FROM A ONE-OFF CLIENT POD:
    - The second way to test the connectivity of your application is to run curl in another pod that you create specifically for this task.
    - Creating a pod just to see if it can access another pod is useful when you’re specifically testing pod-to-pod connectivity.
    - `kubectl run --image=curlimages/curl -it --restart=Never --rm client-pod curl <IP>:8080`
5. CONNECTING TO PODS VIA KUBECTL PORT FORWARDING:
    - During development, the easiest way to talk to applications running in your pods is to use the `kubectl port-forward` command, which allows you to communicate with a specific pod through a proxy bound to a network port on your local computer.
    - To open a communication path with a pod, you don’t even need to look up the pod’s IP, as you only need to specify its name and the port.
    - `kubectl port-forward myapp 8080`
    - The proxy now waits for incoming connections. Run the following curl command in another terminal: `curl localhost:8080`

![proxy bound to a network port](./images/img08.png)
<!-- Vir: https://livebook.manning.com/book/kubernetes-in-action-second-edition -->





