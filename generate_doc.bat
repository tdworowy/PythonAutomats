sphinx-apidoc -o docs PythonAutomats
cd docs
xcopy *.rst source /i /r /q
make clean && make html