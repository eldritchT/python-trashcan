import time
# StylePrintLib by dw17
# You can use this library for anything except reuploading in any form.
# Also, this lib works in most terminals, but not every.
# WORK IN PROGRESS
def timeprint(text: str, chartime: float):
	for i in text:
		print(i, end="")
		time.sleep(chartime)
		
def decorate(color: str):
    colors = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKCYAN': '\033[96m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
    }
    return colors[color.upper()]
