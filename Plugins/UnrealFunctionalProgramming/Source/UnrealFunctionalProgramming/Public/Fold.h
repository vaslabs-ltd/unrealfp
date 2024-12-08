#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"

#include "Fold.generated.h"

// ================== FOLD ================================================

UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_TwoParams(int32, FFoldInt32Delegate, int32, Accumulator, int32, Element);

UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_TwoParams(float, FFoldFloatDelegate, float, Accumulator, float, Element);

UCLASS()
class UNREALFUNCTIONALPROGRAMMING_API UFold : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:

    // ===================== FOLD ===========================================================
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static int32 Fold_Int32(const TArray<int32>& Array, int32 InitialValue, FFoldInt32Delegate Function);

    /** Fold function for float arrays */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static float Fold_Float(const TArray<float>& Array, float InitialValue, FFoldFloatDelegate Function);

    // add more
};