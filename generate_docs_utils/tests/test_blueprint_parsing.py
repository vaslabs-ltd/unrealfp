
from Blueprint import BlueprintOutput, parse_blueprint, parse_blueprints
from Delegate import Delegate, DelegateInput, DelegateKind, DelegateOutput

class TestBlueprintParsing:
    def test_blueprint_signature_is_parsed(self):
        pre_parsed_delegates = [
            Delegate("FForeachInt32Delegate", DelegateKind(False, 1), [DelegateInput("int32", "Element")], [])
        ]
        input = [
            """UFUNCTION(BlueprintCallable, Category = "Functional")""",
            """static void ForeachApply_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function);"""
        ]
        blueprint = parse_blueprint(pre_parsed_delegates, input)

        assert blueprint.meta.description == ""
        assert blueprint.meta.category == "Functional"
        assert blueprint.name == "ForeachApply_Int32"
        assert blueprint.meta.callable

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

        assert blueprint.outputs == [BlueprintOutput("void")]

    def test_blueprint_generic_function_output_is_read(self):
        pre_parsed_delegates = [
            Delegate("FForeachInt32Delegate", DelegateKind(False, 1), [DelegateInput("int32", "Element")], [])
        ]
        input = [
            """UFUNCTION(BlueprintCallable, Category = "Functional")""",
            """static TArray<int32> Map_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function);"""
        ]
        blueprint = parse_blueprint(pre_parsed_delegates, input)

        assert blueprint.outputs[0].type == "TArray<int32>"
        assert blueprint.outputs[0].unreal_signature == "int Array"

        assert blueprint.outputs == [BlueprintOutput("TArray<int32>")]

    
    def test_multiple_blueprint_blocks_are_parsed(self):
        input = [
            """UFUNCTION(BlueprintCallable, Category = "Functional")""",
            """static void ForeachApply_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function);""",
            """UFUNCTION(BlueprintCallable, Category = "Functional")""",
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
        assert blueprints[0].meta == expected_blueprint.meta
        assert blueprints[0].inputs == expected_blueprint.inputs
        assert blueprints[0].outputs == expected_blueprint.outputs

        expected_blueprint = parse_blueprint(pre_parsed_delegates, input[2:4])
        assert blueprints[1].name == expected_blueprint.name
        assert blueprints[1].meta == expected_blueprint.meta
        assert blueprints[1].inputs == expected_blueprint.inputs
        assert blueprints[1].outputs == expected_blueprint.outputs




        