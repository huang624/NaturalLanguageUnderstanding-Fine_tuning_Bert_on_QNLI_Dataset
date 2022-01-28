FROM nvidia/cuda:11.1-cudnn8-devel-ubuntu20.04

WORKDIR /app
EXPOSE 8000


# Basic dependencies (python 3.8)
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl \
    git \
    python3 \
    python3-distutils \
    && rm -rf /var/lib/apt/lists

# Setup python
RUN curl https://bootstrap.pypa.io/get-pip.py | python3 \
    && python3 -m pip install --upgrade pip setuptools wheel

# Install modules
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy whole app
COPY . .

ENTRYPOINT uvicorn server:app --host 0.0.0.0 --port 8000
