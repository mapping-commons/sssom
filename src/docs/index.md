# About SSSOM

**SSSOM** is the Simple Standard for Sharing Ontological Mappings. It comprises three distinct components that are intended to be used together to facilitate the exchange of semantic mappings:

1. a machine-readable and extensible vocabulary to describe metadata of mappings;
2. a data model to represent mappings and their associated metadata;
3. several file formats to represent sets of mappings on disk and on the network.

Beyond defining the standard itself, the **SSSOM Core Team** also aims to implement open and community-driven collaborative workflows designed to evolve the standard continuously to address changing requirements and mapping practices, and to provide reference tools and software libraries for working with the standard.


# Basic concepts

A **SSSOM mapping** comprises two components:

1. The **core mapping** (often referred to, for brevity, as simply a “mapping”), which is a triple `<subject, predicate, object>` that reflects a correspondence between a subject entity, for example a class in an ontology, and an object entity, for example an identifier in some database, via a semantic mapping predicate, for example `skos:exactMatch`.
2. The mapping’s **metadata**, which are supplementary pieces of information about the mapping itself. This notably includes information pertaining to the *provenance* of the mapping (for example, who decided that the subject and the object should be mapped) and its *justification* (why should the subject and the object be mapped).

A **SSSOM mapping set** is a collection of SSSOM mappings, with its own metadata.

For a detailed overview see [here](XXX-TODO-XXX).


# Quick links

**General**

- [GitHub page](https://github.com/mapping-commons/sssom)
- [Detailed description](XXX-TODO-XXX)
- [Formal specification](XXX-TODO-XXX)

**Publications**

- [A Simple Standard for Sharing Ontological Mappings (SSSOM)](https://doi.org/10.1093/database/baac035) (initial publication in _Database_)
- [A Simple Standard for Ontological Mappings 2022: Updates of data model and outlook](https://zenodo.org/record/7672104) (paper and presentation at the Ontology Matching Workshop 2022)
- [A Simple Standard for Ontological Mappings 2023: Updates on data model, collaborations and tooling](https://zenodo.org/record/8202395) (paper and presentation at the Ontology Matching Workshop 2023)
- [Other presentations](presentations.md)

**Related software**

- [SSSOM Toolkit](https://mapping-commons.github.io/sssom-py/) (reference implementation of the standard, in Python)
