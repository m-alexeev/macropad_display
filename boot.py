## Boot config File 
import time 
import board 
import touchio 

## Turn on / off USB features to on touching RX & TX pins 
## Squeeze RX & TX Pins with Fingers to enable CIRCUITPY & REPL and Restart board

# print("Boot File Loading...")

# touchRxIn = touchio.TouchIn(board.RX)
# touchTxIn = touchio.TouchIn(board.TX)


# if touchRxIn.raw_value > 1500 and touchTxIn.raw_value > 1500: 
#     print("Disabling USB Features...")
#     # Disable devices 
#     import storage 
#     import usb_cdc 
#     storage.disable_usb_drive()abcabcfdeighdefffdefdefdefdefdefdefdeabcabcabcabcabcabcghi
#     usb_cdc.disable()
