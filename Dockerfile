FROM jupyter/scipy-notebook:latest

USER root

# Do root stuff here

USER $NB_UID

RUN conda config --add channels conda-forge


RUN pip install spotipy

RUN conda install -c conda-forge nodejs

RUN pip install d6tflow

RUN conda install -c conda-forge tornado==5.1.1

RUN fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

USER root

RUN apt-get update
RUN apt-get install python3-pydot graphviz --yes

USER $NB_UID

WORKDIR /home/jovyan/work

CMD ["start-notebook.sh", "--NotebookApp.port=9999", "--NotebookApp.token=''"]
