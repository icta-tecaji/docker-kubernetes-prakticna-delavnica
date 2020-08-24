# -! jupyter-scipy-notebook
run_scipy_notebook:
	docker-compose -f ./docker_okolje/jupyter-scipy-notebook/docker-compose.yaml up -d

stop_scipy_notebook:
	docker-compose -f ./docker_okolje/jupyter-scipy-notebook/docker-compose.yaml down

get_jupyter_url:
	python3 ./docker_okolje/jupyter-scipy-notebook/get_jupyter_url.py