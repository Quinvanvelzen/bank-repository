# Creates base (parent) image
FROM python:3.10

# a wheel installs faster than normal source distributions (tar files)
# this shows the version to be installed in the docker image
# {dist}-{version}(-{build})?-{python}-{abi}-{platform}.whl
ARG wheel=bank-0.0.1-py3-none-any.whl

# upgrade pip (python package installer) to the latest version, so that the latest features are available
RUN python -m pip install --upgrade pip

# a code folder is created in docker
WORKDIR /code

# Copying files in the code folder: COPY ./dist/$wheel /code/$wheel
COPY ./dist/$wheel /code/$wheel

# the bank package (wheel) is installed in the code directory
RUN pip install --no-cache-dir --upgrade /code/$wheel

# when a container starts from this image, the CMD is run
# uvicorn starts the app, list all ip adresses inside the container
# by default listen to local host
# this is written in json format, it looksl like this: uvicorn demo.greet_api.core:app --host 0.0.0.0 --port 8000
CMD ["uvicorn", "demo.greet_api.core:app", "--host", "0.0.0.0", "--port", "8000"]
