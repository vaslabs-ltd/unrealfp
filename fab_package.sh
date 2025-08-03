PLUGIN_NAME="UnrealFunctionalProgramming"
cd Plugins/$PLUGIN_NAME
directories_to_keep="Config/\
 Content/\
 Resources/\
 Source/\
 $PLUGIN_NAME.uplugin"

target_dir="../../target"

zip -r -9 -X -q -o "$PLUGIN_NAME.zip" $directories_to_keep

[ -d $target_dir ] && rm -r $target_dir

mkdir -p $target_dir/fab

mv "$PLUGIN_NAME.zip" $target_dir/fab/$PLUGIN_NAME.zip

cd -