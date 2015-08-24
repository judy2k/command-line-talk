#!/usr/bin/env python

import click

click.secho('some red text', fg='red')
click.secho('and with a green background', fg='red', bg='green')
click.secho('and in bright text', fg='red', bg='green', bold=True)
click.secho('back to normal now')
