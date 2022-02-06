

init:
	@esptool.py --port /dev/tty.usbserial-0001 erase_flash
	@esptool.py --chip esp32 --port /dev/tty.usbserial-0001 write_flash -z 0x1000 esp32-20220117-v1.18.bin
	@ampy put libs/*.py