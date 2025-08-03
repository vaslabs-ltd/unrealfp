COPYRIGHT_TEXT='// Copyright Vaslabs LTD 2025 All Rights Reserved.'

file_lookup_dirs="Plugins/UnrealFunctionalProgramming/Source/UnrealFunctionalProgramming/Private \
Plugins/UnrealFunctionalProgramming/Source/UnrealFunctionalProgramming/Public \
Plugins/UnrealFunctionalProgramming/Source/UnrealFunctionalProgramming"

extensions="cpp h cs"

for dir in $file_lookup_dirs; do
    for ext in $extensions; do
        for file in $(ls $dir/*.$ext); do
            # if file does not exist, skip
            if [ ! -f "$file" ]; then
                echo "File $file does not exist, skipping."
                continue
            fi
            #if copyright text is already present, skip
            if grep -q "$COPYRIGHT_TEXT" "$file"; then
                echo "Copyright text already present in $file, skipping."
                continue
            fi
            echo "Adding copyright text to $file"
            sed -i "1s|^|$COPYRIGHT_TEXT\n\n|" "$file"
        done
        
    done
done

