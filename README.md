# docker-miniforge3-jupyter-datascience

#### Minimal structure for Python Datascience Development in Jupyter Notebook using Miniforge environment

## Services
- miniforge3 that uses image 'condaforge/miniforge3'
- jupyter that uses image 'jupyter/scipy-notebook'

## Volumes
- shared:
This volume is shared by the two containers.

## Running
```sh
docker-compose up
```
And in browser: 

```sh
http://127.0.0.1:8888/lab
```

## Understand
### Purpose of this repository
Aim to create a python development environment for datascience.
- Execute python scripts that create a dataframe with random values and save it as a 'csv' file.
- Execute python scripts that apply a function to the generated dataframe and save the results in a 'csv' file.
- Open Jupyter to create (or execute) a notebook that use the generated data to display plots.
### Dockerfiles
#### conda
Create a container from 'condaforge/miniforge3' image and copy and run python scripts in the shared folder.

#### jupyter
Create a container from 'jupyter/scipy-notebook' image and copy a notebook.

## To do (ideas)
? : copy and run every python scripts in the shared folder (RUN python *.py)

? : run notebooks
