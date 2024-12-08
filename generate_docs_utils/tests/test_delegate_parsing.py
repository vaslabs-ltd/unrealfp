from Delegate import Delegate, DelegateInput, DelegateKind, DelegateOutput, parse_delegate, parse_delegates

## run pytest unit tests
class TestDelegateParsing:
    def test_delegate_no_return_val_one_param(self):
        input = "DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachInt64Delegate, int64, Element);"
        delegate: Delegate = parse_delegate(input)
        assert delegate.inputs == [DelegateInput("int64", "Element")]
        assert delegate.inputs[0].unreal_signature == "int64"
        assert delegate.outputs == []
        assert delegate.kind == DelegateKind(False, 1)
        assert delegate.name == "FForeachInt64Delegate"

    def test_delegate_return_val_one_param(self):
        input = "DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FFilterInt32Delegate, int32, Element);"
        delegate: Delegate = parse_delegate(input)
        assert delegate.inputs == [DelegateInput("int32", "Element")]
        assert delegate.outputs == [DelegateOutput("bool")]
        assert delegate.kind == DelegateKind(True, 1)
        assert delegate.name == "FFilterInt32Delegate"

    def test_delegate_return_val_two_params(self):
        input = "DECLARE_DYNAMIC_DELEGATE_RetVal_TwoParams(bool, FFilterInt32Delegate, int32, Element, int32, Element2);"
        delegate: Delegate = parse_delegate(input)
        assert delegate.inputs == [DelegateInput("int32", "Element"), DelegateInput("int32", "Element2")]
        assert delegate.outputs == [DelegateOutput("bool")]
        assert delegate.kind == DelegateKind(True, 2)
        assert delegate.name == "FFilterInt32Delegate"

    def parsesAllDelegates(self):
        input = [
            "UDELEGATE(BlueprintCallable)",
            "DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachInt64Delegate, int64, Element);",
            "",
            "UDELEGATE(BlueprintCallable)",
            "DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FFilterInt32Delegate, int32, Element);",
            "UDELEGATE(BlueprintCallable)",
            "DECLARE_DYNAMIC_DELEGATE_RetVal_TwoParams(bool, FFilterInt32Delegate, int32, Element, int32, Element2);",
            "UDELEGATE(BlueprintCallable)",
            "DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachInt64Delegate, int64, Element);",
        ]
        delegates = parse_delegates(input)
        assert len(delegates) == 4
        assert delegates[0] == parse_delegate(input[1])
        assert delegates[1] == parse_delegate(input[4])
        assert delegates[2] == parse_delegate(input[6])
        assert delegates[3] == parse_delegate(input[8])
        
