import yaml


def open_yaml(yaml_file):
    """
    Takes a YAML file as a parameter, opens and loads it as a dictionary and returns the dictionary
    """
    with open(yaml_file, "r") as f:
        try:
            f.readline()
            fstab_dict = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
        finally:
            f.close()
    return fstab_dict


def parse_fstab_dict(fstab_dict):
    """
    Takes a dictionary as a paramater, parses and formats content and prints it
    """
    for key, value in fstab_dict.items():
        device_spec = key
        mount_point = value["mount"]
        fs_type = value["type"]

        options = ""
        if "options" in value:  # read 'options' values if given in YAML file
            if isinstance(value["options"], list):
                for option in value["options"]:
                    options += option + ","
                options = options[:-1]
            else:
                options = value["options"]
        else:
            options = "defaults"  # default 'options' to 'defaults' if not given int YAML file

        # default 'dump' to '0' or read value if given in YAML file
        dump = "0"
        if "dump" in value:
            dump = value["dump"]

        # default 'pass' to '0' or read value if given in YAML file
        pass_fsck = "0"
        if "pass" in value:
            pass_fsck = value["pass"]

        if "export" in value and fs_type == "nfs":
            device_spec += ":" + value["export"]

        print(f"{device_spec} {mount_point} {fs_type} {options} {dump} {pass_fsck}")
