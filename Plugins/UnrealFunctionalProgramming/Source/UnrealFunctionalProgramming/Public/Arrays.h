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
    UFUNCTION(BlueprintPure, Category = "Functional")
    static TArray<int32> Generate_ArrayInt32(int32 Start, int32 End, FInt32Int32Delegate Function);

    /**
     * Generates an array of integers by applying a function to an input integer and the index of the given range
     * and returns the resulting array.
     * 
     * @param Feed The input integer to be used in the function.
     * @param Start The starting index of the range.
     * @param End The ending index of the range exclusive.
     */
    UFUNCTION(BlueprintPure, Category = "Functional")
    static TArray<int32> Generate_ArrayInt32FromInt32(int32 Feed, int32 Start, int32 End, FInt32Int32ToInt32Delegate Function);

    /**
     * Merges two arrays of the same type into a new array without modifying the originals.
     * This function is immutable and similar to the built-in "Append Array" node.
     *
     * @param ArrayA The first input array.
     * @param ArrayB The second input array.
     * @param Result The resulting merged array.
     */
    UFUNCTION(BlueprintPure, CustomThunk, meta = (CustomStructureParam = "ArrayA,ArrayB,Result"), Category = "Functional|Arrays")
    static void Merge_Any(const FGenericStruct& ArrayA, const FGenericStruct& ArrayB, FGenericStruct& Result);

    DECLARE_FUNCTION(execMerge_Any);

    /**
     * Concatenates the elements of an array into a single FString, separated by the specified separator.
     * This function is immutable and does not modify the input array.
     *
     * @param Array The input array of FStrings.
     * @param Separator The string to insert between each element.
     */
    UFUNCTION(BlueprintPure, Category = "Functional|Arrays")
    static FString MkString(const TArray<FString>& Array, const FString& Separator);

    /** 
     * Concatenates the elements of an int32 array into a single FString, separated by the specified separator.
     * 
     * @param Array The input array of integers.
     * @param Separator The string to insert between each element.
     */
    UFUNCTION(BlueprintPure, Category = "Functional|Arrays")
    static FString MkString_Int32(const TArray<int32>& Array, const FString& Separator);
};