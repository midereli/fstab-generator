import yaml


def open_yaml(yaml_file):
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
    for key, value in fstab_dict.items():
        device_spec = key
        mount_point = value["mount"]
        fs_type = value["type"]

        options = ""
        if "options" in value:
            if isinstance(value["options"], list):
                for option in value["options"]:
                    options += option + ","
                options = options[:-1]
            else:
                options = value["options"]
        else:
            options = "defaults"

        dump = ""
        if "dump" in value:
            dump = value["dump"]
        else:
            dump = "0"

        fsck = ""
        if "fsck" in value:
            fsck = value["fsck"]
        else:
            fsck = "0"

        if "export" in value and fs_type == "nfs":
            device_spec += ":" + value["export"]

        print(f"{device_spec} {mount_point} {fs_type} {options} {dump} {fsck}")
