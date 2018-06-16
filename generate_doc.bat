sphinx-apidoc -o docs PythonAutomats
cd docs
xcopy *.rst source /i /y
make clean && make html