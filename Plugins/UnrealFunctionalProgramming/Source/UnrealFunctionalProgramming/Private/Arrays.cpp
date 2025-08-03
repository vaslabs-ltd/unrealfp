// Copyright Vaslabs LTD 2025 All Rights Reserved.

#include "Arrays.h"


TArray<int32> UArrays::Generate_ArrayInt32(int32 Start, int32 End, FInt32Int32Delegate Function)
{
    TArray<int32> Result;
    if (!Function.IsBound())
    {
        UE_LOG(LogTemp, Warning, TEXT("Generate: Delegate is not bound."));
        return Result;
    }
    for (int32 Index = Start; Index < End; Index++)
    {
        Result.Add(Function.Execute(Index));
    }
    return Result;
}

TArray<int32> UArrays::Generate_ArrayInt32FromInt32(int32 Feed, int32 Start, int32 End, FInt32Int32ToInt32Delegate Function)
{
    TArray<int32> Result;
    if (!Function.IsBound())
    {
        UE_LOG(LogTemp, Warning, TEXT("Generate_Array: Delegate is not bound."));
        return Result;
    }
    for (int32 Index = Start; Index < End; Index++)
    {
        Result.Add(Function.Execute(Feed, Index));
    }
    return Result;
}

/**
 * Merge_Any is a placeholder function and is never called directly.
 * The actual implementation is handled in execMerge_Any.
 */
void UArrays::Merge_Any(const FGenericStruct& ArrayA, const FGenericStruct& ArrayB, FGenericStruct& Result)
{
    // Placeholder: This function is intentionally left empty.
}

/**
 * execMerge_Any handles the merging of two wildcard arrays into a new array.
 *
 * @param Stack The script stack containing function parameters.
 */
DEFINE_FUNCTION(UArrays::execMerge_Any)
{
    // Retrieve ArrayA
    Stack.MostRecentProperty = nullptr;
    Stack.StepCompiledIn<FArrayProperty>(nullptr);
    FArrayProperty* ArrayAProperty = CastField<FArrayProperty>(Stack.MostRecentProperty);
    void* ArrayAAddr = Stack.MostRecentPropertyAddress;

    // Retrieve ArrayB
    Stack.MostRecentProperty = nullptr;
    Stack.StepCompiledIn<FArrayProperty>(nullptr);
    FArrayProperty* ArrayBProperty = CastField<FArrayProperty>(Stack.MostRecentProperty);
    void* ArrayBAddr = Stack.MostRecentPropertyAddress;

    // Retrieve Result
    Stack.MostRecentProperty = nullptr;
    Stack.StepCompiledIn<FArrayProperty>(nullptr);
    FArrayProperty* ResultProperty = CastField<FArrayProperty>(Stack.MostRecentProperty);
    void* ResultAddr = Stack.MostRecentPropertyAddress;

    P_FINISH;

    // Now you have ArrayAProperty, ArrayBProperty, and ResultProperty, as well as their addresses
    // You can proceed with type checks, resizing the result array, and copying elements as needed.

    if (!ArrayAProperty || !ArrayBProperty || !ResultProperty)
    {
        Stack.Logf(ELogVerbosity::Error, TEXT("Merge_Any: Invalid properties!"));
        return;
    }

    // Check inner properties and ensure types match
    if (!ArrayAProperty->Inner || !ArrayBProperty->Inner || !ResultProperty->Inner)
    {
        Stack.Logf(ELogVerbosity::Error, TEXT("Merge_Any: Invalid inner properties!"));
        return;
    }

    if (!ArrayAProperty->Inner->SameType(ArrayBProperty->Inner))
    {
        Stack.Logf(ELogVerbosity::Error, TEXT("Merge_Any: ArrayA and ArrayB must have the same element type!"));
        return;
    }

    if (!ArrayAProperty->Inner->SameType(ResultProperty->Inner))
    {
        Stack.Logf(ELogVerbosity::Error, TEXT("Merge_Any: Result array type must match input array types!"));
        return;
    }

    // Use FScriptArrayHelper to manipulate arrays
    FScriptArrayHelper ArrayAHelper(ArrayAProperty, ArrayAAddr);
    FScriptArrayHelper ArrayBHelper(ArrayBProperty, ArrayBAddr);
    FScriptArrayHelper ResultHelper(ResultProperty, ResultAddr);

    int32 ACount = ArrayAHelper.Num();
    int32 BCount = ArrayBHelper.Num();

    ResultHelper.Resize(ACount + BCount);

    for (int32 i = 0; i < ACount; i++)
    {
        const uint8* SourceElem = ArrayAHelper.GetRawPtr(i);
        uint8* DestElem = ResultHelper.GetRawPtr(i);
        ResultProperty->Inner->CopyCompleteValue(DestElem, SourceElem);
    }

    for (int32 i = 0; i < BCount; i++)
    {
        const uint8* SourceElem = ArrayBHelper.GetRawPtr(i);
        uint8* DestElem = ResultHelper.GetRawPtr(ACount + i);
        ResultProperty->Inner->CopyCompleteValue(DestElem, SourceElem);
    }

    // The merged result is now stored in ResultAddr via ResultHelper
}

FString UArrays::MkString(const TArray<FString>& Array, const FString& Separator)
{
    return FString::Join(Array, *Separator);
}

FString UArrays::MkString_Int32(const TArray<int32>& Array, const FString& Separator)
{
    TArray<FString> StringArray;
    for (int32 Element : Array)
    {
        StringArray.Add(FString::FromInt(Element));
    }
    return FString::Join(StringArray, *Separator);
}