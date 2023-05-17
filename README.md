[![kodilla-final-project](https://github.com/TomaszKlosinski/kodilla-final-project/actions/workflows/ci.yaml/badge.svg)](https://github.com/TomaszKlosinski/kodilla-final-project/actions/workflows/ci.yaml)

# kodilla-final-project
Final Project for Kodilla Python Bootcamp - a flask-based Blog application.

See the deployed project on Heroku:
https://kodilla-final-project.herokuapp.com/

See other exercises and notes from the Python Bootcamp:
https://github.com/TomaszKlosinski/kodilla-python-bootcamp/


## Local development

To run the application locally:
```shell
pip install -r requirements.txt
export FLASK_APP=blog.py
flask run
```

Alternatively, you can use docker:
```shell
docker build -t blog .
docker run -p 8080:5000 --name blog blog
```

Or docker-compose:
```shell
docker-compose build
docker-compose up
```


## Tests

Install required packages:
```shell
pip install -r requirements.txt
```

Run locally:
```shell
pytest -v
```

Tests with different Python versions:
```shell
tox --recreate
```

Or if you have Vagrant+VirtualBox, you can use:
```shell
vagrant up
```

<!-- ## CI/CD

See the tests on Continuous Integration workflow:
https://github.com/TomaszKlosinski/kodilla-final-project/actions -->
