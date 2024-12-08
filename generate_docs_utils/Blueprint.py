

from typing import Optional
from Delegate import Delegate
import uuid

from UnrealType import UnrealType

class BlueprintMetadata(object):
    def __init__(self, category: str, description: str, callable: bool):
        self.category = category
        self.description = description
        self.callable = callable

    def __str__(self):
        return f'BlueprintMetadata(category={self.category}, description={self.description}, callable={self.callable})'

    def __eq__(self, value):
        return value.category == self.category and value.description == self.description and value.callable == self.callable

class TypeWrapper(UnrealType):

    def __init__(self, type: str):
        super().__init__(type)

class BlueprintInput(UnrealType):
    def __init__(self, type: str, name: str, is_const, delegate: Optional[Delegate]):
        super().__init__(type)
        self.name = name
        self.delegate = delegate
        self.is_const = is_const
        self.GUID = uuid.uuid4().hex.upper()
        self.unreal_category = self.category(type, delegate)

    def __eq__(self, value):
        if (value == None):
            return False
        return value.name == self.name and value.type == self.type and value.is_const == self.is_const and value.is_reference == self.is_reference and value.delegate == self.delegate

    def category(self, type: str, delegate: Optional[Delegate] = None) -> str:
        if delegate:
            return f"Delegate"
        else:
            return super().category(type)

class BlueprintOutput(UnrealType):
    def __init__(self, type: str):
        super().__init__(type)
        self.GUID = uuid.uuid4().hex.upper()
        self.unreal_signature = self.unreal_signature_text(type)

    def __str__(self):
        return f'BlueprintOutput(type={self.type})'

    def __eq__(self, value):
        if (value == None):
            return False
        return value.type == self.type


class Blueprint(object):
    def __init__(self, name: str, meta: BlueprintMetadata, inputs: list[BlueprintInput], outputs: list[BlueprintOutput]):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.meta = meta

class BlueprintList(object):
    def __init__(self, member_name: str, blueprints: list[Blueprint]):
        if member_name.startswith("U"):
            self.member_name = member_name[1:]
        else:
            self.member_name = member_name
        self.blueprints = blueprints

def parse_blueprints(pre_parsed_delegates: list[Delegate], lines: list[str]) -> list[Blueprint]:
    """
        Parses all blueprints from header file that have a line UFUNCTION above them,
        ignores the rest
    """
    blueprint_lines = _clean_blueprint_lins(lines)
    blueprints = []
    for i in range(0, len(blueprint_lines), 2):
        blueprints.append(parse_blueprint(pre_parsed_delegates, blueprint_lines[i:i+2]))

    return blueprints

def _clean_blueprint_lins(lines: list[str]) -> tuple[str, list[str]]:
    next_line_is_blueprint = False
    cleaned_lines = []
    for line in lines:
        cleaned_line = line.strip()
        if (not next_line_is_blueprint and cleaned_line.startswith("UFUNCTION")):
            next_line_is_blueprint = True
            cleaned_lines.append(cleaned_line)
        elif (next_line_is_blueprint):
            next_line_is_blueprint = False
            cleaned_lines.append(cleaned_line)
    return cleaned_lines

def parse_blueprint(pre_parsed_delegates, lines: list[str]) -> Blueprint:
    meta = parse_blueprint_metadata(lines[0])
    blueprint = parse_blueprint_line(pre_parsed_delegates, meta, lines[1])
    return blueprint

def parse_blueprint_metadata(line: str) -> BlueprintMetadata:
    """
    Parses contents of UFUNCTION(BlueprintCallable, Category = "Functional")
    into BlueprintMetadata
    """
    startingBlueprintFunction = "UFUNCTION("
    endingBlueprintFunction = ")"
    endingIndex = line.rindex(endingBlueprintFunction)

    if not line.startswith(startingBlueprintFunction):
        raise ValueError(f"Expected line to start with {startingBlueprintFunction}")
    
    effective_line = line[len(startingBlueprintFunction):endingIndex]

    blueprint_metadata_parts = list(map(lambda x: x.strip(), effective_line.split(",")))
    callable = blueprint_metadata_parts[0] == "BlueprintCallable"
    category = ""
    description = ""
    for blueprint_metadata_part in blueprint_metadata_parts[1:]:
        if blueprint_metadata_part.find("="):
            parts = blueprint_metadata_part.split("=")
            parameter = parts[0].strip()
            if parameter == "Category":
                category = parts[1].strip().strip("\"")
            elif parameter == "ToolTip":
                description = parts[1].strip()
                
            # add more metadata here

    return BlueprintMetadata(category, description, callable)


def parse_blueprint_line(pre_parsed_delegates: list[Delegate], meta: BlueprintMetadata, line: str) -> Blueprint:
    """
    Parses static void ForeachApply_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function);
    into a Blueprint object
    """
    # tokenize line
    parts = line.split("(")
    signature = parts[0].strip()
    parameters = parts[1].strip()[:-2].strip()
    parameters_parts = parameters.split(",")
    method_details = signature.split(" ")
    method_name = ""
    method_type = ""
    for detail in method_details[::-1]:
        if detail != "" and method_name == "":
            method_name = detail
        elif method_name != "" and method_type == "" and detail != "":
            method_type = detail
    
    inputs = parse_blueprint_inputs(pre_parsed_delegates, parameters_parts)
    output = BlueprintOutput(method_type)

    return Blueprint(method_name, meta, inputs, [output])


def parse_blueprint_inputs(pre_parsed_delegate: list[Delegate], parameters_parts: list[str]) -> list[BlueprintInput]:
    inputs = []
    for parameter in parameters_parts[::-1]:
        cleaned_parameter = parameter.strip()
        if cleaned_parameter == "":
            continue
        inputs.insert(0, parse_blueprint_input(pre_parsed_delegate, cleaned_parameter))
    return inputs


def parse_blueprint_input(pre_parsed_delegate: list[Delegate], parameter: str) -> BlueprintInput:
    parts = parameter.split(" ")
    
    name = ""
    type = ""
    is_const = False

    for part in parts[::-1]:
        if (name == ""):
            name = part
        elif (type == ""):
            type = part
        else:
            if (part == "const"):
                is_const = True

    input_delegate = None
    for delegate in pre_parsed_delegate:
        if delegate.name == type:
            input_delegate = delegate
            break
    return BlueprintInput(name=name, type=type, is_const=is_const, delegate=input_delegate)
