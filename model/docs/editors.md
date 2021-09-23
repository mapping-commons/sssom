# <span style="color:red">Still under development -- not yet ready for prime time</span>



# Template for LinkML based schemas

## Requirements
* __Python >= 3.7.1__
* __GNU make__ - A command line gnu make process (Windows users can use [cygwin](https://www.cygwin.com/) - make comes built in on a Mac)
* __pip__ - comes with most python distros - you should be ok
* __virtualenv__ - can be added via `pip install virtualenv`
* __pipenv__ - can be added via `pip install pipenv`
* 

## What is this?

This is a GitHub template for a [LinkML](https://github.com/linkml/) based projects.

It allows you to create a project for your schema as quickly as
possible. It takes care of generating a beautiful readthedocs themed
site, as well as downstream artefacts, including:

 * JSON-Schema
 * ShEx
 * OWL
 * RDF (direct mapping)
 * JSON-LD Contexts
 * SQL DDL (TODO)
 * Python classes to represent model elements
 * TSV/CSV reports (TODO)

## Quickstart

 1. Click the big green <span style="color:green">"Use this template"</span> button on this page
 2. Name your repo according to your schema, e.g. my-awsome-project-model, and clone it
 3. Edit `model/CONFIG.yaml` to set your specific parameters. The details on the parameters can be found in
the [LinkML Template Configuration Model](https://linkml.github.io/template-config-model/) directory. 
    (_Note that the Template Configuration Model was built using this very template._)
 4. Configure the repository:
    * `make -f MakeConfig reset`
    
    This will generate a number of files that can be used to make, test, and distribute your final model.  Note
    that the template-configurator only needs to be run once as a rule.  You can, however, re-generate allof
    the target artifacts with `make -f MakeConfig reset`.  You can also selectively remove artifacts and get them
    regenerated with `make -f MakeConfig update`
 5. Rename the schema file in [model/schema](model/schema) to match the `root_schema` named in the CONFIG.yaml file.  
    Note: `root_schema` does not have the `.yaml` suffix, the file does.  As an example, if you specified `root_schema: my-schema`,
    the schema would be named model/schema/my-schema.yaml
 6. Edit the root_schema to add your own types, classes and slots.
 7. Type `make` to build your downstream artefacts (jsonschema, owl, etc)
 8. Once satisfied, commit your new project to github, which will rerun the make process.
 9. The package can also be installed in `pypi` - this is an advanced topic, see [PYPI_SETUP]() for details
10. This file (ABOUT.md) and the `images` directory can be removed once you are satisfied


## How it works

This repo is a GitHub "template" repo. When you "Use this template" it will make a copy for your project.

Everything is orchestrated by a generic single [Makefile](Makefile). For this to work you should follow certain conventions:

 * Keep your schema in src/schema
 * Use the `.yaml` suffix for all schema files
 * Use the suggested directory layout here.

To run the Makefile you will need Python (>=3.7):
