## Unow Mailer

This project was created as a Python API using FastAPI. It sends emails to the user through SMTP, working with Gmail. A new Gmail account was created to manage the emails.

### Requirements
- Python3.12
- pipenv
- Docker

## Setting

Before deploying this project locally, start with the Symfony REST API first, because it needs the network created in that project:
https://github.com/nasquevedo/rest-api-unow/blob/develop/README.md

After deploying the first project, the pipenv dependency must be installed, just in case the machine doesn't have this:

```sh 
pip install pipenv
````

Once pipenv was installed, install the project dependencies with the next command:

```sh
pipenv install
```

As soon as the dependencies were installed, run the container using the docker-compose file:

```sh
docker-compose up -d --build
```

Finally, the container should be created correctly and test it on localhost:8000
(http://localhost:8000/)[http://localhost:8000/]
