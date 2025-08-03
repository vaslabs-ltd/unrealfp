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
 NodeGuid=2E556D41AECC412FBC3BAC6E6EBBA11A
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.Fold&#x27;&quot;,MemberName=&quot;Fold_Int32&quot;)
 
 CustomProperties Pin (PinId=0B5D503D876443B0999F715446A03328,PinName=&quot;Array&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=CCBCC9CAA43445B8BB96BBEF100E1215,PinName=&quot;InitialValue&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=A66B10041CE84C5E9D69D21B0FC74838,PinName=&quot;Function&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;delegate&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/CoreUObject.Package&#x27;/Script/UnrealFunctionalProgramming&#x27;&quot;, MemberName=&quot;FFoldInt32Delegate__DelegateSignature&quot;),PinType.PinValueType=(), PinType.ContainerType=None, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 CustomProperties Pin (PinId=E740E91BC3384BD5BDDCEA3D0890B6B9,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot; ,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
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
 NodeGuid=B09931BD9E4F4FD280C716F124D5AD30
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.Fold&#x27;&quot;,MemberName=&quot;Fold_Float&quot;)
 
 CustomProperties Pin (PinId=9C683F2395184D30AAB70077B1FA7C7C,PinName=&quot;Array&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;float&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=87697891D1C24130AD8408A61DE9F158,PinName=&quot;InitialValue&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;float&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=61B72D64487D44BDB5774301B4F8DB33,PinName=&quot;Function&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;delegate&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/CoreUObject.Package&#x27;/Script/UnrealFunctionalProgramming&#x27;&quot;, MemberName=&quot;FFoldFloatDelegate__DelegateSignature&quot;),PinType.PinValueType=(), PinType.ContainerType=None, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 CustomProperties Pin (PinId=2D9721324D7046429E58914F36AC9D71,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot; ,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;float&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 End Object
 
    </canvas>
</div>
    