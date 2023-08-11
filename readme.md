# Experimenting with Balena and Docker -- working toward building OrcaNode

docker-python is a simple flask server app loaded into Rpi via Balena

python-env-docker is an example of getting .env parameter values via a 
python script with balena loading the image into the Rpi

Next step:  A simple bash script running in the Rpi that can access the .env parameters.

Eventually:  (1) Install pisound drivers and then (2) build orcanode

The orcanode-balena directory has a working Dockerfile docker-compose.yml set of files.

    You do need a .env file with the AWS keys and NODE_NAME etc.
