
RUN project
```shell script
sudo docker-compose run django_server python3 src/testDT/manage.py migrate
sudo docker-compose build
sudo docker-compose up
```