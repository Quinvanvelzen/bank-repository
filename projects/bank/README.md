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
```shell
docker build -t myimage .
```

#### Run the image
```shell
docker run -d --name mycontainer -p 8000:8000 myimage
```