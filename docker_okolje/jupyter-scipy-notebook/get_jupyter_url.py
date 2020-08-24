import subprocess
import sys
import docker

# get container id
docker_run = subprocess.run(['docker', 'ps'], stdout=subprocess.PIPE)
docker_run_str = docker_run.stdout.decode('utf-8')
docker_run_list = docker_run_str.split()
try:
    jupyter_id = docker_run_list.index('jupyter/scipy-notebook')
    docker_id = docker_run_list[jupyter_id-1]
except ValueError:
    print('No running container.')

client = docker.from_env()
container = client.containers.get(docker_id)
jupyter_logs = container.logs().decode('utf-8').split('\n')
org_url = jupyter_logs[7].split('or')[1].strip()

new_list=org_url.split('127.0.0.1')

new_url = f'{new_list[0]}192.168.56.101{new_list[1]}'
print(new_url)