sphinx-apidoc -o docs PythonAutomats
cd docs
xcopy *.rst source /i /r /y
make clean && make html