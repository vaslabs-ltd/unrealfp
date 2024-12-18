

from typing import Optional
from Delegate import Delegate
import uuid

from UnrealType import UnrealType

class BlueprintDescription(object):
    def __init__(self, description: str, param_descriptions: dict[str, str]):
        self.description = description
        self.param_descriptions = param_descriptions

class BlueprintMetadata(object):
    def __init__(self, category: str, description: BlueprintDescription, callable: bool, is_pure: bool):
        self.category = category
        self.description = description
        self.callable = callable
        self.is_pure = is_pure

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
    def __init__(self, type: str, delegate: Optional[Delegate]):
        super().__init__(type)
        self.GUID = uuid.uuid4().hex.upper()
        self.unreal_signature = self.unreal_signature_text(type)
        self.delegate = delegate

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
    comment_counters, blueprint_lines = _clean_blueprint_lines(lines)
    blueprints = []
    lines_read = 0
    for comment_counter in comment_counters:
        next_chunk_size = lines_read + comment_counter + 2
        blueprint_chunk = blueprint_lines[lines_read:next_chunk_size]
        lines_read = next_chunk_size
        blueprints.append(parse_blueprint(pre_parsed_delegates, blueprint_chunk))

    return blueprints

def _clean_blueprint_lines(lines: list[str]) -> tuple[list[int], list[str]]:
    next_line_is_blueprint = False
    reading_doc_comments = False
    has_comments = False
    cleaned_lines: list[str] = []
    comment_lines: list[int] = []
    comment_counter = 0
    for line in lines:
        cleaned_line = line.strip()
        if (not next_line_is_blueprint and cleaned_line.startswith("/**")):
            reading_doc_comments = True
            comment_counter = 1
            cleaned_lines.append(cleaned_line)
            has_comments = True
            if (cleaned_line.endswith("*/")):
                reading_doc_comments = False
                comment_lines.append(comment_counter)
                comment_counter = 0
        elif reading_doc_comments:
            cleaned_lines.append(cleaned_line)
            comment_counter += 1
            if (cleaned_line.endswith("*/")):
                reading_doc_comments = False
                comment_lines.append(comment_counter)
                comment_counter = 0
        elif (not next_line_is_blueprint and cleaned_line.startswith("UFUNCTION")):
            next_line_is_blueprint = True
            cleaned_lines.append(cleaned_line)
            if not has_comments:
                comment_lines.append(0)
        elif (next_line_is_blueprint):
            next_line_is_blueprint = False
            cleaned_lines.append(cleaned_line)
    return comment_lines, cleaned_lines

def parse_blueprint(pre_parsed_delegates, lines: list[str]) -> Blueprint:
    description = read_doc_comments_if_any(lines)
    blueprint_lines = skip_comments(lines)
    meta = parse_blueprint_metadata(blueprint_lines[0], description)
    blueprint = parse_blueprint_line(pre_parsed_delegates, meta, blueprint_lines[1])
    return blueprint

def skip_comments(lines: list[str]) -> list[str]:
    offset = 0
    start_skipping = False
    for i, line in enumerate(lines):
        cleaned_line = line.strip()
        if (not start_skipping and cleaned_line.startswith("/**")):
            start_skipping = True
            if (cleaned_line.endswith("*/")):
                offset = i + 1
                break
        elif (start_skipping):
            if (cleaned_line.endswith("*/")):
                offset = i + 1
                break
    return lines[offset:]

def read_doc_comments_if_any(lines: list[str]) -> str:
    """
    Reads doc comments from a list of lines
    """
    comments = []
    comments_follow = False
    description = ""
    param_descriptions = {}
    for line in lines:
        cleaned_line = line.strip()        
        if (not comments_follow and cleaned_line.startswith("/**")):
            comments_follow = True
            if cleaned_line.endswith("*/"):
                comments.append(cleaned_line.rstrip("/**").lstrip("*/"))
                comments_follow = False
        elif (comments_follow):
            text_line = cleaned_line.lstrip("*").rstrip("*/").strip()
            if (text_line.startswith("@param")):
                cleaned_text_line = text_line.rstrip("*/")
                parts = cleaned_text_line.split(" ")
                param_name = parts[1]
                param_description = " ".join(parts[2:])
                param_descriptions[param_name] = param_description
            else:
                comments.append(text_line)
            if (cleaned_line.endswith("*/")):
                comments_follow = False
    description = "\n".join(filter(lambda x: len(x.strip()) > 0, comments))
    return BlueprintDescription(description.strip(), param_descriptions)


def parse_blueprint_metadata(line: str, description: BlueprintDescription) -> BlueprintMetadata:
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
    is_pure = blueprint_metadata_parts[0] == "BlueprintPure"
    category = ""
    for blueprint_metadata_part in blueprint_metadata_parts[1:]:
        if blueprint_metadata_part.find("="):
            parts = blueprint_metadata_part.split("=")
            parameter = parts[0].strip()
            if parameter == "Category":
                category = parts[1].strip().strip("\"")

            # add more metadata here

    return BlueprintMetadata(category, description, callable, is_pure)


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
    delegate = list(filter(lambda x: x.name == method_type, pre_parsed_delegates))
    if len(delegate) > 0:
        output = BlueprintOutput(method_type, delegate.pop())
    else:
        output = BlueprintOutput(method_type, None)
        
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
