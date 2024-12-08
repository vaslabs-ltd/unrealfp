#include "Foreach.h"

#include "Components/Button.h"

template<typename T, typename DelegateType>
void Foreach_Internal(const TArray<T>& Array, DelegateType Function)
{
    for (const T& Element : Array)
    {
        Function.ExecuteIfBound(Element);
    }
}

template<typename T, typename DelegateType>
void ForeachRange_Internal(const TArray<T>& Array, int32 Start, int32 End, DelegateType Function)
{
    if (!Function.IsBound())
    {
        UE_LOG(LogTemp, Warning, TEXT("ForeachRange_Internal: Delegate is not bound."));
        return;
    }
    if (Start < 0 || End < 0)
    {
        UE_LOG(LogTemp, Warning, TEXT("ForeachRange_Internal: Start and End must be non-negative."));
        return;
    }
    for (int32 Index = Start; Index < End; ++Index)
    {
        if (Index < Array.Num())
        {
            Function.Execute(Array[Index]);
        }
        else
        {
            UE_LOG(LogTemp, Warning, TEXT("ForeachRange_Internal: Index out of bounds."));
            break;
        }
    }
}

template<typename T, typename DelegateType>
void Foreach_Internal_Object(const TArray<T*>& Array, DelegateType Function)
{
    for (T* Element : Array)
    {
        if (IsValid(Element) && Function.IsBound())
        {
            Function.Execute(Element);
        }
        else if (!IsValid(Element))
        {
            UE_LOG(LogTemp, Warning, TEXT("Foreach_Internal_Object: Encountered an invalid pointer."));
        }
        else
        {
            UE_LOG(LogTemp, Warning, TEXT("Foreach_Internal_Object: Delegate is not bound."));
            break;
        }
    }
}

void UForeach::ForeachApply_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function)
{
    return Foreach_Internal<int32, FForeachInt32Delegate>(Array, Function);
}

void UForeach::ForeachApply_Int64(const TArray<int64>& Array, FForeachInt64Delegate Function)
{
    return Foreach_Internal<int64, FForeachInt64Delegate>(Array, Function);
}

void UForeach::ForeachApply_Bool(const TArray<bool>& Array, FForeachBoolDelegate Function)
{
    return Foreach_Internal<bool, FForeachBoolDelegate>(Array, Function);
}

void UForeach::ForeachApply_Float(const TArray<float>& Array, FForeachFloatDelegate Function)
{
    return Foreach_Internal<float, FForeachFloatDelegate>(Array, Function);
}

// Type-specific function for UButton
void UForeach::ForeachApply_Button(const TArray<UButton*>& Array, FForeachButtonDelegate Function)
{
    Foreach_Internal_Object<UButton, FForeachButtonDelegate>(Array, Function);
}

void UForeach::Foreach_String(const TArray<FString>& Array, FForeachStringDelegate Function)
{
    Foreach_Internal<FString, FForeachStringDelegate>(Array, Function);
}

void UForeach::Foreach_Object(const TArray<UObject*>& Array, FForeachObjectDelegate Function)
{
    Foreach_Internal_Object<UObject, FForeachObjectDelegate>(Array, Function);
}

void UForeach::Foreach_Actor(const TArray<AActor*>& Array, FForeachActorDelegate Function)
{
    Foreach_Internal_Object<AActor, FForeachActorDelegate>(Array, Function);
}

void UForeach::Foreach_Component(const TArray<UActorComponent*>& Array, FForeachComponentDelegate Function)
{
    Foreach_Internal_Object<UActorComponent, FForeachComponentDelegate>(Array, Function);
}

template<typename T, typename DelegateType>
void Foreach_Internal_Object_With_Index(const TArray<T*>& Array, DelegateType Function)
{
    if (!Function.IsBound())
    {
        UE_LOG(LogTemp, Warning, TEXT("Foreach_Internal_Object_With_Index: Delegate is not bound."));
        return;
    }
    for (int32 Index = 0; Index < Array.Num(); ++Index)
    {
        T* Element = Array[Index];
        if (IsValid(Element))
        {
            Function.Execute(Element, Index);
        }
        else
        {
            UE_LOG(LogTemp, Warning, TEXT("Foreach_Internal_Object_With_Index: Encountered an invalid pointer."));
            break;
        }
    }
}

void UForeach::Foreach_Button_With_Index(const TArray<UButton*>& Array, FForeachButtonDelegateWithIndex Function)
{
    Foreach_Internal_Object_With_Index<UButton, FForeachButtonDelegateWithIndex>(Array, Function);
}