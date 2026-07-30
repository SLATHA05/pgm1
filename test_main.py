import subprocess
import sys


def run_program():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True
    )

    # If the student's program crashes, show the error
    assert result.returncode == 0, f"Program crashed:\n{result.stderr}"

    return result.stdout.strip()


def test_profit():
    output = run_program()
    assert "800" in output


def test_contains_profit():
    output = run_program().lower()
    assert "profit" in output
