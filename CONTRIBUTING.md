# How to contribute

## Setup a development environment

1) First of all make sure to have a 3.x python version installed
2) Clone the source code:
    `git@github.com:MarketSquare/robotframework-archivelibrary.git`
3) I suggest to create a python virtual environment:
```sh
    cd robotframework-requests/
    python -m venv venv
    source venv/bin/activate
```
4) Install the library in editing mode and all the test dependencies:
    `python -m pip install -e`
5) Run acceptance tests with robot:
    `robot ./atests`
6) Run unit tests wiht pytest:
    `pytest ./utests`

If everything went well now you're ready to go!

## Coding guidelines

Many checks and tests are automatically performed in Continuous Integration with the
GitHub Actions.

Have a look at the file `.github/workflows/python-app.yml` to see the commands used. 

#### Linting

The project uses flake8 for linting the source code.

#### Unit tests

PyTest is integrated for unit tests that located in `utests/` folder.

#### Acceptance tests

Obviously for acceptance tests Robot Framework is used, files are located in `atests/`.
   
#### Test Coverage

Test coverage is evaluated for unit and acceptance tests, after test execution 
`coverage report` command shows you the statistics. 

#### Documentation

Keywords documentation (on Linux) can be updated running the following script:

`doc/generate_doc.sh`
