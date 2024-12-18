# Arrays


### Generate_ArrayInt32


<div markdown="1">
<details markdown="1">
<summary>Inputs</summary>

- Start: **int**
- End: **int**
- Function: **Delegate**
    - FInt32Int32Delegate: `int => int`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Outputs</summary>

- `int Array`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Description</summary>

Generates an array of integers by applying a function to the index of the given range
and returns the resulting array.

#### Parameters

- Start: The starting index of the range.

- End: The ending index of the range exclusive.

</details>


</div>

<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction&quot; 
 NodeGuid=DE803C98B719453381FDB0846F4ABB26
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.Arrays&#x27;&quot;,MemberName=&quot;Generate_ArrayInt32&quot;)
 
 CustomProperties Pin (PinId=555FFCF7A56242E4B1E701DB8EDCD52A,PinName=&quot;Start&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=219AA10E42374471BEDC3625155885E7,PinName=&quot;End&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=A4A149DE4C5D4030931D5C53E056ECAE,PinName=&quot;Function&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;delegate&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/CoreUObject.Package&#x27;/Script/UnrealFunctionalProgramming&#x27;&quot;, MemberName=&quot;FInt32Int32Delegate__DelegateSignature&quot;),PinType.PinValueType=(), PinType.ContainerType=None, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 CustomProperties Pin (PinId=67EF5C3EBAA24630A2704DC92893F948,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot; ,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 End Object
 
    </canvas>
</div>
    
### Generate_ArrayInt32FromInt32


<div markdown="1">
<details markdown="1">
<summary>Inputs</summary>

- Feed: **int**
- Start: **int**
- End: **int**
- Function: **Delegate**
    - FInt32Int32ToInt32Delegate: `int, int => int`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Outputs</summary>

- `int Array`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Description</summary>

Generates an array of integers by applying a function to an input integer and the index of the given range
and returns the resulting array.

#### Parameters

- Feed: The input integer to be used in the function.

- Start: The starting index of the range.

- End: The ending index of the range exclusive.

</details>


</div>

<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction&quot; 
 NodeGuid=C52B555273AC47DAA891B66314459149
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.Arrays&#x27;&quot;,MemberName=&quot;Generate_ArrayInt32FromInt32&quot;)
 
 CustomProperties Pin (PinId=26288291B5E147E19B0717931DD9B6D0,PinName=&quot;Feed&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=B48F7122E79C41279C3080DDB62411B4,PinName=&quot;Start&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=5FFF172B888140CDA64FF145B9001A6A,PinName=&quot;End&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=FAF57B8F8FB44119999640B9C6D59A65,PinName=&quot;Function&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;delegate&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/CoreUObject.Package&#x27;/Script/UnrealFunctionalProgramming&#x27;&quot;, MemberName=&quot;FInt32Int32ToInt32Delegate__DelegateSignature&quot;),PinType.PinValueType=(), PinType.ContainerType=None, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 CustomProperties Pin (PinId=F4165847C63A401595C1503D5ECB43F9,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot; ,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 End Object
 
    </canvas>
</div>
    
### Merge_Any


<div markdown="1">
<details markdown="1">
<summary>Inputs</summary>

- ArrayA: **object**
- ArrayB: **object**
- Result: **object**

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Outputs</summary>

- `()`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Description</summary>

Merges two arrays of the same type into a new array without modifying the originals.
This function is immutable and similar to the built-in "Append Array" node.

#### Parameters

- ArrayA: The first input array.

- ArrayB: The second input array.

- Result: The resulting merged array.

</details>


</div>

<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction&quot; 
 NodeGuid=F9B9AE7447274742BBDF0575FD1AE3CB
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.Arrays&#x27;&quot;,MemberName=&quot;Merge_Any&quot;)
 
 CustomProperties Pin (PinId=872918DF83484305A64D2762B2D911EB,PinName=&quot;ArrayA&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;object&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=E7715C3FC5F44101B0A3DCA1527DE051,PinName=&quot;ArrayB&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;object&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=674044E9F4C944A7B3DB758CAF9EE8C0,PinName=&quot;Result&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;object&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
 
 End Object
 
    </canvas>
</div>
    
### MkString


<div markdown="1">
<details markdown="1">
<summary>Inputs</summary>

- Array: **string Array**
- Separator: **string**

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Outputs</summary>

- `string`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Description</summary>

Concatenates the elements of an array into a single FString, separated by the specified separator.
This function is immutable and does not modify the input array.

#### Parameters

- Array: The input array of FStrings.

- Separator: The string to insert between each element.

</details>


</div>

<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction&quot; 
 NodeGuid=ABF97BD736034EC2A7E79E65731595A7
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.Arrays&#x27;&quot;,MemberName=&quot;MkString&quot;)
 
 CustomProperties Pin (PinId=C09BF77295124684A312E61EFE5ED2AF,PinName=&quot;Array&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;string&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=07D0B95D2A8048F28ED97E70BBF20769,PinName=&quot;Separator&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;string&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
 CustomProperties Pin (PinId=CAC2DFAE5F604CFEBECC640D27212F16,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot; ,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;string&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 End Object
 
    </canvas>
</div>
    
### MkString_Int32


<div markdown="1">
<details markdown="1">
<summary>Inputs</summary>

- Array: **int Array**
- Separator: **string**

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Outputs</summary>

- `string`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Description</summary>

Concatenates the elements of an int32 array into a single FString, separated by the specified separator.

#### Parameters

- Array: The input array of integers.

- Separator: The string to insert between each element.

</details>


</div>

<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction&quot; 
 NodeGuid=E2F0AA65D6114101B2DCF03195B1CE0D
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.Arrays&#x27;&quot;,MemberName=&quot;MkString_Int32&quot;)
 
 CustomProperties Pin (PinId=597F98C214084699898869FB4ACDE9E3,PinName=&quot;Array&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=C29981B27E8A4D3B88AEAB83501408EB,PinName=&quot;Separator&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;string&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
 CustomProperties Pin (PinId=34A0D673E6044705A84EEE0EBB56DFFE,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot; ,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;string&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 End Object
 
    </canvas>
</div>
    