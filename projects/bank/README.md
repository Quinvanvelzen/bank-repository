# bank-repository
Project to practice with Object Oriented Programming


## Commands

### Example usage

#### Build the project

Navigate to this folder (where the `pyproject.toml` file is)

Run:

```shell
poetry build-project
```

#### Build a Docker image
This reads the files in the current directory (.), it builds an image according to the instructions in the dockerfile. It tags the resulting image with the name 'myimage'
```shell
docker build -t myimage .
```

#### Run the image
```shell
docker run -d --name mycontainer -p 8000:8000 myimage
```

### Rebuilding the image

```shell
poetry build-project 
docker stop $(docker ps -q)
docker rm $(docker ps -a -q)
docker rmi myimage
docker build -t myimage .
docker run -d --name mycontainer -p 8000:8000 myimage
```