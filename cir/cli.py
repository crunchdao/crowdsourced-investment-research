import click
import matplotlib.pyplot as plt
import numpy as np


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
)
def cli():
    """Management CLI for desci"""


@cli.command(name="helloworld")
def helloworld():
    """Hello World."""
    print("Hello World!")
