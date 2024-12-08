
#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"

#include "Filter.generated.h"


UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FFilterInt32Delegate, int32, Element);


UCLASS()
class UNREALFUNCTIONALPROGRAMMING_API UFilter : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    //===================Filter=========================
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static TArray<int32> Filter_Int32(const TArray<int32>& Array, FFilterInt32Delegate Predicate);

    UFUNCTION(BlueprintCallable, Category = "Functional")
    static TArray<FString> Filter_By_Index_FString(const TArray<FString>& Array, FFilterInt32Delegate Predicate);
};
