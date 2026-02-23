import subprocess

def test_file_correct():
    with open("Jorge.txt", "wb") as f:
        f.write(b"Banana Madura")
    result = subprocess.run(
        ["python3", "read_file.py", "Jorge.txt"],
        capture_output=True,
        text=True
    )
    subprocess.run(["rm", "rf", "Jorge.txt"])
    assert result.stdout.strip() == "Banana Madura"

def test_file_not_found():
    result = subprocess.run(
        ["python3", "read_file.py", "./unknown_file.txt"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "Error: File not found."


def test_file_is_dir():
    result = subprocess.run(
        ["python3", "read_file.py", "/bin/"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "Error: The argument provided is a directory."


def test_file_permiss():
    subprocess.run(["touch", "forbidden.txt"])
    subprocess.run(["chmod", "000", "forbidden.txt"])
    result = subprocess.run(
        ["python3", "read_file.py", "forbidden.txt"],
        capture_output=True,
        text=True
    )
    subprocess.run(["rm", "rf", "forbidden.txt"])
    assert result.stdout.strip() == "Unexpected error: PermissionError"


def test_file_unicode():
    with open("invalid.txt", "wb") as f:
        f.write(b"\x80abc")
    result = subprocess.run(["python3", "read_file.py", "invalid.txt"],
        capture_output=True,
        text=True
    )
    subprocess.run(["rm", "-rf", "invalid.txt"])
    assert result.stdout.strip() == "Unexpected error: UnicodeDecodeError"