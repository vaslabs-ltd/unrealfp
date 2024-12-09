
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
        assert blueprints[0].meta.description.description == ""
        assert blueprints[0].meta.description.param_descriptions == {}
        assert blueprints[0].meta.callable
        assert len(blueprints[0].inputs) == 2
        assert blueprints[0].inputs[0].name == "Array"
        assert blueprints[0].inputs[0].type == "TArray<int32>&"
        assert blueprints[0].inputs[0].delegate == None
        assert blueprints[0].inputs[1].name == "Predicate"
        assert blueprints[0].inputs[1].type == "FForAllInt32Delegate"
        assert blueprints[0].inputs[1].delegate == Delegate("FForAllInt32Delegate", DelegateKind(True, 1), [DelegateInput("int32", "Element")], [DelegateOutput("bool")])

    test_with_comments = """
        #pragma once

        #include "CoreMinimal.h"
        #include "UObject/Interface.h"
        #include "CoreMinimal.h"
        #include "Kismet/BlueprintFunctionLibrary.h"
        #include "Components/Button.h" // Include for UButton
        #include "Functions.h"

        #include "Arrays.generated.h"

        UCLASS()
        class UNREALFUNCTIONALPROGRAMMING_API UArrays : public UBlueprintFunctionLibrary
        {
            GENERATED_BODY()

        public:

            /**
            * Generates an array of integers by applying a function to the index of the given range
            * and returns the resulting array.
            * 
            * @param Start The starting index of the range.
            * @param End The ending index of the range exclusive.
            */
            UFUNCTION(BlueprintCallable, Category = "Functional")
            static TArray<int32> Generate_ArrayInt32(int32 Start, int32 End, FInt32Int32Delegate Function);

            /**
            * Generates an array of integers by applying a function to an input integer and the index of the given range
            * and returns the resulting array.
            * 
            * @param Feed The input integer to be used in the function.
            * @param Start The starting index of the range.
            * @param End The ending index of the range exclusive.
            */
            UFUNCTION(BlueprintCallable, Category = "Functional")
            static TArray<int32> Generate_ArrayInt32FromInt32(int32 Feed, int32 Start, int32 End, FInt32Int32ToInt32Delegate Function);

            /**
            * Merges two arrays of the same type into a new array without modifying the originals.
            * This function is immutable and similar to the built-in "Append Array" node.
            *
            * @param ArrayA The first input array.
            * @param ArrayB The second input array.
            * @param Result The resulting merged array.
            */
            UFUNCTION(BlueprintCallable, CustomThunk, meta = (CustomStructureParam = "ArrayA,ArrayB,Result"), Category = "Functional|Arrays")
            static void Merge_Any(const FGenericStruct& ArrayA, const FGenericStruct& ArrayB, FGenericStruct& Result);

            DECLARE_FUNCTION(execMerge_Any);

            /**
            * Concatenates the elements of an array into a single FString, separated by the specified separator.
            * This function is immutable and does not modify the input array.
            *
            * @param Array The input array of FStrings.
            * @param Separator The string to insert between each element.
            */
            UFUNCTION(BlueprintCallable, Category = "Functional|Arrays")
            static FString MkString(const TArray<FString>& Array, const FString& Separator);

            /** Concatenates the elements of an int32 array into a single FString, separated by the specified separator.*/
            UFUNCTION(BlueprintCallable, Category = "Functional|Arrays")
            static FString MkString_Int32(const TArray<int32>& Array, const FString& Separator);
        };
"""

    def tests_blueprint_comments_are_extracted(self):
        member_name, blueprint_lines = extract_blueprint_lines(self.test_with_comments.splitlines())
        comments_per_blueprint = [7, 8, 8, 7, 1]
        assert len(blueprint_lines) == sum(comments_per_blueprint) + 2*len(comments_per_blueprint)
        assert member_name == "UArrays"

        for i in range(1, comments_per_blueprint[0]):
            assert '/**' in blueprint_lines[i] or '*' in blueprint_lines[i] or '*/' in blueprint_lines[i]
        
        assert blueprint_lines[comments_per_blueprint[0]] == "UFUNCTION(BlueprintCallable, Category = \"Functional\")"
        assert blueprint_lines[comments_per_blueprint[0] + 1] == "static TArray<int32> Generate_ArrayInt32(int32 Start, int32 End, FInt32Int32Delegate Function);"

        blueprintlist = parse_blueprints_from_lines(self.test_with_comments.splitlines())
        
        blueprints = blueprintlist.blueprints
        assert len(blueprints) == len(comments_per_blueprint)

        assert blueprints[1].meta.description.description.startswith("""Generates an array of integers by applying""")
        assert blueprints[1].meta.description.param_descriptions == {
            "Feed": "The input integer to be used in the function.",
            "Start": "The starting index of the range.", 
            "End": "The ending index of the range exclusive."
        }
