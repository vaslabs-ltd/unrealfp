# Forall


### ForAll_Int32


<div markdown="1">
<details markdown="1">
<summary>Inputs</summary>

- **Array** : Array int
- **Predicate** : object
    - FForAllInt32Delegate: `int32 => bool`

</details>


</div>


<div markdown="1">
<details markdown="1">
<summary>Outputs</summary>

- `bool`

</details>


</div>

<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction&quot; 
 NodeGuid=577615974689448BA68C9D1BD62BFF47
 FunctionReference=(MemberParent=&quot;/Script/CoreUObject.Class&#x27;/Script/UnrealFunctionalProgramming.Forall&#x27;&quot;,MemberName=&quot;ForAll_Int32&quot;)
 CustomProperties Pin (PinId=BF1B82810E624ED8BAA2555AE7BBFC1B,PinName=&quot;execute&quot;,PinToolTip=&quot;\nExec&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
 CustomProperties Pin (PinId=73A1E04A9CF34C35B815ED141DCE9ABC,PinName=&quot;then&quot;,PinToolTip=&quot;\nExec&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
 CustomProperties Pin (PinId=93580DE8F8674FD5B2EF2B194BC19604,PinName=&quot;Array&quot;,PinToolTip=&quot;&quot;,, PinType.PinCategory=&quot;int&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=Array, PinType.bIsReference=True, PinType.bIsConst=True, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
CustomProperties Pin (PinId=E638F590D3E24228BB27532D5E3668D5,PinName=&quot;Predicate&quot;,PinToolTip=&quot;&quot;,, PinType.PinCategory=&quot;delegate&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/CoreUObject.Package&#x27;/Script/UnrealFunctionalProgramming&#x27;&quot;, MemberName=&quot;FForAllInt32Delegate__DelegateSignature&quot;),PinType.PinValueType=(), PinType.ContainerType=None, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 CustomProperties Pin (PinId=AE6AA76C645140199A68CAB853AF56D8,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;&quot;,,Direction=&quot;EGPD_Output&quot;, PinType.PinCategory=&quot;bool&quot;, PinType.PinSubCategory=&quot;&quot;, PinType.PinSubCategoryObject=None, PinType.PinSubCategoryMemberReference=(), PinType.PinValueType=(), PinType.ContainerType=, PinType.bIsReference=False, PinType.bIsConst=False, PinType.bIsWeakPointer=False, PinType.bIsUObjectWrapper=False, PinType.bSerializeAsSinglePrecisionFloat=False, )
 End Object
 
    </canvas>
</div>
    