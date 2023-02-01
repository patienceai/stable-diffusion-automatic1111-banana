FROM nvidia/cuda:11.7.1-runtime-ubuntu22.04

RUN apt update && apt-get -y install git wget \
    python3.10 python3.10-venv python3-pip \
    build-essential libgl-dev libglib2.0-0 vim
RUN ln -s /usr/bin/python3.10 /usr/bin/python 

RUN useradd -ms /bin/bash banana
USER banana
WORKDIR /home/banana

RUN git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
WORKDIR /home/banana/stable-diffusion-webui
RUN git checkout 2c1bb46c7ad5b4536f6587d327a03f0ff7811c5d

RUN wget -O models/Stable-diffusion/model.safetensors 'https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors'

ADD prepare.py .
RUN python prepare.py --skip-torch-cuda-test --xformers --reinstall-torch --reinstall-xformers

ADD download.py download.py
RUN python download.py --use-cpu=all

RUN mkdir -p scripts/banana/scripts
ADD script.py scripts/banana/scripts/banana.py
ADD app.py app.py
ADD server.py server.py

CMD ["python", "server.py", "--xformers", "--disable-safe-unpickle", "--port", "8000"]
