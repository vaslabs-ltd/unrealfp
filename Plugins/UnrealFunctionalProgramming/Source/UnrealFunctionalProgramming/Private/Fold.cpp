// Copyright Vaslabs LTD 2025 All Rights Reserved.


#include "Fold.h"

// ========== FOLD ===============================
template<typename T, typename DelegateType>
T Fold_Internal(const TArray<T>& Array, T InitialValue, DelegateType Function)
{
    if (!Function.IsBound())
    {
        UE_LOG(LogTemp, Warning, TEXT("Fold: Delegate is not bound."));
    }
    T Accumulator = InitialValue;
    for (const T& Element : Array)
    {
        Accumulator = Function.Execute(Accumulator, Element);
    }
    return Accumulator;
}

int32 UFold::Fold_Int32(const TArray<int32>& Array, int32 InitialValue, FFoldInt32Delegate Function)
{
    return Fold_Internal<int32, FFoldInt32Delegate>(Array, InitialValue, Function);
}

float UFold::Fold_Float(const TArray<float>& Array, float InitialValue, FFoldFloatDelegate Function)
{
    return Fold_Internal<float, FFoldFloatDelegate>(Array, InitialValue, Function);
}