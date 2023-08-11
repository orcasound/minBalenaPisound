# Test accessing parameters stored in .env file under Balena

Create new directory and virtual environment
 python3 -m venv .venv
 source .venv/bin/activate
 
 Create python file that uses parameters  envtest.py
 
docker build --tag python-env-docker .

Then:
docker run python-env-docker
in .env file, foo equals 1.234    # python has been able to get the parameters from the .env file
bar equals this is text

#### balena push val-one --noparent-check
Now, in the dashboard.balena-cloud.com
Restarting service 'main sha256:cd4d46b62322a78fac735c31c7549bb3f2ebe2ffdfe192d4665163b6bda54372'
 main  in .env file, foo equals 1.234   # Yippeeeeeee
 main  bar equals this is text
Service exited 'main sha256:cd4d46b62322a78fac735c31c7549bb3f2ebe2ffdfe192d4665163b6bda54372'


## envtest.py
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    # Get the value of the `FOO` parameter from the `.env` file.
    foo = os.environ.get("FOO")

    # Get the value of the `BAR` parameter from the `.env` file.
    bar = os.environ.get("BAR")

    # Print the values of the `FOO` and `BAR` parameters.
    print("in .env file, foo equals", foo)
    print("bar equals", bar)

if __name__ == "__main__":
    main()



## requirements.txt
python-dotenv==1.0.0

## Dockerfile
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "envtest.py"]

 
