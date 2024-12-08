unreal_types = {
   "FString": "string",
   "int32": "int",
   "int64": "int64",
   "float": "float",
   "bool": "bool",
   "void": "()"
}

class UnrealType(object):
    def __init__(self, type: str):
        self.type = type
        self.unreal_category = self.category(type)
        self.unreal_container_type = self.container_type(type)
        self.unreal_signature = self.unreal_signature_text(type)
        self.is_reference = type.endswith("&")

    def category(self, type) -> str:
        if type.startswith("TArray<"):
            category = type.split("<")[1].split(">")[0]
        elif type.endswith("&"):
            category = type[:-1] 
        else:
            category = type
        
        return unreal_types.get(category, 'object')
        
    def container_type(self, type) -> str:
        if type.startswith("TArray"):
            return "Array"
        else:
            return ""
    def unreal_signature_text(self, type: str) -> str:
        """if it's a container type, it removes the T in front and the generics
        e.g. TArray<int32> -> int -> Array by using the unreal_types dict as well
        and falling back to object if absent
        """
        if "<" in type and ">" in type:
            type_indicator = unreal_types.get(type.split("<")[1].split(">")[0], 'object')
            container = type.split("<")[0].lstrip("T")
            return f"{type_indicator} {container}"
        elif type.endswith("&"):
            type_indicator = type[:-1]
            return unreal_types.get(type_indicator, 'object')
        else:
            return unreal_types.get(type, 'object')