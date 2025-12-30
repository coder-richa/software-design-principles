"""
This module prints the current Python version from within a Docker container.
"""

import sys


def main():
    """Main entry point of the script."""
    print(f"Hello from inside Docker! Python version: {sys.version}")


if __name__ == "__main__":
    main()
