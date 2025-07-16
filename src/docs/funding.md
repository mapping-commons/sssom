## Funding

The Simple Standard for Sharing Ontological Mappings (SSSOM) is a community-driven project which has received support from many different sources.
We list the most important ones in the following.

### Volunteering efforts

A huge fraction of the work on SSSOM has been done by volunteers without dedicated grant support.
We hereby acknowledge their contributions as being absolutely essential. A selection of amazing contributions (by no means exhaustive):

- The development of [SSSOM Java](https://incenp.org/dvlpt/sssom-java/)
- Hundreds of careful contributions to discussions on the [SSSOM issue tracker](https://github.com/mapping-commons/sssom/issues)
- The first draft of the [Mapping Registry Cookiecutter](https://github.com/mapping-commons/mapping-commons-cookiecutter)
- We try to keep track of other [Community efforts here](https://github.com/mapping-commons/sssom/discussions/318)

### Phenomics First (NIH / NHGRI #1RM1HG010860-01)

A lot of the groundwork of SSSOM was done to support a disease mapping project as part of the [Mondo Disease Ontology](https://github.com/monarch-initiative/mondo),
which included, but was not limited to:

- Creation of a basic metadata model
- Implementation of validation and parsing methods in [sssom-py](https://github.com/mapping-commons/sssom-py)
- Generating [training materials](training.md)
- Organising [workshops](workshops.md)
- Outreach activities to clinical communities such as [OHDSI](https://www.ohdsi.org/)

The grant was awarded to members of the Monarch Initiative.

### Monarch (NIH / OD #5R24OD011883)

To support development of cross-species mappings and knowledge graph integration for the [Monarch Knowledge Graph](https://monarchinitiative.org/),
a few new features had to be supported:

- Groundwork for the [Semantic Mapping Vocabulary](https://github.com/mapping-commons/semantic-mapping-vocabulary) which contains, for example, cross-species mapping properties.
- The advancement of the concepts and tools behind the "Mapping Commons", including supporting the development of the [Mapping Registry Cookiecutter](https://github.com/mapping-commons/mapping-commons-cookiecutter)
- Various improvements to the SSSOM metadata model, including the introduction of curation rules.
- The [OxO2 SSSOM mapping browser](https://github.com/EBISPOT/oxo2)

The grant was awarded to members of the Monarch Initiative.

### Bosch Gift to LBNL

A lot of the work on tooling was supported by a Bosch Gift to the Lawrence Berkely National Laboratory (Chris Mungall group). We thank Bosch for their generous support which helped us with the following:

- Implementation of conversion and testing methods in [sssom-py](https://github.com/mapping-commons/sssom-py)
- The development of training materials
- The development of specialised matching tools such as [OAK lexmatch](https://incatools.github.io/ontology-access-kit/guide/mappings.html) which provided the first implementation of the SSSOM standard in a matching tool.

### DARPA: Young Faculty Award W911NF2010255

A huge amount of refactoring of [sssom-py](https://github.com/mapping-commons/sssom-py) and development best practices, as well as training materials, was provided through this grant (awarded to Benjamin M. Gyori). Other contributions include work on the [Semantic mapping reasoner and assembler](https://github.com/biopragmatics/semra)
