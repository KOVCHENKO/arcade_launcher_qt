#### Running venv
venv/Scripts/activate

#### Installing packages
pip install -r requirements.txt

#### Deactivating venv
venv/Scripts/deactivate

#### Necessary packages for card reader
##### install
apt search pcsc

apt-get install pcscd pcsc-tools

apt-get install libusb-dev libpcsclite1 libpcsclite-dev libpcsclite1-dbg dh-autoreconf

##### run
pcsc

pcsc_scan

#### SWIG need to be installed
apt-get install swig
