#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"

#include "Exists.generated.h"



UDELEGATE(BlueprintPure)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FExistsInt32Delegate, int32, Element);

UCLASS()
class UNREALFUNCTIONALPROGRAMMING_API UExists : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:

    UFUNCTION(BlueprintPure, Category = "Functional")
    static bool Exists_Int32(const TArray<int32>& Array, FExistsInt32Delegate Predicate);
};