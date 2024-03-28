#! /usr/bin/env python

'''
Example custom dynamic inventory script for Ansible, in Python
'''

import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):
    ''' Host inventory class. '''

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host`.
        elif self.args.host:
            self.inventory = self.empty_inventory()
        # If no arguments were specified.
        else:
            self.inventory = self.example_inventory()

        print json.dumps(self.inventory);

    def read_cli_args(self):
        ''' Read the command line args passed to the script. '''
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

    def example_inventory(self):