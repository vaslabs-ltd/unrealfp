#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "Functions.h"

#include "Map.generated.h"

// Delegate for mapping int32 to int32
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(int32, FMapInt32ToInt32Delegate, int32, Element);

// Delegate for mapping int32 to float
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(float, FMapInt32ToFloatDelegate, int32, Element);

// Delegate for mapping int32 to bool
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(bool, FMapInt32ToBoolDelegate, int32, Element);

// Delegate for mapping int32 to FString
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(FString, FMapInt32ToStringDelegate, int32, Element);

// Delegate for mapping int32 to Text
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(FText, FMapInt32ToTextDelegate, int32, Element);

// Delegate for mapping String to int32
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(int32, FMapStringToInt32Delegate, FString, Element);

// Delegate for mapping float to UMaterialInstanceDynamic*
UDELEGATE(BlueprintCallable)
DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam(UMaterialInstanceDynamic*, FMapFloatToMIDDelegate, float, Element);

UCLASS()
class UNREALFUNCTIONALPROGRAMMING_API UMap : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    // ================ MAP ========================================
        /** Map function from int32 to int32 */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static TArray<int32> Map_Int32ToInt32(const TArray<int32>& Array, FMapInt32ToInt32Delegate Function);

    /** Map function from int32 to float */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static TArray<float> Map_Int32ToFloat(const TArray<int32>& Array, FMapInt32ToFloatDelegate Function);

    /** Map function from int32 to bool */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static TArray<bool> Map_Int32ToBool(const TArray<int32>& Array, FMapInt32ToBoolDelegate Function);

    /** Map function from int32 to FString */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static TArray<FString> Map_Int32ToString(const TArray<int32>& Array, FMapInt32ToStringDelegate Function);

    /** Map function from int32 to Text */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static TArray<FText> Map_Int32ToText(const TArray<int32>& Array, FMapInt32ToTextDelegate Function);

    /** Map function from float to UMaterialInstanceDynamic* */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static TArray<UMaterialInstanceDynamic*> Map_FloatToMID(const TArray<float>& Array, FMapFloatToMIDDelegate Function);

    /** function from FString to int32 */
    UFUNCTION(BlueprintCallable, Category = "Functional")
    static TArray<int32> Map_StringToInt32(const TArray<FString>& Array, FMapStringToInt32Delegate Function);
};