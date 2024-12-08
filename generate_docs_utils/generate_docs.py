

from Delegate import Delegate
from read_header_file import parse_from_file
from export_to_unreal import serialize_blueprints, SerializedBlueprint

def unreal_engine_blocks(file: str, parsed_delegates: list[Delegate]) -> list[SerializedBlueprint]:
    with open(file, "r") as f:
        blueprint_list = parse_from_file(f, parsed_delegates)
        objects = serialize_blueprints(blueprint_list)

    return objects