# What is this

- handle raspi pico with:
  - [micropython](https://github.com/micropython/micropython)

## First

```bash
$ ./allow_dev.sh
```

## Useful links

- Examples of micropython for raspberry Pi Pico
  - [rapberrypi/pico-micropython-examples](https://github.com/raspberrypi/pico-micropython-examples)

## Useful commands

### ampy

- write/read file

```bash
$ pip install adafruit-ampy
$ export AMPY_PORT=/dev/ttyUSB0
$ ampy ls
```

### Thonny IDE

- GUI code editor for micropython

```bash
$ pip3 install thonny
```

In case you confront with `ModuleNotFoundError: No module named '_tkinter'`, See [this](https://stackoverflow.com/questions/26357567/cannot-import-tkinter-after-installing-python-3-with-pyenv#26358646):

```bash
$ pyenv uninstall x.x.x
$ sudo apt install tk-dev
$ pyenv install x.x.x
```

### picocom

- Connect to REPL through serial communication

```bash
$ sudo apt install picocom
$ picocom /dev/ttyUSB0 -b 115200
```

### fritzing

- Designing Circuits IDE

```bash
$ sudo apt install fritzing
$ fritzing
```

### esptool.py

```bash
$ pip install esptool
$ esptool.py --port /dev/ttyUSB0 erase_flash
# Micropython
$ wget \
    "http://micropython.org/resources/firmware/esp32-idf3-20200902-v1.13.bin"
# Original firmware
# Goto: https://github.com/espressif/esp-at/releases/tag/v2.1.0.0_esp32s2
# Download: ESP32-S2-WROOM_AT_Bin_V2.1.0.0.zip
# Copy: factory/factory_WROOM.bin
$ esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash \
    -z 0x1000 esp32-*.bin
```
