## Boot config File
import time
import board
import touchio
import json

import usb_cdc
import storage

print("Boot File Loading...")


def read_config() -> None:
	with open("./config.json", 'r') as f:
		config = json.load(f)
		
		## Get config 
		usb = config['USB']
		repl = config['REPL']

		if repl:
			usb_cdc.enable()
		else:
			usb_cdc.disable()


read_config()
