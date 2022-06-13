# The SSSOM Toolkit

In the following we will give a brief introduction into the SSSOM toolkit. For more detailed documentation please refer to https://mapping-commons.github.io/sssom-py.

## Pre-requisites

- Complete the [basic SSSOM tutorial](tutorial.md)
- [Install SSSOM toolkit](https://mapping-commons.github.io/sssom-py/installation.html). Alternatively, you can install the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit) and follow the tutorial using its [docker image](https://oboacademy.github.io/obook/howto/odk-setup/).
- We are assuming a Unix shell for this tutorial, but most of the principles should apply to the Windows CMD as well. Windows users may prefer to install the ODK (see above).

## Overview

SSSOM toolkit (STK), previously known as `sssom-py`, is a set of utility methods for processing SSSOM files, packaged as a Command Line Client (CLI) and a [python package](https://pypi.org/project/sssom/). In the following, we will extract mappings from an ontology an process them with the CLI. The goal is to give a sense of the functionality of the toolkit. Additional and more up-to-date information on usage can be found [here](https://mapping-commons.github.io/sssom-py).

## Table of Contents

1. `parse`: [Extracting mappings from an external source](#parse)
2. `merge`: [Combining mappings from several sources](#merge)
3. `convert`: [Converting an SSSOM mapping table into different formats](#convert)

<a id="parse"></a>

## Extracting mappings from an external source

One key issue developers are faced with is to convert various different mapping formats into a common representation (e.g. SSSOM). The SSSOM toolkit (STK) already implements a number of commonly use mapping formats:

1. [OWL Ontologies](https://en.wikipedia.org/wiki/Web_Ontology_Language)
2. [Alignment API](https://moex.gitlabpages.inria.fr/alignapi/) Format (format used by the Ontology Alignment Evaluation Initiative, OAEI)
3. Parsers for SNOMED mapping format and FHIR Concept Map are [in the making](https://github.com/mapping-commons/sssom-py/pull/207), June 2022.

Here we use Uberon, an anatomy ontology in the biomedical domain.

```
wget http://purl.obolibrary.org/obo/uberon/uberon-base.json -O uberon-base.json
```

Feel free to download the file manually if you do not have `wget` installed.

Now use `sssom parse` to extract all the mappings provided by the ontology. As there are multiple json based formats that can be parsed, you have to tell `sssom` which format you are using: `--input-format obographs-json`.

```
sssom parse uberon-base.json --input-format obographs-json --output uberon.sssom.tsv
```

From a CLI design perspective we already notice a few things:

1. `uberon-base.json` is passed to the STK _as an argument_ (without an option like `-i`). This is the case for most _primary inputs_ (mapping tables, source files) througout the SSSOM client.


<a id="merge"></a>

## Combining mappings from several sources

<a id="convert"></a>

## Converting an SSSOM mapping table into different formats



## Other methods:

- cliquesummary
- correlations
- crosstab
- dedupe
- diff
- dosql
- partition
- ptable
- reconcile-prefixes
- rewire
- sort
- sparql
- split
- validate

_Under construction_.