#! /usr/bin/env python3

try:

    from src import cli

    cli()

except Exception as e:
    print(f"\nUnknown error: {e}")
