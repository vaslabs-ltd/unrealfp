"""Blueprint block example

Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name="K2Node_CallFunction_14" ExportPath="/Script/BlueprintGraph.K2Node_CallFunction'/Game/UnrealFPTesting/Docs.Docs:EventGraph.K2Node_CallFunction_14'"
   FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/UnrealFunctionalProgramming.Filter'",MemberName="Filter_By_Index_FString")
   NodePosX=336
   NodePosY=2112
   NodeGuid=A74EB14733394415A02A0D3745F84426
   CustomProperties Pin (PinId=BF1B82810E624ED8BAA2555AE7BBFC1B,PinName="execute",PinToolTip="\nExec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=73A1E04A9CF34C35B815ED141DCE9ABC,PinName="then",PinToolTip="\nExec",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=D4768432767F4118B91D6615814908A2,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinToolTip="Target\nFilter Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/UnrealFunctionalProgramming.Filter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/UnrealFunctionalProgramming.Default__Filter",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=109D24DEA566432985EDB0C0E689DABE,PinName="Array",PinToolTip="Array\nArray of Strings",PinType.PinCategory="string",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_VariableGet_10 C1D7D1E47FFB43B9BE974F66313A3675,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=31C2356FB0EC485282C1A2519C33D5D2,PinName="Predicate",PinToolTip="Predicate\nDelegate",PinType.PinCategory="delegate",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(MemberParent="/Script/CoreUObject.Package'/Script/UnrealFunctionalProgramming'",MemberName="FilterInt32Delegate__DelegateSignature"),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=7B46728E4FC643C4892A228262C52291,PinName="ReturnValue",PinToolTip="Return Value\nArray of Strings\n\nFilter by Index FString",Direction="EGPD_Output",PinType.PinCategory="string",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
"""


import uuid
from Blueprint import Blueprint, BlueprintInput, BlueprintList, BlueprintMetadata, BlueprintOutput

class SerializedBlueprint(object):
   def __init__(self, blueprint: Blueprint, raw: str):
      self.blueprint = blueprint
      self.raw = raw

def serialize_blueprints(blueprint_list: BlueprintList) -> SerializedBlueprint:
   member_parent = f"/Script/UnrealFunctionalProgramming.{blueprint_list.member_name}"
   serialized_objects = []
   for blueprint in blueprint_list.blueprints:
      raw = serialize_blueprint(member_parent, blueprint.name, blueprint)
      serialized_objects.append(SerializedBlueprint(blueprint, raw))
   
   return serialized_objects


def serialize_blueprint(member_parent: str, member_name: str, blueprint: Blueprint) -> str:
   guid = uuid.uuid4().hex.upper()
   return f"""{begin_object_class()}
   NodeGuid={guid}
   FunctionReference=(MemberParent="/Script/CoreUObject.Class'{member_parent}'",MemberName="{member_name}")
   {serialize_callable(blueprint.meta)}
   {serialize_input_properties(blueprint.inputs)}
   {serialize_output_properties(blueprint.outputs)}
   {end_object()}
   """.replace(",\n", ",").replace("   ", " ")


def serialize_callable(meta: BlueprintMetadata) -> str:
   if meta.is_pure:
      return ""
   elif meta.callable:
      return """CustomProperties Pin (PinId=BF1B82810E624ED8BAA2555AE7BBFC1B,PinName="execute",PinToolTip="\\nExec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=73A1E04A9CF34C35B815ED141DCE9ABC,PinName="then",PinToolTip="\\nExec",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)"""

def begin_object_class() -> str:
   return """Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name="K2Node_CallFunction" """

def end_object() -> str:
   return """End Object"""

def serialize_input_properties(inputs: list[BlueprintInput]) -> str:
   serialized_inputs = []
   for input in inputs:
      serialized_inputs.append(f"CustomProperties {serialize_input_property(input)}")
   return "\n".join(serialized_inputs)

def serialize_output_properties(outputs: list[BlueprintOutput]) -> str:
   serialized_outputs = []
   for output in outputs:
      if (output.type != "void"):
         serialized_outputs.append(f"CustomProperties {serialize_output_property(output)}")
   return "\n".join(serialized_outputs)

def serialize_output_property(output: BlueprintOutput) -> str:
   category = output.unreal_category
   if (output.delegate):
      return create_delegate_return_pin(output.GUID, output.delegate.name, "Connect a delegate function")
   else:
      return create_output_pin(output.GUID, "ReturnValue", "", category, output.unreal_container_type)

def serialize_input_property(input: BlueprintInput) -> str:
   if input.delegate is not None:
      return create_delegate_input_pin(input.GUID, input.name, "", input.delegate.name)
   category = input.unreal_category
   return create_input_pin(input.GUID, input.name, "", category, input.unreal_container_type, True, True)


def create_delegate_input_pin(id: str, name: str, tooltip: str, delegate_name: str) -> str:
   return f"""Pin (PinId={id},{pin_ref(name, tooltip)},{create_delegate_pin(delegate_name)})"""

def create_input_pin(pin_id: str, name: str, tooltip: str, category: str, container_type: str, is_reference: bool, is_const: bool) -> str:
   return f"""Pin (PinId={pin_id},{pin_ref(name, tooltip)},{create_in_pin(category, container_type, is_reference, is_const)})"""

def create_output_pin(pin_id: str, name: str, tooltip: str, category: str, container_type: str) -> str:
   return f"""Pin (PinId={pin_id},{pin_ref(name, tooltip)},{create_return_pin(category, container_type)})"""

def pin_ref(name: str, tooltip: str) -> str:
   return f"""PinName="{name}",PinToolTip="{tooltip}" """

def create_in_pin(category: str, container_type: str, is_reference: bool, is_const: bool) -> str:
   return f"""
   PinType.PinCategory="{category}",
   PinType.PinSubCategory="",
   PinType.PinSubCategoryObject=None,
   PinType.PinSubCategoryMemberReference=(),
   PinType.PinValueType=(),
   PinType.ContainerType={container_type},
   PinType.bIsReference={is_reference},
   PinType.bIsConst={is_const},
   PinType.bIsWeakPointer=False,
   PinType.bIsUObjectWrapper=False,
   PinType.bSerializeAsSinglePrecisionFloat=False
   """.replace(",\n", ",").replace("   ", " ")

def create_delegate_pin(delegate_name: str) -> str:
   return f"""
   PinType.PinCategory="delegate",
   PinType.PinSubCategory="",
   PinType.PinSubCategoryObject=None,
   PinType.PinSubCategoryMemberReference=(MemberParent="/Script/CoreUObject.Package'/Script/UnrealFunctionalProgramming'",
   MemberName="{delegate_name}__DelegateSignature"),PinType.PinValueType=(),
   PinType.ContainerType=None,
   PinType.bIsReference=False,
   PinType.bIsConst=False,
   PinType.bIsWeakPointer=False,
   PinType.bIsUObjectWrapper=False,
   PinType.bSerializeAsSinglePrecisionFloat=False,
   """.replace(",\n", ",").replace("   ", " ")


def create_delegate_return_pin(pin_id: str, delegate_name: str, tooltip: str) -> str:
   return f"""Pin (PinId={pin_id},PinName="ReturnValue",
PinToolTip="{tooltip}",
Direction="EGPD_Output",
PinType.PinCategory="delegate",PinType.PinSubCategory="",
PinType.PinSubCategoryObject=None,
PinType.PinSubCategoryMemberReference=(MemberParent="/Script/CoreUObject.Package'/Script/UnrealFunctionalProgramming'",
MemberName="{delegate_name}__DelegateSignature"),
PinType.PinValueType=(),
PinType.ContainerType=None,
PinType.bIsReference=False,
PinType.bIsConst=False,
PinType.bIsWeakPointer=False,
PinType.bIsUObjectWrapper=False,
PinType.bSerializeAsSinglePrecisionFloat=False,
PersistentGuid=00000000000000000000000000000000,bHidden=False,
bNotConnectable=False,bDefaultValueIsReadOnly=False,
bDefaultValueIsIgnored=False,
bAdvancedView=False,
bOrphanedPin=False,)""".replace(",\n", ",").replace("   ", " ")

def create_return_pin(category: str, container_type: str) -> str:
   return f"""Direction="EGPD_Output",
   PinType.PinCategory="{category}",
   PinType.PinSubCategory="",
   PinType.PinSubCategoryObject=None,
   PinType.PinSubCategoryMemberReference=(),
   PinType.PinValueType=(),
   PinType.ContainerType={container_type},
   PinType.bIsReference=False,
   PinType.bIsConst=False,
   PinType.bIsWeakPointer=False,
   PinType.bIsUObjectWrapper=False,
   PinType.bSerializeAsSinglePrecisionFloat=False,
   """.replace(",\n", ",").replace("   ", " ")


def custom_property_tail() -> str:
   return """PersistentGuid=00000000000000000000000000000000,
   bHidden=False,
   bNotConnectable=False,
   bDefaultValueIsReadOnly=False,
   bDefaultValueIsIgnored=False,
   bAdvancedView=False,
   bOrphanedPin=False,)""".replace(",\n", ",").replace("   ", " ")