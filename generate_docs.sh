cd generate_docs_utils
source venv/bin/activate

pip install -r requirements.txt


python3 mkdocs.py ../Plugins/UnrealFunctionalProgramming/Source/UnrealFunctionalProgramming/Public/ ../unreal-fp/

cd -

cd unreal-fp

mkdocs build
