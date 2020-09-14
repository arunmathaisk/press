# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe and contributors
# For license information, please see license.txt
import click

from backbone.hypervisor import Hypervisor, Shell
from backbone.tests import run_tests


@click.group()
def cli():
	pass


@cli.group()
def hypervisor():
	pass


@hypervisor.command()
def setup():
	shell = Shell()
	hypervisor = Hypervisor(shell=shell)
	hypervisor.setup()


@hypervisor.command()
def build():
	shell = Shell()
	hypervisor = Hypervisor(shell=shell)
	hypervisor.build()


@hypervisor.command()
def up():
	shell = Shell()
	hypervisor = Hypervisor(shell=shell)
	hypervisor.up()


@hypervisor.command()
@click.option("-c", "--command")
def ssh(command):
	shell = Shell()
	hypervisor = Hypervisor(shell=shell)
	hypervisor.ssh(command=command)


@cli.command()
def tests():
	run_tests()
