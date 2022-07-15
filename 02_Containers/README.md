# Containers

## Containers History
- **Applications are at the heart of businesses**. If applications break, businesses break.
- Most applications run on servers. **In the past we could only run one application per server**.
    - Windows and Linux just didn’t have the tenologies to safely and securely run multiple applications on the same server.
- Every time the business needed a new application, the IT department would **buy a new server**. Most of the time **nobody knew the performance requirements** of the new application, forcing the IT department to make guesses when choosing the model and size of the server to buy.
- This resulted in over-powered servers operating as low as 5-10% of their potential capacity. A **tragic waste of company capital and environmental resources**.

### Virtual Machines
- VMware, Inc. gave the world a gift - the virtual machine (VM). IT departments no longer needed to procure a brand-new oversized server every time the business needed a new application.
- VMs aren't perfect:
    - Every VM requires its own dedicated operating system (OS).
    - Every OS consumes CPU, RAM and other resources that could otherwise be used to power more applications.
    - Every OS needs patching and monitoring.
    - And in some cases, every OS requires a license.
    - VMs are slow to boot, and portability isn’t great — migrating and moving VM workloads between hypervisors and cloud platforms is harder than it needs to be.
    - Results in wasted time and resources.

### Linux containers
- For a long time, the big web-scale players, like Google, have been using container technologies to address the shortcomings of the VM model.
- In the container model, the container is roughly analogous to the VM. A major difference is that **containers do not require their own full-blown OS**. In fact, all containers on a single host share the host’s OS. This frees up huge amounts of system resources such as CPU, RAM, and storage. It also reduces potential licensing costs and reduces the overhead of OS patching and other maintenance.
- **Containers are also fast to start and ultra-portable**. Moving container workloads from your laptop, to the cloud, and then to VMs or bare metal in your data center is a breeze.
- Modern containers started in the Linux world and are the product of an immense amount of work from a wide variety of people over a long period of time.
- Some of the major technologies that enabled the massive growth of containers in recent years include; kernel namespaces, control groups, union filesystems, and of course Docker.

> There are many operating system virtualization tenologies similar to containers that predate Docker and modern containers. Some even date back to System/360 on the Mainframe. BSD Jails and Solaris Zones are some other well-known examples of Unix-type container technologies.

- But for now, it’s enough to say that Docker was the magic that made Linux containers usable. Put another way, Docker, Inc. made containers simple!

## Conatiners vs Virtual Machines







NP DDD - 51















- ugašanje kontejnerja
- procesi v kontejnerju
- Attaching to running containers

- Starting a new container (advanced)