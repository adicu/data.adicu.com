data.adicu.com
====================

To get started:

# app structure

|-- app.py (the executable for this app)
|-- app/ (request handlers; notably all inheriting from basic.py)
|-- conf/ (configs)
|-- lib/ (generic library code; will *not* do any request handling)
|-- scripts/ (command line helper scripts; database start/stop scripts)
|-- tests/ (py.test scripts that should be used during development)

Top level files should be: executables (the main app), or a README.md.
