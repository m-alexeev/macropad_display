## Boot config File 
import time 
import board 
import touchio 
import neopixel 

## Turn on / off USB features to on touching RX & TX pins 
## Squeeze RX & TX Pins with Fingers to enable CIRCUITPY & REPL and Restart board


led = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = 0.2)
touchRxIn = touchio.TouchIn(board.RX)
touchTxIn = touchio.TouchIn(board.TX)


if touchRxIn.raw_value > 1500 and touchTxIn.raw_value > 1500: 
    for i in range(5):  # blink LED
        led[0] = 0x00ff00
        time.sleep(0.1)
        led[0] = 0x000000
        time.sleep(0.1)
    # Disable devices 
    import storage 
    import usb_cdc 
    storage.disable_usb_drive()
    usb_cdc.disable()

      