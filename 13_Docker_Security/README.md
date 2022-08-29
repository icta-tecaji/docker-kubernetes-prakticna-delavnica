# Docker Security


## Container security
- https://snyk.io/learn/container-security/
- https://snyk.io/blog/secure-your-kubernetes-applications-with-snyk-container/
- https://snyk.io/blog/snyk-container-registry-security-integrations-github-gitlab-nexus-digitalocean/
-https://snyk.io/learn/container-security/container-monitoring/

Vulnerabilities can be introduced to containers in a number of ways: 
- from the software inside the container, 
- how the container interacts with the host operating system and adjacent containers, 
- the configurations for networking and storage
- from other images that your containers rely on
    - your container image may be based on a publicly available image that contains known vulnerabilities and malware, especially if you didn’t download the image from a verified publisher and authenticate the image publisher and contents


## Container scanning

Container scanning, or container image scanning, is the process and scanning tools used to identify vulnerabilities within containers and their components. It’s key to container security, and enables developers and cybersecurity teams to fix security threats in containerized applications before deployment.

**A container scanner is an automated tool that analyzes these various container components to detect security vulnerabilities.**

Security scanners can be **integrated during various stages of development**:
- scan potential parent images from your desktop before deciding which one to use as the base for your image
- using IDE plugins
- integrate container vulnerability scanning into the continuous integration and continuous delivery (CI/CD)
- monitor containerized deployments when they’re running on Kubernetes or another platform
- scanning container registries is also a great way to reduce the number of vulnerabilities across all of the frequently used images in your organization
    - You can also monitor your stored images over time, to identify any newly disclosed vulnerabilities in your existing images and prevent those from being deployed to production in the future.

Most container scanning solutions leverage a public source for vulnerability information like the National Vulnerability Database (NVD) or the Common Vulnerabilities & Exposures (CVE) database. These databases publish known exploits to enable automated vulnerability management, security measurement, and compliance. 

Each new layer has the risk of introducing new vulnerabilities into the container, so it’s crucial that the container scanner you use can detect issues layer by layer.

> **How does Container scanning work?** Scanning containers for vulnerabilities usually involves a security tool that analyzes a container image layer by layer to detect potential security issues. Most scanning solutions leverage a database of known vulnerabilities so that organizations can stay up-to-date as the security threat landscape evolves. Containerized applications also consist of multiple components, including custom code, open source dependencies, images, Dockerfiles, and more. Scanning for vulnerabilities across all of these components is critical for comprehensive container security.


- https://docs.docker.com/get-started/09_image_best/#security-scanning