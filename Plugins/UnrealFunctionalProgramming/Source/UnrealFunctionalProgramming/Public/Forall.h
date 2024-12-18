#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"

#include "Forall.generated.h"

// ==================== FORALL =============================================

UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FForAllInt32Delegate, int32, Element);

UCLASS()
class UNREALFUNCTIONALPROGRAMMING_API UForall : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    // ================ FORALL ========================================
    UFUNCTION(BlueprintPure, Category = "Functional")
    static bool ForAll_Int32(const TArray<int32>& Array, FForAllInt32Delegate Predicate);
};