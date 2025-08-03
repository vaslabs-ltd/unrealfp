// Copyright Vaslabs LTD 2025 All Rights Reserved.

#include "FlatMap.h"

template<typename SourceType, typename TargetType, typename DelegateType>
TArray<TargetType> FlatMap_Internal(const TArray<SourceType>& Array, DelegateType Function)
{
    TArray<TargetType> Result;
    if (!Function.IsBound())
    {
        UE_LOG(LogTemp, Warning, TEXT("FlatMap_Internal: Delegate is not bound."));
        return Result;
    }

    for (const SourceType& Element : Array)
    {
        TArray<TargetType> MappedValues = Function.Execute(Element);
        Result.Append(MappedValues);
    }
    return Result;
}


TArray<int32> UFlatMap::FlatMap_StringToInt32(const TArray<FString>& Array, FFlatMapStringToInt32Delegate Function)
{
    return FlatMap_Internal<FString, int32, FFlatMapStringToInt32Delegate>(Array, Function);
}



