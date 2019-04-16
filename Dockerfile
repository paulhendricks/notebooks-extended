# FROM rapidsai/rapidsai:cuda9.2-runtime-ubuntu16.04
FROM rapidsai/rapidsai-nightly:0.6-cuda10.0-devel-ubuntu18.04-gcc7-py3.7
#FROM rapidsai/rapidsai:0.6-cuda10.0-devel-ubuntu18.04-gcc7-py3.7

RUN apt-get update &&\
    apt-get install -y graphviz

SHELL ["/bin/bash", "-c"]
RUN source activate rapids && conda install -y \
        matplotlib \
        scikit-learn \
        seaborn

RUN source activate rapids && pip install graphviz

# ToDo: let user supply kaggle creds
RUN source activate rapids && pip install kaggle

ADD data /data
RUN mkdir -p /rapids/notebooks/extended
# symlinked so users can browse the data directory inside JupyterLab
RUN ln -s /data /rapids/notebooks/extended

ADD tutorials /rapids/notebooks/extended/tutorials

WORKDIR /rapids/notebooks/extended
#CMD bash
CMD source activate rapids && sh /rapids/notebooks/utils/start-jupyter.sh
