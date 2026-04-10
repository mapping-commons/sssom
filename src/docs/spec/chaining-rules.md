## SSSOM Mapping Chains

The goal of this document is to capture all obvious mapping chaining rules that could be applied to SSSOM, 
and later delivered as part of `sssom toolkit`. 
This is all structural, and should not be confused with proper reasoning or mapping reconciliation ala 
[boomer](https://github.com/INCATools/boomer).

The idea is to provide the functionality to apply these chaining rules over a given mapping set, and record
the appropriate metadata for that rule.

Rules:

- [Transitivity Rule](#transitivity)
- [Role chains over exact/equivalent matches](#rce)
- [Inverse Rule](#inverse)
- [Generalisation Rule](#generalisation)

<a id="transitivity"></a>

## Transitivity Rule

Transitivity of a relation `R` implies that if an entity `A` is `R`-related to an entity `B` which in turn is 
`R`-related to an entity `C`, `A` is also `R`-related to `C`. 

### Predicates applicable in transitivity rules

We consider the following predicates transitive:

- skos:exactMatch
- skos:narrowMatch
- skos:broadMatch
- owl:equivalentClass / owl:equivalentProperty
- rdfs:subClassOf / rdfs:subPropertyOf	
- owl:sameAs

Note that technically speaking `skos:narrowMatch` and `skos:broadMatch` are not considered transitive 
(`skos:broaderTransitive` would be), but we are not defining a new semantics here, 
just a reasonable default for a mapping tool, which will nearly always hold true.

Predicates we do not consider transitive include: `skos:relatedMatch` (for practical reasons), `oboInOwl:hasDbXref`, 
`skos:closeMatch`, `rdfs:seeAlso` (weakest form of a mapping link), `rdf:type`.

### Rules

- T1: `(:A)-[predicate_id]->(:B)-[predicate_id]->(:C)` -> `(:A)-[predicate_id]->(:C)`

### Examples

- T1-EX: `(:A)-[skos:broadMatch]->(:B)-[skos:broadMatch]->(:C)` -> `(:A)-[skos:broadMatch]->(:C)`

<a id="rce"></a>

## Role chains over exact/equivalent matches

Role chains are rules that allow us to bridge across mappings across multiple different properties.
Role chains over exact are simple to define, so we start with these

### Predicates applicable in transitity rules

- skos:narrowMatch
- skos:broadMatch
- skos:closeMatch
- skos:relatedMatch

### Rules for SKOS

- RCE1: `(:A)-[skos:exactMatch|owl:equivalentClass]->(:B)-[predicate_id]->(:C)` -> `(:A)-[predicate_id]->(:C)`
- RCE2: `(:A)-[predicate_id]->(:B)-[skos:exactMatch]->(:C)` -> `(:A)-[predicate_id]->(:C)`

### Rules that should probably not be inferred (OWL)

The following rules hold true, but will be left to a reasoner to be inferred:

- RCE-N1: `(:A)-[owl:equivalentClass]->(:B)-[rdfs:subClassOf]->(:C)` -> `(:A)-[rdfs:subClassOf]->(:C)`
- RCE-N2: `(:A)-[rdfs:subClassOf]->(:B)-[owl:equivalentClass]->(:C)` -> `(:A)-[rdfs:subClassOf]->(:C)`
- RCE-N3: `(:A)-[owl:equivalentProperty]->(:B)-[rdfs:subPropertyOf]->(:C)` -> `(:A)-[rdfs:subPropertyOf]->(:C)`
- RCE-N4: `(:A)-[rdfs:subPropertyOf]->(:B)-[owl:equivalentProperty]->(:C)` -> `(:A)-[rdfs:subPropertyOf]->(:C)`

<a id="inverse"></a>

## Inverse Rules

`R` inverse of `S` implies that if an entity `A` is `R`-related to an entity `B` then `B` is also `S`-related to `A`. 
We like to call the output of an inverse rule a `walk-back`. A command that applies an inverse rule could be called `flip`. 

### Predicates applicable in inverse rules

This excludes the exact predicates for which inverse rules are redundant.

### Rules for SKOS

- RI1: `(:A)-[skos:narrowMatch]->(:B)` -> `(:B)-[skos:broadMatch]->(:A)`
- RI2: `(:A)-[skos:broadMatch]->(:B)` -> `(:B)-[skos:narrowMatch]->(:A)`

### Rules for SEMAPV

- RI3: `(:A)-[semapv:crossSpeciesExactMatch]->(:B)` -> `(:B)-[semapv:crossSpeciesExactMatch]->(:A)`
- RI4: `(:A)-[semapv:crossSpeciesNarrowMatch]->(:B)` -> `(:B)-[semapv:crossSpeciesBroadMatch]->(:A)`
- RI5: `(:A)-[semapv:crossSpeciesBroadMatch]->(:B)` -> `(:B)-[semapv:crossSpeciesNarrowMatch]->(:A)`

<a id="generalisation"></a>

## Generalisation Rules

Generalisation rules are rules that can be applied to weaken a mapping deliberately. This is sometimes useful, for example when
combining strong OWL-Semantics mappings with weaker SKOS-based ones.

## Rules

- RG1: `(:A)-[owl:equivalentTo]->(:B)` -> `(:A)-[skos:exactMatch]->(:B)`
- RG2: `(:A)-[owl:subClassOf]->(:B)` -> `(:A)-[skos:broadMatch]->(:B)`
