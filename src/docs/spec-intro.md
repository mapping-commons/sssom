# Specification of the SSSOM standard

This document is the official specification for the SSSOM standard.

It is divided in two sections covering the two different components of the standard:

* the specification for the [data model](spec-model.md), to manipulate SSSOM mappings and mapping sets in your programs;
* the specification for the [serialisation formats](spec-formats.md), to read, write, and exchange SSSOM mapping sets.

Both sections are _normative_.

## Conventions used in this document

### Key words

Throughout the specification, the key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” are to be interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14) when, and only when, they appear in all capitals, as shown here.

### IRI prefixes

Throughout the specification, the following IRI prefix names are used:

| Prefix name | IRI prefix |
| ----------- | ---------- |
| owl         | http://www.w3.org/2002/07/owl# |
| rdf         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs        | http://www.w3.org/2000/01/rdf-schema# |
| semapv      | https://w3id.org/semapv/vocab/ |
| skos        | http://www.w3.org/2004/02/skos/core# |
| sssom       | https://w3id.org/sssom/ |
| xsd         | http://www.w3.org/2001/XMLSchema# |
| linkml      | https://w3id.org/linkml/ |
