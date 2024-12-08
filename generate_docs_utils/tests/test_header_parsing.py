
from Blueprint import parse_blueprints, BlueprintList
from Delegate import Delegate, DelegateInput, DelegateKind, DelegateOutput
from read_header_file import extract_blueprint_lines, extract_delegate_lines, parse_blueprints_from_lines
class TestHeaderParsing:
    test = """
            #pragma once
            #include "CoreMinimal.h"
            #include "UObject/Interface.h"
            #include "CoreMinimal.h"
            #include "Kismet/BlueprintFunctionLibrary.h"

            #include "Forall.generated.h"

            // ==================== FORALL =============================================

            UDELEGATE(BlueprintCallable)
            DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FForAllInt32Delegate, int32, Element);

            UCLASS()
            class UNREALFUNCTIONALPROGRAMMING_API UForall : public UBlueprintFunctionLibrary
            {
                GENERATED_BODY()

            public:
                // ================ FORALL ========================================
                UFUNCTION(BlueprintCallable, Category = "Functional")
                static bool ForAll_Int32(const TArray<int32>& Array, FForAllInt32Delegate Predicate);
            };
                    
        """
    def test_delegate_lines_are_extracted(self):
        
        delegate_lines = extract_delegate_lines(self.test.splitlines())
        assert len(delegate_lines) == 2
        for delegate_line in delegate_lines:
            assert delegate_line.startswith("UDELEGATE") or delegate_line.startswith("DECLARE_DYNAMIC_DELEGATE")

    def test_public_blueprint_lines_are_extracted(self):
        member_name, blueprint_lines = extract_blueprint_lines(self.test.splitlines())
        assert len(blueprint_lines) == 2
        assert member_name == "UForall"

    def test_blueprints_are_parsed(self):
        blueprintlist = parse_blueprints_from_lines(self.test.splitlines())
        blueprints = blueprintlist.blueprints
        
        assert blueprintlist.member_name == "Forall"
        assert len(blueprints) == 1
        assert blueprints[0].name == "ForAll_Int32"
        assert blueprints[0].meta.category == "Functional"
        assert blueprints[0].meta.description == ""
        assert blueprints[0].meta.callable
        assert len(blueprints[0].inputs) == 2
        assert blueprints[0].inputs[0].name == "Array"
        assert blueprints[0].inputs[0].type == "TArray<int32>&"
        assert blueprints[0].inputs[0].delegate == None
        assert blueprints[0].inputs[1].name == "Predicate"
        assert blueprints[0].inputs[1].type == "FForAllInt32Delegate"
        assert blueprints[0].inputs[1].delegate == Delegate("FForAllInt32Delegate", DelegateKind(True, 1), [DelegateInput("int32", "Element")], [DelegateOutput("bool")])
