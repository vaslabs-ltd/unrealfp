// Copyright Vaslabs LTD 2025 All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "Components/Button.h" // Include for UButton

#include "Foreach.generated.h"

// ================== FOREACH ================================================
// Delegate for int32
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachInt32Delegate, int32, Element);

// Delegate for int64
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachInt64Delegate, int64, Element);

// Delegate for bool
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachBoolDelegate, bool, Element);

// Delegate for float
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachFloatDelegate, float, Element);

UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachStringDelegate, FString, Element);


// Delegate for UButton
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachButtonDelegate, UButton*, Button);

UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachObjectDelegate, UObject*, Element);

UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachActorDelegate, AActor*, Element);

UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_OneParam(FForeachComponentDelegate, UActorComponent*, Element);

UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_TwoParams(FForeachButtonDelegateWithIndex, UButton*, Element, int32, Index);


UCLASS()
class UNREALFUNCTIONALPROGRAMMING_API UForeach : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    /** ForeachApply for int32 arrays */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static void ForeachApply_Int32(const TArray<int32>& Array, FForeachInt32Delegate Function);

    /** ForeachApply for int64 arrays */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static void ForeachApply_Int64(const TArray<int64>& Array, FForeachInt64Delegate Function);

    /** ForeachApply for bool arrays */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static void ForeachApply_Bool(const TArray<bool>& Array, FForeachBoolDelegate Function);

    /** ForeachApply for float arrays */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static void ForeachApply_Float(const TArray<float>& Array, FForeachFloatDelegate Function);

    /** ForeachApply function for UButton arrays */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static void ForeachApply_Button(const TArray<UButton*>& Array, FForeachButtonDelegate Function);

    UFUNCTION(BlueprintCallable, Category = "Functional")
    static void Foreach_String(const TArray<FString>& Array, FForeachStringDelegate Function);

    UFUNCTION(BlueprintCallable, Category = "Functional")
    static void Foreach_Object(const TArray<UObject*>& Array, FForeachObjectDelegate Function);

    UFUNCTION(BlueprintCallable, Category = "Functional")
    static void Foreach_Actor(const TArray<AActor*>& Array, FForeachActorDelegate Function);

    UFUNCTION(BlueprintCallable, Category = "Functional")
    static void Foreach_Component(const TArray<UActorComponent*>& Array, FForeachComponentDelegate Function);

    UFUNCTION(BlueprintCallable, Category = "Functional")
    static void Foreach_Button_With_Index(const TArray<UButton*>& Array, FForeachButtonDelegateWithIndex Function);
    // add more functions for other types as needed
};