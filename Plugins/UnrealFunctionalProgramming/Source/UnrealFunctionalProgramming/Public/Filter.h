
#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"

#include "Filter.generated.h"


UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FFilterInt32Delegate, int32, Element);

UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FFilterFVectorDelegate, FVector, Element);

UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FFilterLinearColorDelegate, FLinearColor, Element);

UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FFilterVectorParameterValueDelegate, FVectorParameterValue, Element);

UCLASS()
class UNREALFUNCTIONALPROGRAMMING_API UFilter : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    //===================Filter=========================
    UFUNCTION(BlueprintPure, Category = "Functional")
    static TArray<int32> Filter_Int32(const TArray<int32>& Array, FFilterInt32Delegate Predicate);

    UFUNCTION(BlueprintPure, Category = "Functional")
    static TArray<FString> Filter_By_Index_FString(const TArray<FString>& Array, FFilterInt32Delegate Predicate);

    /** Filter array of vectors structure array */
    UFUNCTION(BlueprintPure, Category = "Functional")
    static TArray<FVector> Filter_FVector(const TArray<FVector>& Array, FFilterFVectorDelegate Predicate);

    /** Filter array of linear colors */
    UFUNCTION(BlueprintPure, Category = "Functional")
    static TArray<FLinearColor> Filter_LinearColor(const TArray<FLinearColor>& Array, FFilterLinearColorDelegate Predicate);

    /** Filter array of Material's Vector Parameter Values */
    UFUNCTION(BlueprintPure, Category = "Functional")
    static TArray<FVectorParameterValue> Filter_VectorParameterValue(const TArray<FVectorParameterValue>& Array, FFilterVectorParameterValueDelegate Predicate);
};
