from pathlib import Path
from termcolor import colored, cprint
from module import Module

class CustomModule(Module):
    def __init__(self):
        information = {"Name": "MacOS Utility to display information of the system",
                       "Description": "This module will display information of the system in the system's victim console",
                       "Author": "@lucferbux"}

        # -----------name-----default_value--description--required?
        options = {"warrior": [None, "Warrior in war", True],
                   "type": ["SPSoftwareDataType", "Type of the display [SPSoftwareDataType | SPNetworkDataType | SPHardwareDataType]", True]}

        # Constructor of the parent class
        super(CustomModule, self).__init__(information, options)

    # This module must be always implemented, it is called by the run option
    def run_module(self):

        warrior_exist = False
        for p in Path("/tmp/").glob("ibs-*"):
            if str(p)[9:] == self.args["warrior"]:
                warrior_exist = True
                break

        if warrior_exist:
            function = """
            function sys-info {
                param(
                        [Parameter(Mandatory)]
                        [ValidateSet("SPSoftwareDataType", "SPNetworkDataType", "SPHardwareDataType")]
                        [string]$type
                )
                $infos = system_profiler $type                
                return $infos -replace '[^\x00-\x7F]+', ''
            }
            """
            function += 'sys-info {}'.format(self.args["type"])

            with open('/tmp/ibs-{}'.format(self.args["warrior"]), 'a') as f:
                f.write(function)
            cprint ('[+] Done!', 'green')
        else:
            cprint ('[!] Failed... Warrior don´t found', 'red')
