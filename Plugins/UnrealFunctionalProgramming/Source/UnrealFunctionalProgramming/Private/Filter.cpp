#include "Filter.h"

// ==================== FILTER ========================================

template<typename T, typename DelegateType>
TArray<T> Filter_Internal(const TArray<T>& Array, DelegateType Predicate)
{
    if (!Predicate.IsBound())
    {
        // Handle the case where the delegate is not bound
        UE_LOG(LogTemp, Warning, TEXT("Filter: Delegate is not bound."));
        return TArray<T>();
    }
    TArray<T> Result;
    for (const T& Element : Array)
    {
        if (Predicate.Execute(Element))
        {
            Result.Add(Element);
        }
    }
    return Result;
}

template<typename T, typename DelegateType>
TArray<T> Filter_Internal_With_Index(const TArray<T>& Array, DelegateType Predicate)
{
    if (!Predicate.IsBound())
    {
        // Handle the case where the delegate is not bound
        UE_LOG(LogTemp, Warning, TEXT("Filter: Delegate is not bound."));
        return TArray<T>();
    }
    TArray<T> Result;
    
    for (int32 Index = 0; Index < Array.Num(); ++Index)
    {
        if (Predicate.Execute(Index))
        {
            Result.Add(Array[Index]);
        }
    }

    return Result;
}


// type-specific functions

TArray<int32> UFilter::Filter_Int32(const TArray<int32>& Array, FFilterInt32Delegate Predicate)
{
    return Filter_Internal<int32, FFilterInt32Delegate>(Array, Predicate);
}


TArray<FString> UFilter::Filter_By_Index_FString(const TArray<FString>& Array, FFilterInt32Delegate Predicate)
{
    return Filter_Internal_With_Index<FString, FFilterInt32Delegate>(Array, Predicate);
}