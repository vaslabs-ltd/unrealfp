#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"

#include "Functions.generated.h"

// ================== Identity ================================================
// Delegate for int32
UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(int32, FInt32Int32Delegate, int32, Input);

// Delegate for boolean
UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(int32, FInt32BoolDelegate, bool, Input);

// Delegate for int32 -> Array<int32>
UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(TArray<int32>, FInt32ArrayInt32Delegate, int32, Input);

// Delegate for mapping (int32, int32) -> int32
UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_TwoParams(int32, FInt32Int32ToInt32Delegate, int32, Input1, int32, Input2);

UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(FLinearColor, FMapVectorParameterValueToLinearColorDelegate, FVectorParameterValue, Element);


UCLASS()
class UNREALFUNCTIONALPROGRAMMING_API UFunctions : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    // ================ int32 ========================================
    UFUNCTION(BlueprintPure, Category = "Functional")
    static int32 ApplyInt32ToInt32Function(int32 Input, FInt32Int32Delegate Function);

    UFUNCTION(BlueprintPure, Category = "Functional")
    static bool ApplyInt32ToBoolFunction(int32 Input, FInt32BoolDelegate Function);

    /** conversion function to map FVectorParameterValue to FLinearColor */
    UFUNCTION()
    static FLinearColor ConvertVectorParameterValueToLinearColor(FVectorParameterValue Element);

    /** Blueprint-callable function to return the pre-bound delegate  that extracts a linear color delegate from a vector parameter value */
    UFUNCTION(BlueprintPure, Category = "Functional|Delegates")
    static FMapVectorParameterValueToLinearColorDelegate GetVectorParamValueToLinearColorDelegate();
};