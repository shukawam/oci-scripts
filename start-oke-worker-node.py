import argparse
import sys

import oci
from oci.core import ComputeClient


class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog, indent_increment=2, max_help_position=50, width=None):
        super().__init__(prog, indent_increment, max_help_position, width)


def parseInput():
    parser = argparse.ArgumentParser(
        description="OKE Worker Node START Script.", formatter_class=CustomHelpFormatter)
    parser.add_argument('--compartment-id', type=str, help="[required]")
    parser.add_argument('--profile', type=str,
                        default="DEFAULT", help="[optional]")
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
    else:
        return parser.parse_args()


def main():
    args = parseInput()
    config = oci.config.from_file("~/.oci/config", args.profile)
    compartment_id = args.compartment_id

    compute_client = ComputeClient(config)
    compute_list_response = compute_client.list_instances(compartment_id).data

    oke_worker_nodes = list(
        filter(lambda d: d.display_name.startswith('oke'), compute_list_response))

    for worker_node in oke_worker_nodes:
        worker_nodes_id = worker_node.id
        instance_action_response = compute_client.instance_action(
            worker_nodes_id, "START")
        print(instance_action_response.data.lifecycle_state)


if __name__ == "__main__":
    main()
