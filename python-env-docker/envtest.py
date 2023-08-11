import os
from dotenv import load_dotenv

load_dotenv()

def main():
    # Get the value of the `FOO` parameter from the `.env` file.
    foo = os.environ.get("FOO")

    # Get the value of the `BAR` parameter from the `.env` file.
    bar = os.environ.get("BAR")

    # Print the values of the `FOO` and `BAR` parameters.
    print("in folder python-env-docker's .env file, foo equals", foo)
    print("bar equals", bar)

if __name__ == "__main__":
    main()



