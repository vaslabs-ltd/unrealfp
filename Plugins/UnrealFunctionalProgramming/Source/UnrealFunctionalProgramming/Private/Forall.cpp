#include "Forall.h"

// ========================= FORALL ========================================
template<typename T, typename DelegateType>
bool ForAll_Internal(const TArray<T>& Array, DelegateType Predicate)
{
    if (!Predicate.IsBound())
    {
        // Handle the case where the delegate is not bound
        UE_LOG(LogTemp, Warning, TEXT("ForAll: Delegate is not bound."));
        // if array is empty then forall would be true regardless of predicate bind, this
        // can be debateable though
        return Array.Num() == 0;
    }
    
    for (const T& Element : Array)
    {
        if (!Predicate.Execute(Element))
        {
            return false;
        }
    }
    return true;
}

bool UForall::ForAll_Int32(const TArray<int32>& Array, FForAllInt32Delegate Predicate)
{
    return ForAll_Internal(Array, Predicate);
}