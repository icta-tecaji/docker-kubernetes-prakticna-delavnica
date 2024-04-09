



### Configure default logging driver
- https://docs.docker.com/engine/install/linux-postinstall/#configure-default-logging-driver
Docker provides logging drivers for collecting and viewing log data from all containers running on a host. The default logging driver, json-file, writes log data to JSON-formatted files on the host filesystem. Over time, these log files expand in size, leading to potential exhaustion of disk resources.

To avoid issues with overusing disk for log data, consider one of the following options:

Configure the json-file logging driver to turn on log rotation.
Use an alternative logging driver such as the "local" logging driver that performs log rotation by default.
Use a logging driver that sends logs to a remote logging aggregator.