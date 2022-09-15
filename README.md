# oci-scripts

## usage

<!-- @import "[TOC]" {cmd="toc" depthFrom=3 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [start-oke-worker-node](#start-oke-worker-node)
- [delete-oke-quickstart-vcn](#delete-oke-quickstart-vcn)

<!-- /code_chunk_output -->

### start-oke-worker-node

```bash
$ python3 start-oke-worker-node.py --help
usage: start-oke-worker-node.py [-h] [--compartment-id COMPARTMENT_ID] [--profile PROFILE]

OKE Worker Node START Script.

options:
  -h, --help                       show this help message and exit
  --compartment-id COMPARTMENT_ID  [required]
  --profile PROFILE                [optional]
```

### delete-oke-quickstart-vcn

```bash
$ python3 delete-oke-quickstart-vcn.py --help
usage: delete-oke-quickstart-vcn.py [-h] [--compartment-id COMPARTMENT_ID] [--vcn-id VCN_ID] [--profile PROFILE]

OKE Worker Node START Script.

options:
  -h, --help                       show this help message and exit
  --compartment-id COMPARTMENT_ID  [required]
  --vcn-id VCN_ID                  [required]
  --profile PROFILE                [optional]
```