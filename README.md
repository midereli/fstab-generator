# File Systems Table *or* `fstab` generator

## What is fstab-generator?

fstab-generator converts a YAML file describing the mount points of a system into an `/etc/fstab` file.

## How to use it?

*Please use Python with a version greater than* `3.6.0`.

### Create and activate virtual environment *(recommended, but not required)*

*If you don't want to create a virtual environment, please jump to [Install requirements](#install-requirements).*

```sh
# Create your Python virtual environment
python3 -m venv .venv
```
```sh
# Activate your virtual environment (POSIX)
source .venv/bin/activate
```
```sh
# Activate your virtual environment (Windows cmd.exe)
.venv\Scripts\activate.bat
```
### Install requirements
```sh
pip install -r requirements.txt
```
### Execution
#### Execute with `-h` for general information
```sh
python run.py -h
```
<!--
```sh
usage: run.py [-h] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  name of the yaml file to be parsed
```
-->
#### Execute with no arguments to test with the `mount-points.yaml` file provided in the project folder `resources/yaml-files/`
```sh
python run.py
```
<!--
```sh
/dev/sda1 /boot xfs defaults 0 0
/dev/sda2 / ext4 defaults 0 0
/dev/sdb1 /var/lib/postgresql ext4 defaults 0 0
192.168.4.5:/var/nfs/home /home nfs noexec,nosuid 0 0
```
-->
#### Execute with `-f` or `--file` to test with any YAML file
```sh
python run.py --file resources/yaml-files/mount-points-test-case-1.yaml
```
<!--
```sh
/dev/sda1 /boot xfs defaults 0 0
/dev/sda2 / ext4 defaults 0 0
/dev/sdb1 /var/lib/postgresql ext4 defaults 0 0
192.168.4.5:/var/nfs/home /home nfs noexec 0 0
```
-->
