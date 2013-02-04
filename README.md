skeleton application
====================

This is an example tornado application structure

# application structure

app_name
|-- app_name.py (the executable for this app)
|-- settings.py (the only spot with external references used by the application, preferences, configuration variables)
|-- app/ (request handlers; notably all inheriting from basic.py)
|-- conf/ (configs)
|-- lib/ (generic library code; may or may not be application dependent, and will *not* do any request handling)
|-- scripts/ (command line helper scripts; database start/stop scripts; migration scripts)
|-- static/ (static web assets)
|-- templates/ (templates rendered)
|-- tests/ (py.test or test.sh scripts that should be used during development)

Top level files should be: executables (the main app or queue readers), settings.py, or a README.md.
