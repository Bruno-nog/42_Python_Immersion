import os

def verify_virtual_env() -> None:
    """Verify if virtual environment is active or inactive"""
    try:
        if (os.environ['VIRTUAL_ENV']):
            print("Virtual environment active")
    except KeyError:
        print("Virtual environment inactive")

if __name__ == '__main__':
    verify_virtual_env()