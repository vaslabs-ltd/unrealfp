#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "FlatMap.generated.h"

UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(TArray<int32>, FFlatMapStringToInt32Delegate, FString, Element);


UCLASS()
class UNREALFUNCTIONALPROGRAMMING_API UFlatMap : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    /** FlatMap function from FString to int32 array */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static TArray<int32> FlatMap_StringToInt32(const TArray<FString>& Array, FFlatMapStringToInt32Delegate Function);
};
