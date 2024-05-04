# Fyle Backend Challenge

### Installation

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```

### Start Server with Docker 

```
# Using DockerFile

sudo docker build -t sarthak0714/fyle-backend
sudo docker run -p 7755:7755 sarthak0714/fyle-backend

#Using docker-compose

sudo docker compose up

# Server will start at `http://0.0.0.0:7755`
```
### Run Tests (Reset DB before testing)

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
#
```

### ScreenShots [All Test Cases & 95% coverage]

![Test Cases and Coverage]()
