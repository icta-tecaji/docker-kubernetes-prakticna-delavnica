# Configuring applications with ConfigMaps and Secrets

## Configuring containerized applications
One of the great advantages of running apps in containers is that you **eliminate the gaps between environments**.

Almost all apps require configuration (settings that differ between deployed instances, credentials for accessing external systems, and so on), which **shouldn’t be baked into the built app itself**.

Cloud-native microservices applications should de-couple the application
and the configuration, bringing benefits such as:
- Re-usable application images
- Simpler testing
- Simpler and fewer disruptive changes

There are multiple ways of passing configuration options to a containerized application:
- Passing command-line arguments to containers
- Setting custom environment variables for each container
- Mounting configuration files into containers through a special type of volume

Kubernetes supports configuration injection with two resource types: ConfigMaps and Secrets. Though most configuration options don’t contain any **sensitive information**, several can. These include credentials, private encryption keys, and similar data that needs to be kept secure. This type of information needs to be handled with special care, which is why Kubernetes offers another type of first-class object called a **Secret**. 

Both types can store data in any reasonable format, and that data lives in the cluster independent of any other resources.

You **create ConfigMap and Secret objects** like other resources in Kubernetes—
using kubectl, either with create commands or by applying a YAML specification. Unlike other resources, **they don’t do anything**; they’re just **storage units intended for small amounts of data**. Those storage units can be loaded into a Pod, becoming part of the container environment, so the application in the container can read the data.

## Using environment variables in Kubernetes

Environment variables are a core operating system feature in Linux and Windows, and they can be set at the machine level so any app can read them. They’re commonly used, and all containers have some, which are set by the operating system inside the container and by Kubernetes.
- `cd 23_Configuring_applications_with_ConfigMaps_and_Secrets/examples/01_env_variables/`
- `sudo kubectl apply -f 01_sleep.yaml`
- `sudo kubectl wait --for=condition=Ready pod -l app=sleep`
- `sudo kubectl get pod`
- Check some of the environment variables in the Pod container: `sudo kubectl exec deploy/sleep -- printenv HOSTNAME NON_VALID_VARIABLE` (printenv is a Linux command that shows the value of environment variables. The HOSTNAME variable exists in all Pod containers and is set by Kubernetes to be the Pod name. The NON_VALID_VARIABLE variable doesn’t exist, so the command exits with an error code)

Many technology stacks use environment variables as a basic configuration system. The simplest way to provide those settings in Kubernetes is by adding environment variables in the Pod specification.
- `cat 02_sleep-with-env.yaml`
- Update the sleep Deployment with the new Pod spec: `sudo kubectl apply -f 02_sleep-with-env.yaml`
- Check the same environment variables in the new Pod: `sudo kubectl exec deploy/sleep -- printenv HOSTNAME NON_VALID_VARIABLE`

> Environment variables are static for the life of the Pod; **you can’t update any values while the Pod is running**. If you need to make configuration changes, you need to perform an update with a replacement Pod.

You should get used to the idea that deployments aren’t just for new feature releases; you’ll also use them for configuration changes and software patches, and you must **design your apps to handle frequent Pod replacements**.

The new app is using the same Docker image; it’s the same application with all the same binaries — only the configuration settings have changed between deployments.

Setting **environment values inline in the Pod specification is fine for simple settings**, but real applications usually have more complex configuration requirements, which is when you use ConfigMaps.

## Creating configmaps using the kubectl

**A ConfigMap is just a resource that stores some data that can be loaded into a Pod.** The data can be a set of key-value pairs, a blurb of text, or even a binary file. You can use key-value pairs to load Pods with environment variables, text to load any type of config file—JSON, XML, YAML, TOML, INI—and binary files to load license keys.

One Pod can use many ConfigMaps, and each ConfigMap can be used by many Pods.

![ConfigMaps are separate resources](./images/img01.png)
<!-- Vir: Elton Stoneman - Learn Kubernetes in a Month of Lunches-Manning Publications (2021) -->

If you reference a ConfigMap in a Pod specification, **the ConfigMap needs to exist before you deploy the Pod**.

This spec expects to find a ConfigMap called `sleep-config-literal` with key-value pairs in the data, and the easiest way to create that is by passing the key and value to a kubectl command.
- `cat 03_sleep-with-configMap-env.yaml`
- Create a ConfigMap with data from the command line:
    - `sudo kubectl create configmap sleep-config-literal --from-literal=my-app-id='12345'`
> NOTE: ConfigMap keys must be a valid DNS subdomain (they may only contain alphanumeric characters, dashes, underscores, and dots). They may optionally include a leading dot.
- `sudo kubectl get cm sleep-config-literal` (check the ConfigMap details)
- `sudo kubectl describe cm sleep-config-literal` (show the friendly description of the ConfigMap)
- `sudo kubectl apply -f 03_sleep-with-configMap-env.yaml`
- `sudo kubectl exec deploy/sleep -- sh -c 'printenv'`

ConfigMaps usually contain more than one entry. To create a ConfigMap with multiple literal entries, you add multiple `--from-literal` arguments.

Creating ConfigMaps from literal values is fine for individual settings, but it **gets cumbersome fast if you have a lot of configuration data**. As well as specifying literal values on the command line, Kubernetes lets you load ConfigMaps from files.

## Storing and using configuration files in ConfigMaps



