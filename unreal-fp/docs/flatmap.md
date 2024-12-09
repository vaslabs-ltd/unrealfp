# FlatMap


### FlatMap_StringToInt32


<div markdown="1">
<details markdown="1">
<summary>Inputs</summary>

- Array: **string Array**
- Function: **Delegate**
    - FFlatMapStringToInt32Delegate: `string => int Array`

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

FlatMap function from FString to int32 array

</details>


</div>

<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction&quot; 
 NodeGuid=ABC77B04107C44408857FA500EF6DB53
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.FlatMap&#x27;&quot;,MemberName=&quot;FlatMap_StringToInt32&quot;)
 CustomProperties Pin (PinId=BF1B82810E624ED8BAA2555AE7BBFC1B,PinName=&quot;execute&quot;,PinToolTip=&quot;\nExec&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
 CustomProperties Pin (PinId=73A1E04A9CF34C35B815ED141DCE9ABC,PinName=&quot;then&quot;,PinToolTip=&quot;\nExec&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
 CustomProperties Pin (PinId=A23BA6C9E12B4F4B999330BDF4ACF108,PinName=&quot;Array&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;string&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False
 )
CustomProperties Pin (PinId=DFA0BADCDDCD4541B2A8598E1BE1F641,PinName=&quot;Function&quot;,PinToolTip=&quot;&quot; , PinType.PinCategory=&quot;delegate&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/CoreUObject.Package&#x27;/Script/UnrealFunctionalProgramming&#x27;&quot;, MemberName=&quot;FFlatMapStringToInt32Delegate__DelegateSignature&quot;),PinType.PinValueType=(), PinType.ContainerType=None, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 CustomProperties Pin (PinId=D26054B0969C4D8C868975FAB408DB98,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot; ,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 End Object
 
    </canvas>
</div>
    