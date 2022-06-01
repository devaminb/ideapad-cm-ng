#!/usr/bin/env python3

import click

from ideapad_cm.battery.Battery import Battery
from ideapad_cm.battery.CantReadStatusError import CantReadStatusError


@click.group()
@click.version_option(package_name="ideapad-cm", prog_name="ideapad-cm")
def cli():
    pass


@cli.command()
def enable():
    """Enable battery conservation mode."""
    Battery().conservation_mode.enable()


@cli.command()
def disable():
    """Disable battery conservation mode."""
    Battery().conservation_mode.disable()


@cli.command()
def status():
    """Get the status of battery conservation mode."""
    try:
        is_enabled: bool = Battery().conservation_mode.status()
        if is_enabled:
            click.echo("Battery conservation mode is currently enabled.")
        else:
            click.echo("Battery conservation mode is currently disabled.")
    except CantReadStatusError:
        click.echo("Error reading battery conservation mode status.")


cli.add_command(enable)

if __name__ == '__main__':
    # TODO: Make sure the returned exit codes match the original script
    cli()
