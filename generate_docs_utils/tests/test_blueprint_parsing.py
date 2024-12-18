
from Blueprint import BlueprintOutput, parse_blueprint, parse_blueprints
from Delegate import Delegate, DelegateInput, DelegateKind, DelegateOutput, parse_delegate, parse_delegates

class TestBlueprintParsing:
    def test_blueprint_signature_is_parsed(self):
        pre_parsed_delegates = [
            Delegate("FForeachInt32Delegate", DelegateKind(False, 1), [DelegateInput("int32", "Element")], [])
        ]
        input = [
            """UFUNCTION(BlueprintPure, Category = "Functional")""",
            """static void ForeachApply_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function);"""
        ]
        blueprint = parse_blueprint(pre_parsed_delegates, input)

        assert blueprint.meta.description.description == ""
        assert blueprint.meta.category == "Functional"
        assert blueprint.name == "ForeachApply_Int32"
        assert blueprint.meta.is_pure

        assert len(blueprint.inputs) == 2
        assert blueprint.inputs[0].name == "Array"
        assert blueprint.inputs[0].type == "TArray<int32>&"
        assert blueprint.inputs[0].delegate == None
        assert blueprint.inputs[0].is_const == True
        assert blueprint.inputs[0].is_reference == True
        assert blueprint.outputs[0].type == "void"

        assert blueprint.inputs[1].name == "Function"
        assert blueprint.inputs[1].type == "FForeachInt32Delegate"
        assert blueprint.inputs[1].delegate == pre_parsed_delegates[0]

        assert blueprint.outputs == [BlueprintOutput("void", None)]

    def test_blueprint_generic_function_output_is_read(self):
        pre_parsed_delegates = [
            Delegate("FForeachInt32Delegate", DelegateKind(False, 1), [DelegateInput("int32", "Element")], [])
        ]
        input = [
            """UFUNCTION(BlueprintCallable, Category = "Functional")""",
            """static TArray<int32> Map_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function);"""
        ]
        blueprint = parse_blueprint(pre_parsed_delegates, input)

        assert not blueprint.meta.is_pure
        assert blueprint.outputs[0].type == "TArray<int32>"
        assert blueprint.outputs[0].unreal_signature == "int Array"

        assert blueprint.outputs == [BlueprintOutput("TArray<int32>", None)]

        input = [
            """UFUNCTION(BlueprintPure, Category = "Functional")""",
            """static TArray<int32> Map_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function);"""
        ]
        blueprint = parse_blueprint(pre_parsed_delegates, input)
        assert blueprint.meta.is_pure

    def test_blueprint_parses_comments(self):
        input = [
                "/**", 
                "* Concatenates the elements of an int32 array into a single FString, separated by the specified separator.",
                "* ",
                "* @param Array The input array of integers.",
                "* @param Separator The string to insert between each element.*/",
                """UFUNCTION(BlueprintPure, Category = "Functional|Arrays")""",
                "static FString MkString_Int32(const TArray<int32>& Array, const FString& Separator);"
        ]

        blueprint = parse_blueprint([], input)
        assert blueprint.meta.description.description == "Concatenates the elements of an int32 array into a single FString, separated by the specified separator."
        assert blueprint.meta.description.param_descriptions["Array"] == "The input array of integers."
        assert blueprint.meta.description.param_descriptions["Separator"] == "The string to insert between each element."

        input = [
                """/** ForeachApply for int32 arrays */""",
                """UFUNCTION(BlueprintPure, Category = "Functional")""",
                """static void ForeachApply_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function);"""

        ]

        blueprint = parse_blueprint([], input)
        assert blueprint.meta.description.description == "ForeachApply for int32 arrays"


    def test_blueprint_fstring_input(self):
        input = [
            """UFUNCTION(BlueprintPure, Category = "Functional|Arrays")""",
            """static FString MkString(const TArray<FString>& Array, const FString& Separator);"""
        ]
        blueprint = parse_blueprint([], input)
        assert blueprint.inputs[0].unreal_category == "string"
        assert blueprint.inputs[0].is_const
        assert blueprint.inputs[0].is_reference == True
        assert blueprint.inputs[0].delegate is None
        assert blueprint.outputs[0].unreal_category == "string"
    
    def test_multiple_blueprint_blocks_are_parsed(self):
        input = [
            """UFUNCTION(BlueprintPure, Category = "Functional")""",
            """static void ForeachApply_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function);""",
            """UFUNCTION(BlueprintPure, Category = "Functional")""",
            """static TArray<int32> MapApply_Int32(const TArray<int32>& Array, FMapInt32ToInt32Delegate Function);""",
            """static void ForeachApply_Int32(const TArray<bool>& Array, FForeachInt32Delegate Function);""", # ingored
            """static void ForeachApply_Int32(const TArray<int64>& Array, FForeachInt32Delegate Function);""" #ignored
        ]

        pre_parsed_delegates = [
            Delegate("FForeachInt32Delegate", DelegateKind(False, 1), [DelegateInput("int32", "Element")], []),
            Delegate("FMapInt32ToInt32Delegate", DelegateKind(True, 1), [DelegateInput("int32", "Element")], [DelegateOutput("int32")])
        ]

        blueprints = parse_blueprints(pre_parsed_delegates, input)

        assert len(blueprints) == 2
        expected_blueprint = parse_blueprint(pre_parsed_delegates, input[0:2])

        assert blueprints[0].name == expected_blueprint.name
        assert blueprints[0].meta.category == expected_blueprint.meta.category
        assert blueprints[0].meta.description.description == expected_blueprint.meta.description.description
        assert blueprints[0].meta.description.param_descriptions == expected_blueprint.meta.description.param_descriptions
        assert blueprints[0].inputs == expected_blueprint.inputs
        assert blueprints[0].outputs == expected_blueprint.outputs

        expected_blueprint = parse_blueprint(pre_parsed_delegates, input[2:4])
        assert blueprints[1].name == expected_blueprint.name
        assert blueprints[1].meta.description.description == expected_blueprint.meta.description.description
        assert blueprints[1].meta.category == expected_blueprint.meta.category
        assert blueprints[1].meta.description.param_descriptions == expected_blueprint.meta.description.param_descriptions
        assert blueprints[1].inputs == expected_blueprint.inputs
        assert blueprints[1].outputs == expected_blueprint.outputs

    def test_recognises_output_delegate(self):
        input = [
                """UFUNCTION(BlueprintPure, Category = "Functional|Delegates")""",
                """static FMapVectorParameterValueToLinearColorDelegate GetVectorParamValueToLinearColorDelegate();"""
        ]

        parsed_delegates = [
            """UDELEGATE(BlueprintPure)""",
            """DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(FLinearColor, FMapVectorParameterValueToLinearColorDelegate, FVectorParameterValue, Element);"""
        ]

        pre_parsed_delegates = parse_delegates(parsed_delegates)

        blueprints = parse_blueprints(pre_parsed_delegates, input)

        assert len(blueprints) == 1
        assert blueprints[0].inputs == []
        assert blueprints[0].outputs == [BlueprintOutput("FMapVectorParameterValueToLinearColorDelegate", pre_parsed_delegates[0])]





        