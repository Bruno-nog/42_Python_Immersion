import cowsay

def greeting(name: str) -> None:
    """receives a name and prints a greeting"""
    cowsay.cow(f"Hello {name}")