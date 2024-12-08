

from typing import TextIO

from Blueprint import Blueprint, BlueprintList, parse_blueprints
from Delegate import Delegate, parse_delegates


  
def extract_delegate_lines(lines: list[str]) -> list[str]:
    delegate_lines = []
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line.startswith("UDELEGATE") or cleaned_line.startswith("DECLARE_DYNAMIC_DELEGATE"):
            delegate_lines.append(cleaned_line)
    return delegate_lines
    
def extract_blueprint_lines(lines: list[str]):
    public_started = False
    next_line_is_blueprint = False
    next_line_is_class_line = False
    blueprint_lines = []
    class_line = ""
    for line in lines:
        cleaned_line = line.strip()
        if (public_started):
            if (not next_line_is_blueprint and cleaned_line.startswith("UFUNCTION")):
                next_line_is_blueprint = True
                blueprint_lines.append(cleaned_line)
            elif (next_line_is_blueprint):
                next_line_is_blueprint = False
                blueprint_lines.append(cleaned_line)
            elif (cleaned_line.startswith("};") or cleaned_line.startswith("private:")):
                public_started = False
        elif (cleaned_line.startswith("public:")):
            public_started = True
        elif (not next_line_is_class_line and cleaned_line.startswith("UCLASS()")):
                next_line_is_class_line = True
        elif next_line_is_class_line:
                next_line_is_class_line = False
                class_line = cleaned_line
    member_name = member_name_from_class_line(class_line)


    return member_name, blueprint_lines

def parse_blueprints_from_lines(lines: list[str], delegates: list[Delegate] = []) -> BlueprintList:
    delegate_lines = extract_delegate_lines(lines)
    member_name, blueprint_lines = extract_blueprint_lines(lines)
    
    if (len(delegates) == 0):
        pre_parsed_delegates = parse_delegates(delegate_lines)
    else:
        pre_parsed_delegates = delegates

    return BlueprintList(member_name, parse_blueprints(pre_parsed_delegates, blueprint_lines))

def parse_from_file(file: TextIO, delegates: list[Delegate] = []) -> BlueprintList:
    return parse_blueprints_from_lines(file.readlines(), delegates)


def member_name_from_class_line(class_line: str) -> str:
    """
    Parses the class name from class line such as
    class UNREALFUNCTIONALPROGRAMMING_API UExists : public UBlueprintFunctionLibrary
    and returns it as the member name
    """
    if class_line == "":
        return class_line
    parts = class_line.strip().split(" ")
    return parts[2]