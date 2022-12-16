### Sprawdzić oryginalne Arduino:

```commandline
q = PyTechBrain('/dev/ttyACM0')
Initializing object: <PyTechBrain.PyTechBrain.PyTechBrain object at 0x7f5140095cc0>.
q.board_init()
New debug messages:
Initializing object: <PyTechBrain.PyTechBrain.PyTechBrain object at 0x7f5140095cc0>.
2022-12-16 09:07:08.713179 -> Python version checking: 
3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0]
2022-12-16 09:07:24.084762 -> Board initialization starting - auto.
2022-12-16 09:07:24.093842 -> Element 0: /dev/ttyS4 / None / ttyS4
2022-12-16 09:07:24.093856 -> Element 1: /dev/ttyACM0 / None / ttyACM0
2022-12-16 09:07:24.093870 -> Not Arduino FTDI compatible device: n/a / None / USB VID:PID=0000:0000 
2022-12-16 09:07:24.093876 -> Not Arduino FTDI compatible device: ttyACM0 / Arduino (www.arduino.cc) / USB VID:PID=2341:0043 SER=55732323530351617221 LOCATION=1-2:1.0 
2022-12-16 09:07:24.093879 -> Error - no FTDI compatible decise found.
2022-12-16 09:07:24.093882 -> Some errors with auto initialization.
False
```

Dmesg:

```shell
Dec 16 09:06:42 laptop kernel: [ 4069.848650] usb 1-2: new full-speed USB device number 9 using xhci_hcd
Dec 16 09:06:42 laptop kernel: [ 4070.003975] usb 1-2: New USB device found, idVendor=2341, idProduct=0043, bcdDevice= 0.01
Dec 16 09:06:42 laptop kernel: [ 4070.003989] usb 1-2: New USB device strings: Mfr=1, Product=2, SerialNumber=220
Dec 16 09:06:42 laptop kernel: [ 4070.003995] usb 1-2: Manufacturer: Arduino (www.arduino.cc)
Dec 16 09:06:42 laptop kernel: [ 4070.004000] usb 1-2: SerialNumber: 55732323530351617221
Dec 16 09:06:42 laptop kernel: [ 4070.007763] cdc_acm 1-2:1.0: ttyACM0: USB ACM device
Dec 16 09:06:42 laptop mtp-probe: checking bus 1, device 9: "/sys/devices/pci0000:00/0000:00:14.0/usb1/1-2"
Dec 16 09:06:42 laptop mtp-probe: bus: 1, device: 9 was not an MTP device
Dec 16 09:06:42 laptop snapd[2465]: hotplug.go:200: hotplug device add event ignored, enable experimental.hotplug
Dec 16 09:06:42 laptop mtp-probe: checking bus 1, device 9: "/sys/devices/pci0000:00/0000:00:14.0/usb1/1-2"
Dec 16 09:06:42 laptop mtp-probe: bus: 1, device: 9 was not an MTP device

```