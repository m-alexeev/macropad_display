## Boot config File
import time
import board, digitalio
import json

import usb_cdc
import storage

print("Boot File Loading...")

reset_button = digitalio.DigitalInOut(board.A2) #Encoder Switch
reset_button.pull = digitalio.Pull.UP # Connected to ground so pull up
		

def disable_usb() -> None:
	if not reset_button.value: 
		print("Enabling USB and REPL")
		storage.enable_usb_drive()
		usb_cdc.enable()
	else:
		print("Disabling USB and REPL")
		# Disable USB and REPL if reset button not pressed
		storage.disable_usb_drive()
		usb_cdc.disable()


# disable_usb()



