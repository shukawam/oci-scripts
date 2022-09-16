import argparse
import sys

import oci
from oci.core import ComputeClient


class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog, indent_increment=2, max_help_position=50, width=None):
        super().__init__(prog, indent_increment, max_help_position, width)


def parseInput():
    parser = argparse.ArgumentParser(
        description="Dreamkast Dev Instance START Script.", formatter_class=CustomHelpFormatter)
    parser.add_argument('--compartment-id', type=str, help="[required]")
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
    else:
        return parser.parse_args()


def start_instance(compute_client: ComputeClient, compartment_id: str):
    compute_list_response = compute_client.list_instances(compartment_id).data

    oke_worker_nodes = list(
        filter(lambda d: d.display_name.startswith('dreamkast'), compute_list_response))

    for worker_node in oke_worker_nodes:
        worker_nodes_id = worker_node.id
        instance_action_response = compute_client.instance_action(
            worker_nodes_id, "START").data
        print(instance_action_response.lifecycle_state +
              ": " + instance_action_response.display_name)


def main():
    args = parseInput()
    config = oci.config.from_file("~/.oci/config", "TOKYO")
    compartment_id = args.compartment_id
    compute_client = ComputeClient(config)
    start_instance(compute_client=compute_client,
                   compartment_id=compartment_id)
    print("DONE.")


if __name__ == "__main__":
    main()
