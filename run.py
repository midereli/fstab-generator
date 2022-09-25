from fstab.helpers import open_yaml, parse_fstab_dict
import argparse


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str,
                        help="name of the yaml file to be parsed")
    args = parser.parse_args()

    if args.file:
        fstab_dict = open_yaml(yaml_file=args.file)
    else:
        fstab_dict = open_yaml(yaml_file="mount-points.yaml")

    parse_fstab_dict(fstab_dict=fstab_dict)


if __name__ == '__main__':
    run()
