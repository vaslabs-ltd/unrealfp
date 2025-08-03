// Copyright Vaslabs LTD 2025 All Rights Reserved.

#include "Functions.h"

template<typename ReturnType, typename InputType, typename DelegateType>
ReturnType ApplyFunction_Internal(InputType Input, DelegateType Function)
{
    if (Function.IsBound())
    {
        return (ReturnType)(Function.Execute(Input));
    }
    else
    {
        UE_LOG(LogTemp, Warning, TEXT("ApplyFunction: Delegate is not bound."));
        return ReturnType(); // Default-constructed return value
    }
}

int32 UFunctions::ApplyInt32ToInt32Function(int32 Input, FInt32Int32Delegate Function)
{
    return ApplyFunction_Internal<int32, int32, FInt32Int32Delegate>(Input, Function);
}

bool UFunctions::ApplyInt32ToBoolFunction(int32 Input, FInt32BoolDelegate Function)
{
    return ApplyFunction_Internal<bool, int32, FInt32BoolDelegate>(Input, Function);
}

FLinearColor UFunctions::ConvertVectorParameterValueToLinearColor(FVectorParameterValue Element)
{
    return Element.ParameterValue;
}

FMapVectorParameterValueToLinearColorDelegate UFunctions::GetVectorParamValueToLinearColorDelegate()
{
    UFunctions* DefaultObject = GetMutableDefault<UFunctions>();
    FMapVectorParameterValueToLinearColorDelegate Delegate;
    Delegate.BindUFunction(DefaultObject, "ConvertVectorParameterValueToLinearColor");
    return Delegate;
}