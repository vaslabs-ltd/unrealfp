// Copyright Vaslabs LTD 2025 All Rights Reserved.

using UnrealBuildTool;

public class UnrealFunctionalProgramming : ModuleRules
{
    public UnrealFunctionalProgramming(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = ModuleRules.PCHUsageMode.UseExplicitOrSharedPCHs;

        PublicIncludePaths.AddRange(
            new string[] {}
        );

        PrivateIncludePaths.AddRange(
            new string[] {}
        );

        PublicDependencyModuleNames.AddRange(
            new string[]
            {
                "Core",
				"CoreUObject",
				"Engine",
				"InputCore",
				"UMG", // For UMG UI elements like UButton
				"Slate",
				"SlateCore",
            }
        );

        PrivateDependencyModuleNames.AddRange(
            new string[]
            {
                "CoreUObject",
                "Engine",
                "Slate",
                "SlateCore",
            }
        );

        if (Target.bBuildEditor)
        {
            PrivateDependencyModuleNames.AddRange(
                new string[]
                {
                    "BlueprintGraph",
                    "KismetCompiler",
                    "Kismet",
                    "UnrealEd",
                    "GraphEditor",
                    "EditorStyle",
                }
            );
        }
    }
}
