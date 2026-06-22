"""
Simple logger for Automation-YT.
"""

from datetime import datetime


def log(message):
    print(f"[{datetime.now()}] {message}")


if __name__ == "__main__":
    log("Automation-YT started.")
