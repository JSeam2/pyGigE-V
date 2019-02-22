### PyGigE-V

#### Minimal Python wrapper for Teledyne DALSA's GigE-V Framework
A python wrapper for some of the GigE-V Framework API methods which work with [Teledyne Dalsa Cameras](https://www.teledynedalsa.com). 
This is meant for use on Linux systems. I am not sure if this would work on other operating systems. 
This was forked from [jcramer/pyGigE-V](https://github.com/jcramer/pyGigE-V). 
This fork fixes some bugs and ports the code to python3.
The code tested to work on python3, Ubuntu 18.04, Genie Nano camera, and GigE-V-Framework\_2.10.0.0157 

### Installing GigE-V Framework for Linux
1. Go to Teledyne Dalsa's download page for the GigE-V Framework for Linux at [https://www.teledynedalsa.com/en/support/downloads-center/software-development-kits/132/](https://www.teledynedalsa.com/en/support/downloads-center/software-development-kits/132/) __Last accessed on 22 Feb 2019 version 2.10.0.0157__
2. Download the GigE-V Framework (includes documentation) file.
3. Once you have downloaded the file extract it.
4. In the folder you should see a bunch of implementations for different architectures mainly
    - aarch64 64-bit ARMv8 is used in NVIDIA's Jetson
    - ARMhf (arm hard float) 32-bit ARMv7.This refers to ARM processors with hardware floating point support. Beaglebone Black is one example
    - ARMsf (arm soft float) 32-bit ARMv7. this refers to arm processors without hardware floating point, these processors emulates floats in software 
    - x86 this refers to Intel and AMD processors both 32bits and 64bits
5. Extract the appropriate DALSA folder into home directory
6. You will need to install the following prerequisite libraries. On Ubuntu:
```
$ sudo apt install gcc g++ make libx11-dev libxext-dev libgtk-3-dev libglade2-0 libglade2.dev libpcap0.8 libcap2 ethtool
```
7. Once you have installed the libraries navigate to home
```
$ cd ~
$ cd DALSA
``` 
8. Run the install script this should be sufficient for installation
```
./corinstall
```
9. Check if your installation works by running you should see
```
$ lsgev
[MACADDRESS]@[IPADDRESS] on eth0=[IPADDRESS]  # FOR EXAMPLE
```
10. If environment variables are not added, you may add them manually. Access .bashrc if you are using bash and add the following variables at the end of the file. Save and restart the shell and the changes should take effect.
```
# DALSA Environment Variables
export GENICAM_ROOT_V3_0="/opt/genicam_v3_0"
export GENICAM_CACHE_V3_0="/var/opt/genicam/xml/cache"
export GENICAM_LOG_CONFIG_V3_0="/opt/genicam_v3_0/log/config-unix"
export GIGEV_XML_DOWNLOAD="/usr/dalsa/GigeV"
```

10. If you cannot connect to your camera if it is connected via ethernet you will need to edit the network settings. Under IPv4 settings > IPv4 Method, set the connection type as Link Local Only. Under IPv6 settings > IPv6 Method select disable. Give it some time and the camera should eventually be detected. Don't forget to select the connection. Check if the cameras are detected using lsgev command
```
$ lsgev
```

### Installing Python Package from source repo
1.  Download this repository locally
2.  Make sure you have the build tools read
3.  Run `python setup.py install` at the repo's root dir
4.  Test by running `python test.py` example

#### Extending this module using Cython (for developemnt) 
1.  Install GigE-V framework 2.02 https://www.teledynedalsa.com/imaging/products/software/linux-gige-v/
2.  Download this repository locally
3.  Install cython via `pip install Cython`
4.  Change the USE_CYTHON flag to `True` in the setup.py file
5.  Build the module using `python setup.py build_ext --inplace`
6.  test by running `python test.py` example
