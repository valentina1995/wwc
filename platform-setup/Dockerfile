# docker image build --file Dockerfile -t wwc-platform:1.0 .

FROM continuumio/anaconda3

ARG nlp_env=nlp_course
WORKDIR /usr/src/app

# Create the environment
COPY base-requirements.txt .
COPY environment.yaml .
ADD notebooks notebooks
RUN conda env create -f environment.yaml

ENV PATH /opt/conda/envs/nlp_course/bin:$PATH
RUN /bin/bash -c "source activate nlp_course"

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "nlp_course", "/bin/bash", "-c"]

RUN python -m spacy download en_core_web_sm

EXPOSE 8888
# Code to run when container is started
ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]