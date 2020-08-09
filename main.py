#!/usr/bin/env python3

from subprocess import PIPE, run
from argparse import ArgumentParser
from gpiozero import Button
from signal import pause


parser = ArgumentParser('physical_button')
parser.add_argument('cmd', help="Command to run as argument")
args = parser.parse_args()

def button_pressed():
    print(f'Running command: \'{args}\'')

    if len(args.cmd):
        proc = run(args.cmd, stdout=PIPE, stderr=PIPE)

    if len(proc.stdout) > 0:
        print(proc.stdout)


button = Button(2)

button.when_pressed = button_pressed
pause()
