
from UnrealType import UnrealType


class DelegateKind(object):
    def __init__(self, hasRetVal, numParams):
        self.hasRetVal = hasRetVal
        self.numParams = numParams

    def __str__(self):
        return f'DelegateKind(kindStr={self.kindStr}, hasRetVal={self.hasRetVal}, numParams={self.numParams})'

    def __eq__(self, value):
        return value.hasRetVal == self.hasRetVal and value.numParams == self.numParams

class DelegateInput(UnrealType):
    def __init__(self, type, name):
        super().__init__(type)
        self.name = name

    def __str__(self):
        return f'DelegateInput(type={self.type}, name={self.name})'
    
    def __eq__(self, value):
        if (value == None):
            return False
        return value.type == self.type and value.name == self.name
    
class DelegateOutput(UnrealType):
    def __init__(self, type):
        super().__init__(type)
        self.type = type

    def __str__(self):
        return f'DelegateOutput(type={self.type})'
    
    def __eq__(self, value):
        return value.type == self.type

class Delegate(object):
    def __init__(self, name: str, kind: DelegateKind, inputs: list[DelegateInput], outputs: list[DelegateOutput]):
        self.inputs = inputs
        self.outputs = outputs
        self.kind = kind
        self.name = name
        self.unreal_signature = f"{format_inputs(inputs)} => {format_outputs(outputs)}"

    def __str__(self):
        return f'Delegate(name={self.name}, description={self.description}, inputs={self.inputs}, outputs={self.outputs})'

    def __eq__(self, value):
        if (value == None):
            return False
        return value.name == self.name and value.kind == self.kind and value.inputs == self.inputs and value.outputs == self.outputs

def parse_delegates(lines: list[str]) -> list[Delegate]:
    """
    Parses all delegates from a header file, lines representation.
    Picks up every line under UDELEGATE
    and parses the delegate out of it
    """
    delegates = []
    next_line_is_delegate = False
    for line in lines:
        if (not next_line_is_delegate and line.startswith("UDELEGATE")):
            next_line_is_delegate = True
        elif (next_line_is_delegate):
            next_line_is_delegate = False
            delegate = parse_delegate(line)
            delegates.append(delegate)
    return delegates
        
def format_inputs(inputs: list[DelegateInput]):
    """ format inputs in the form of field_type, ..."""
    return ", ".join([f"{input.unreal_signature}" for input in inputs])

def format_outputs(outputs: list[DelegateOutput]):
    """ format outputs in the form of field_type, ..."""
    if not outputs:
        return "()"
    return ", ".join([output.unreal_signature for output in outputs])

def parse_delegate(delegateLine: str):
    """
    Parses delegate line such as
    DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FFilterInt32Delegate, int32, Element);
    or 
    DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachInt64Delegate, int64, Element);
    into a Delegate object
    """
    delegateKind = parse_delegate_kind(delegateLine)
    delegate = parse_delegate_signature(delegateLine, delegateKind)
    return delegate

DELEGATE_INDICATOR = "DECLARE_DYNAMIC_DELEGATE"


def parse_delegate_signature(delegateLine: str, delegateKind: DelegateKind) -> Delegate:
    """
    Parses the delegate signature from the delegate line
    DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FFilterInt32Delegate, int32, Element);
    or 
    DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachInt64Delegate, int64, Element);
    """
    partsStartFrom = delegateLine.index('(')
    partsStr = delegateLine[partsStartFrom+1:-2]
    parts = partsStr.split(',')
    inputs = []
    outputs = []
    if (delegateKind.hasRetVal):
        outputs.append(DelegateOutput(parts[0].strip()))
        delegate_name = parts[1].strip()
        startFrom = 2
    else:
        delegate_name = parts[0].strip()
        startFrom = 1
    for i in range(startFrom, len(parts), 2):
        type = parts[i].strip()
        name = parts[i+1].strip()
        inputs.append(DelegateInput(type, name))


    return Delegate(delegate_name, delegateKind, inputs, outputs)


def parse_delegate_kind(kindStr: str) -> str:
    """
    Parses the kind of delegate from the kind string
    DECLARE_DYNAMIC_DELEGATE_OneParam
    DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam
    """
    if (kindStr.startswith(DELEGATE_INDICATOR)):
        partsStartFrom = kindStr.index('(')
        kindIndicatorStr = kindStr[len(DELEGATE_INDICATOR)+1:partsStartFrom]
        kindIndicatorParts = kindIndicatorStr.split('_')
        return parse_kind(kindIndicatorParts)

    else:
        raise Exception(f'Unknown delegate kind: {kindStr}')


recognisedParams = {
    "OneParam": 1,
    "TwoParams": 2,
    "ThreeParams": 3
}


def parse_kind(kindIndicatorParts: list) -> DelegateKind:
    """
    Parses the kind of delegate from the kind indicator parts
    OneParam
    RetVal_OneParam
    RetVal_TwoParams
    TwoParams
    etc
    supporting up to recognisedParams, add more in the dictionary
    to support more
    """
    if (len(kindIndicatorParts) == 0):
        return DelegateKind(False, 0)
    elif (kindIndicatorParts[0] == "RetVal"):
        if (len(kindIndicatorParts) == 2):
            return DelegateKind(True, recognisedParams[kindIndicatorParts[1]])
        else:
            return DelegateKind(True, 0)
    else:
        return DelegateKind(False, recognisedParams[kindIndicatorParts[0]])