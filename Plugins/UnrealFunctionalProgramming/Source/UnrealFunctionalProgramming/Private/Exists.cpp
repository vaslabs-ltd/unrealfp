// Copyright Vaslabs LTD 2025 All Rights Reserved.

#include "Exists.h"

template<typename T, typename DelegateType>
bool Exists_Internal(const TArray<T>& Array, DelegateType Predicate)
{
    if (!Predicate.IsBound())
    {
        // Handle the case where the delegate is not bound
        UE_LOG(LogTemp, Warning, TEXT("Exists: Delegate is not bound."));
        return false;
    }
    for (const T& Element : Array)
    {
        if (Predicate.Execute(Element))
        {
            return true;
        }
    }
    return false;
}

bool UExists::Exists_Int32(const TArray<int32>& Array, FExistsInt32Delegate Predicate)
{
    return Exists_Internal(Array, Predicate);
}