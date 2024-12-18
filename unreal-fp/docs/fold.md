# Fold


### Fold_Int32


<div markdown="1">
<details markdown="1">
<summary>Inputs</summary>

- Array: **int Array**
- InitialValue: **int**
- Function: **Delegate**
    - FFoldInt32Delegate: `int, int => int`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Outputs</summary>

- `int`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Description</summary>



</details>


</div>

<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction&quot; 
 NodeGuid=70018D7D5CEE46CC872192537844834C
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.Fold&#x27;&quot;,MemberName=&quot;Fold_Int32&quot;)
 
 CustomProperties Pin (PinId=2BF7F60D03D64D548FB307513C9D5493,PinName=&quot;Array&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=396D493C53C54AABB8AEC1ED4B6680E9,PinName=&quot;InitialValue&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=0AAD95D54CA74BFEB791FBFE6962F198,PinName=&quot;Function&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;delegate&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/CoreUObject.Package&#x27;/Script/UnrealFunctionalProgramming&#x27;&quot;, MemberName=&quot;FFoldInt32Delegate__DelegateSignature&quot;),PinType.PinValueType=(), PinType.ContainerType=None, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 CustomProperties Pin (PinId=08F5496F86A744F098CD20440178D0FE,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot; ,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 End Object
 
    </canvas>
</div>
    
### Fold_Float


<div markdown="1">
<details markdown="1">
<summary>Inputs</summary>

- Array: **float Array**
- InitialValue: **float**
- Function: **Delegate**
    - FFoldFloatDelegate: `float, float => float`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Outputs</summary>

- `float`

</details>


</div>

<div markdown="1">
<details markdown="1">
<summary>Description</summary>

Fold function for float arrays

</details>


</div>

<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction&quot; 
 NodeGuid=7555E8774C934DB489BE63BEE3BE535A
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.Fold&#x27;&quot;,MemberName=&quot;Fold_Float&quot;)
 
 CustomProperties Pin (PinId=DE0FF1346AC941938D48C5A707292FF2,PinName=&quot;Array&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;float&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=A4FF993F53F84C36A030258FF10A4B07,PinName=&quot;InitialValue&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;float&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=D6E3630B748F4A45B552058E8A4669F9,PinName=&quot;Function&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;delegate&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/CoreUObject.Package&#x27;/Script/UnrealFunctionalProgramming&#x27;&quot;, MemberName=&quot;FFoldFloatDelegate__DelegateSignature&quot;),PinType.PinValueType=(), PinType.ContainerType=None, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 CustomProperties Pin (PinId=62CCCF3A2F4541F8B8CE35D3537FD42F,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot; ,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;float&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 End Object
 
    </canvas>
</div>
    