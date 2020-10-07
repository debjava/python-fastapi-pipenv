@Echo Off
REM setup environment variable in Python
echo ********* Creating and Setting up virtual environment *********

echo        ********* Upgrading PIP *********

call py -m pip install --upgrade pip

echo        ********* PIP upgraded successfully *********

set PIPENV_VENV_IN_PROJECT="enabled"

echo        ********* Installing pipenv *********

call pip install pipenv

echo        ********* Creating virtual environment *********

call pipenv install

echo        ********* Activating virtual environment *********
call pipenv shell

echo ********* Virtual Environment created successfully *********


echo ********* All set and ready for development *********

