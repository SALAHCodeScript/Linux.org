#!/usr/bin/python3.12
import subprocess as sp

def returnOutputCommand(cmd):
    return bytes.decode(sp.run(cmd, input=None, capture_output=True, timeout=None, check=False).stdout)

path = '/home/mint/Documents/.programming/'
listDir = returnOutputCommand(['ls', path])

