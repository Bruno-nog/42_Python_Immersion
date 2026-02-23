import subprocess

def test_convert():
    result = subprocess.run(
        ["python3", "convert.py", "42"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "42.0"

    result = subprocess.run(
        ["python3", "convert.py", "23.0"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "23.0"
    
    result = subprocess.run(
        ["python3", "convert.py", "-7"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "-7.0"

    result = subprocess.run(
        ["python3", "convert.py", "0"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "0.0"


def test_convert_error():
    result = subprocess.run(
        ["python3", "convert.py", "Hello"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "conversion impossible"

    result = subprocess.run(
        ["python3", "convert.py", "@#$"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "conversion impossible"

    result = subprocess.run(
        ["python3", "convert.py", ""],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "conversion impossible"