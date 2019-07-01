# pyhidapi Installation
You can install pyhidapi [from PyPI](https://pypi.org/project/hid/):
```
pip install hid
```

You also need to ensure that you have the required hidapi shared library. On Linux distributions, this is generally in the repositories (for instance, under Debian/Ubuntu/Linux Mint you can install either libhidapi-hidraw0 or libhidapi-libusb0 depending on which backend you want to use).

Installation procedure for Windows is described in https://github.com/libusb/hidapi#building-on-windows

# OSX Support
pyhidapi works on OSX, but requires that you first build a shared library. There may be better ways to do this, but what I did was as follows:

1. Download the latest hidapi release from https://github.com/libusb/hidapi/downloads and unzip
2. Navigate to the mac directory
3. Modify the Makefile to include -fPIC on the CFLAGS line.  My CFLAGS now look like this: `CFLAGS+=-I../hidapi -Wall -g -c -fPIC`
4. Run `make`.  You should now have a hid.o file in this directory.
5. Create the shared library by running: `gcc -shared -o libhidapi-iohidmanager.so hid.o -framework IOKit -framework CoreFoundation`
6. Copy the resulting libhidapi-iohidmanager.so to /usr/local/lib (or somewhere in the libs search path)
7. Install pyhidapi as normal: `python setup.py install`
8. Verify by running python interactively and typing the following lines:
```
import hid
hid.enumerate()
```
You should see a list of all USB hid devices on your system.

That's it!
