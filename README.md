# File Systems Table *or* `fstab` generator

## What is fstab-generator?

fstab-generator converts a YAML file describing the mount points of a system into an `/etc/fstab` file.

### How to use?

```sh
# Create your Python virtual environment (recommended)
$ python3 -m venv .venv

# Activate your virtual environment
$ source .venv/bin/activate

# Installl requirements
$ pip install -r requirements.txt

# Execute with -h for general information
$ python run.py -h
usage: run.py [-h] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  name of the yaml file to be parsed

# Execute without arguments to test with the "mount-points.yaml" file provided in the project
$ python run.py
/dev/sda1 /boot xfs defaults 0 0
/dev/sda2 / ext4 defaults 0 0
/dev/sdb1 /var/lib/postgresql ext4 defaults 0 0
192.168.4.5:/var/nfs/home /home nfs noexec,nosuid 0 0

# Execute with "-f" or "--file" to test with any YAML file
$ python run.py --file ~/my-great-mount-points-file.yaml/dev/sda1 /boot xfs defaults 0 0
/dev/sda2 / ext4 defaults 0 0
/dev/sdb1 /var/lib/postgresql ext4 defaults 0 0
192.168.4.5:/var/nfs/home /home nfs noexec 0 0
```

