# python-docker  details

ref: https://docs.docker.com/language/python/build-images/

Create flask image and push it into a fleet via 
Open terminal window and enter:
#### balena push val-one --noparent-check

val@pop-os:~$ curl localhost:8000
or
run curl http://127.0.0.1:5000 in the balena-cloud device terminal

#### Hello, Docker etc...!  will be printed on the console

####################################################
### Just use docker on PC - switch to slim Buster in dockerfile
### and, Don't forget the 'dot'!!!)
docker build -t pctest .
docker run pctest

