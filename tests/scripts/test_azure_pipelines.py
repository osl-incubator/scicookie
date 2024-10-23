"""Test Azure Pipelines YAML files."""

import json
import sys

import yaml

from jsonschema import ValidationError, validate

print(sys.argv)
args = 3
if len(sys.argv) != args:
    print("Usage: python test_azure_pipelines.py <schema_file> <yaml_file>")
else:
    schema_file = sys.argv[1]
    yaml_file = sys.argv[2]

    with open(schema_file, "r") as f:
        schema = json.load(f)

    with open(yaml_file, "r") as f:
        yaml_data = yaml.safe_load(f)

    try:
        validate(instance=yaml_data, schema=schema)
        print(
            "The file {} is valid according to the schema {}.".format(
                yaml_file, schema_file
            )
        )
    except ValidationError as e:
        print(f"The file {yaml_file} is invalid:\n {e}")
