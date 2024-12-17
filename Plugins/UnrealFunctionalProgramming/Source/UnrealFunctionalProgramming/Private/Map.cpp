#include "Map.h"

// Templated internal function with generic SourceType for primitive types

template<typename SourceType, typename TargetType, typename DelegateType>
TArray<TargetType> Map_Internal(const TArray<SourceType>& Array, DelegateType Function)
{
    if (!Function.IsBound())
    {
        // Handle the case where the delegate is not bound
        UE_LOG(LogTemp, Warning, TEXT("Map: Delegate is not bound."));
        return TArray<TargetType>();
    }
    TArray<TargetType> Result;
    for (const SourceType& Element : Array)
    {
        TargetType MappedValue = Function.Execute(Element);
        Result.Add(MappedValue);
    }
    return Result;
}

// Type-specific functions

TArray<int32> UMap::Map_Int32ToInt32(const TArray<int32>& Array, FMapInt32ToInt32Delegate Function)
{
    return Map_Internal<int32, int32, FMapInt32ToInt32Delegate>(Array, Function);
}

TArray<float> UMap::Map_Int32ToFloat(const TArray<int32>& Array, FMapInt32ToFloatDelegate Function)
{
    return Map_Internal<int32, float, FMapInt32ToFloatDelegate>(Array, Function);
}

TArray<bool> UMap::Map_Int32ToBool(const TArray<int32>& Array, FMapInt32ToBoolDelegate Function)
{
    return Map_Internal<int32, bool, FMapInt32ToBoolDelegate>(Array, Function);
}

TArray<FString> UMap::Map_Int32ToString(const TArray<int32>& Array, FMapInt32ToStringDelegate Function)
{
    return Map_Internal<int32, FString, FMapInt32ToStringDelegate>(Array, Function);
}

TArray<int32> UMap::Map_StringToInt32(const TArray<FString>& Array, FMapStringToInt32Delegate Function)
{
    return Map_Internal<FString, int32, FMapStringToInt32Delegate>(Array, Function);
}

// Templated internal function with generic SourceType for object types (returns pointers)

template<typename SourceType, typename TargetType, typename DelegateType>
TArray<TargetType*> Map_Internal_Object(const TArray<SourceType>& Array, DelegateType Function)
{
    if (!Function.IsBound())
    {
        // Handle the case where the delegate is not bound
        UE_LOG(LogTemp, Warning, TEXT("Map: Delegate is not bound."));
        return TArray<TargetType*>();
    }
    TArray<TargetType*> Result;
    for (const SourceType& Element : Array)
    {
        TargetType* MappedValue = Function.Execute(Element);
        if (MappedValue)
        {
            Result.Add(MappedValue);
        }

    }
    return Result;
}


TArray<UMaterialInstanceDynamic*> UMap::Map_FloatToMID(const TArray<float>& Array, FMapFloatToMIDDelegate Function)
{
    return Map_Internal_Object<float, UMaterialInstanceDynamic, FMapFloatToMIDDelegate>(Array, Function);
}


TArray<FText> UMap::Map_Int32ToText(const TArray<int32>& Array, FMapInt32ToTextDelegate Function)
{
    return Map_Internal<int32, FText, FMapInt32ToTextDelegate>(Array, Function);
}

TArray<FLinearColor> UMap::Map_VectorParameterValueToLinearColor(const TArray<FVectorParameterValue>& Array, FMapVectorParameterValueToLinearColorDelegate Function)
{
    return Map_Internal<FVectorParameterValue, FLinearColor, FMapVectorParameterValueToLinearColorDelegate>(Array, Function);
}