# FlatMap


### FlatMap_StringToInt32


<div markdown="1">
<details markdown="1">
<summary>Inputs</summary>

- **Array** : Array string
- **Function** : object
    - FFlatMapStringToInt32Delegate: `FString => int Array`

</details>


</div>


<div markdown="1">
<details markdown="1">
<summary>Outputs</summary>

- `int Array`

</details>


</div>

<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction&quot; 
 NodeGuid=D88A2A84E7DC40F2889540B52B1202A6
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.FlatMap&#x27;&quot;,MemberName=&quot;FlatMap_StringToInt32&quot;)
 CustomProperties Pin (PinId=BF1B82810E624ED8BAA2555AE7BBFC1B,PinName=&quot;execute&quot;,PinToolTip=&quot;\nExec&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
 CustomProperties Pin (PinId=73A1E04A9CF34C35B815ED141DCE9ABC,PinName=&quot;then&quot;,PinToolTip=&quot;\nExec&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
 CustomProperties Pin (PinId=DC49045A5ADB47A7A29A3E6FF94C4225,PinName=&quot;Array&quot;,PinToolTip=&quot;&quot;,, PinType.PinCategory=&quot;string&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
CustomProperties Pin (PinId=EC0719A725084EF68C63CF962FE1F8A1,PinName=&quot;Function&quot;,PinToolTip=&quot;&quot;,, PinType.PinCategory=&quot;delegate&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/CoreUObject.Package&#x27;/Script/UnrealFunctionalProgramming&#x27;&quot;, MemberName=&quot;FFlatMapStringToInt32Delegate__DelegateSignature&quot;),PinType.PinValueType=(), PinType.ContainerType=None, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 CustomProperties Pin (PinId=3A4C17F6A0A244C3B15986D5F5FF60A8,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot;,,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 End Object
 
    </canvas>
</div>
    