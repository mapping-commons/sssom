# How to pick the right mapping predicates

A mapping predicate such as skos:exactMatch specifies the semantics of the mapping relation - in other words, it defines how a computer (and human!) should interpret the mapping when it is being used. For example, a computer program may be allowed to merge nodes in a knowledge graph _only when they are `skos:exactMatch`_, but not when they are, say, `skos:closeMatch`.

Picking the right predicate to specify the meaning of your mapping is often a difficult process. The following guide should help you to understand the most widely used mapping predicates and when they are appropriate.

## Table of content

- [The three primary concerns for selecting a mapping predicate](#primary)
- [The 3 step process for selecting an appropriate mapping predicate](#tenstep)
- [Frequently asked questions about mapping predicates](#faq)

## Glossary

- `subject`: the entity that is being mapped
- `object`: the entity that the `subject` is mapped to
- `predicate`: the semantic mapping relationship used

<a id="primary"></a>

## The three primary concerns for selecting a mapping predicate

There are at least three things you need to decide before selecting an appropriate mapping predicate:

1. [Precision](#precision)
2. [Acceptable degree of noise](#noise)
3. [Intended use case](#use-case)

<a id="precision"></a>

### What is the **precision** of the mapping? 

As a curator, you should try to investigate the **intended meaning** of both the subject and the object. This task usually involves trying to find out as much as possible about the mapped identifiers: What is their human readable definition? Are there any logical axioms that could help with understanding the intended meaning? Sometimes, this even involves asking the respective stewards of the database or ontology for clarification. **Important:** The key here is "intended meaning". For example, when you see `FOODON:Apple` (FOODON is an ontology), you do not try to figure out _what an apple is_, but what thing in the world (in your conceptual model of the world) the FOODON developers _intended the `FOODON:Apple` identifier to refer to_. This might be an apple that you can eat, or a [cultivar](https://en.wikipedia.org/wiki/List_of_apple_cultivars)!

The **precision** is simply: is the mapping `exact`, `close`, `broad`, `narrow` or `related`? Here is a basic guide about how to think of each:

- `exact`: The two terms are intended to refer to the same thing. For example, both the subject and the object identifiers refer to the concept of [Gala cultivar](https://en.wikipedia.org/wiki/Gala_(apple)).
- `close`: The two terms are intended to refer to roughly the same thing, but not quite. This is a hazy category and should be avoided in practice, because when taken too literally, most mappings could be interpreted as close mappings. This is not the point of creating mappings, if their intention is to be useful (see "use case" considerations later in this document). An example of a `close` mapping is one between the "heart" concept in a database of anatomical entities for biological research on chimpanzees and the "human heart" in an electronic health record for humans.
- `broad`: The object is conceptually broader than the subject. For example, "human heart" in an electronic health record refers to "heart" in a general anatomy ontology that covers all species, such as Uberon. Another example is "Gala (cultivar)" in one ontology or database to "Apple (cultivar)" in another: the Apple (cultivar) has a broader meaning then "Gala (cultivar)". For a good mapping, it is advisable that "broad" and "narrow" are applied a bit more strictly than is technically permitted by the SKOS specification: both the subject and the object should belong to the same **category**. For example, you should use broad (or narrow) only if both the subject and the object are "cultivars" (in the above example).
- `narrow`: The object is conceptually narrower than the subject. For example "Apple (cultivar)" is a narrow match to "Gala (cultivar)". Think of it as the opposite of "broad". `broad` and `narrow` are so-called inverse categories: If "Gala (cultivar)" is a `broad` match to "Apple (cultivar)", then "Apple (cultivar)" is a `narrow` match to "Gala (cultivar)"! One **note of caution**: `narrow` matches generally have less useful applications then `broad` ones. For example, if we want to _group_ subject entities in a database under an ontology to make them queryable in a knowledge graph, only `broad` matches to the ontology can be retrieved. For example, if we map "Gala (cultivar)" in a database to "Apple (cultivar)" in an ontology, and we wish to write a semantic query to obtain all records that are about "Apple (cultivar)" according to the ontology, we obtain "Gala (cultivar)". This is not true the other way around: if the ontology term is _more_ specific then the database term, it can't be used to group the database data.
- `related`: The subject refers to an analogous concept of a different category. For example "Apple" and "Apple tree" are considered `related` matches, but not `exact` matches, as "Apple" is of the "fruit" category, and "Apple tree" of the "tree" category. Other examples include: "disease" and "phenotype", "chemical" and "chemical exposure", "car" and "car manufacturing process". In general, `related` mappings should be reserved for "direct analogues". For example, we should not try to map to `related` and `broad` categories at the same time, like, for example, "Gala (cultivar)" to "Apple tree". This causes a huge amount of proliferation of very "low value" mappings (see use case section later).

<a id="noise"></a>

### What is the **acceptable degree of noise** of the mapping?

"Noise" is the permissible margin of error for some target use case. Depending on what you want to do with your mappings, different quality levels are acceptable. This section is _not exhaustive_. 

While reading through this section, you should keep one thing in mind: it is _never_ a good idea to think about mappings as "correct" or "wrong". Even the the exact same identifier (for example in Wikidata, or even the biomedical data domain) can mean something very different depending on which database it is using it or in which part of which datamodel (or value set) they are used. Mapping should therefore be perceived as an inexact art where the goal is not "correctness" but "fitness for purpose": can the mappings deliver the use case I am interested in? In the following, we will take a closer look at the varying levels of noise you may need to weigh against each other.

- "zero-noise". Some mappings directly inform decision processes of downstream consumers, such as clinical decision support or manufacturing. For example, in an electronic health record (EHR) system we may want to know what the latest recommended drugs (or contra-indications) for a conditions are, and the disease-drugs relationships may be curated using one terminology such as [OMOP](https://ohdsi.org/omop), and the EHR may be represented using [ICD10-CM](https://icd.codes/icd10cm) (a clinical terminology used widely by hospitals). In these cases, noise should be zero or close to zero, as patient lives depend on the correctness of these mappings.
- "low-noise". Most mappings are used to augment/inform processes that are a bit upstream of the final consumer. For example, mappings are used to group data for analysis or make it easier to find related data during search (enhancing search indexing semantically). The final consumer does not immediately "see" the mappings, but  just  the consequences of applying the mappings. In these cases, a bit of noise may be acceptable, i.e. some mappings that are "not quite right". Practically, this is very often the case where data sources are aligned automatically to enable searches across, so a few bad mappings are better than having none. 
- "high-noise": Some use cases employ data processing approaches that are themselves highly resilient to noise, like Machine Learning. Here, even a larger number of mappings (in a knowledge graph for example) which are "not quite right", or noisy, may be acceptable (if the signal to noise ratio is still ok, i.e. there are "more good than bad" mappings).

There is no easy formula by which you can decide what level of noise is acceptable. Your use case will determine this. What you, as the steward of your organisation's mapping data, should consider is that there is (roughly) an order of magnitude in cost involved between the three levels:

- "high-noise": Very cheap to generate. Automated matching tools can be used to generate the mappings, with no human review required. Your system may implement a way for your consumers to flag up bad results which can be traced back to a bad mapping, and simply exclude them moving forward.
- "low-noise": Moderately expensive. Most mappings are generated using automated matchers, but then confirmed by a human curator. The confirmation process can often be "hand-wavy" to weed out obviously bad mappings, but do not involve the same rigour as "zero-noise" mappings would require to maintain scalability to large volumes of mappings. Such a "hand-wavy" confirmative review can take 10 seconds to 100 seconds (if a quick lookup is required).
- "zero-noise": Very expensive. Every mapping must be carefully reviewed by a human curator, sometimes by a group of curators. In our experience, reviewing or establishing a mapping like this (manually) can take anything between 10 and 30 minutes - occasionally more.

You can use these estimated costs for mapping review to determine how much it would cost to apply the same level of rigour to your own mappings.

<a id="use-case"></a>

### What is the intended use case?

This section is informative, not exhaustive, and will give you a sense of how use cases affect your choice of mapping predicate.

We have covered some implications of use cases in the sections above:

1. Some use cases require lower _levels of noise_, others can live with higher levels of noise.
2. Mappings are rarely 100% exact when mapping across semantic spaces (different database, ontologies, terminologies). What matters is not "correctness" - what matters is that the mappings are "_fit for purpose_" (i.e. useful for your use case).
3. Some mappings may be of _more value_ for your use case than others (for example, `exact` mappings may be more valuable than `broad` mappings). You can find the right level of cost benefit by selecting optimising value and cost of generating/maintaining such mappings. `close` mappings may often have a very low value, but if your acceptable level of noise is high, just generate them, since they don't cost you anything!

Other key considerations in the sections are:

- [Semantic frameworks for analysis and querying](#uc-semantic)
- [Instance vs concept-level mapping](#instance)
- [Typical use cases](#uc-typical)

<a id="uc-semantic"></a>

#### Semantic frameworks for analysis and querying

There are four semantic frameworks/formalisms that default SSSOM supports: (1) [SPARQL/RDF(S)](https://www.w3.org/TR/rdf-sparql-query/) (querying an integrated knowledge with basic SPARQL); (2) [Simple Knowledge organisation systems (SKOS)](https://www.w3.org/TR/skos-reference/); (3) [Web Ontology Language (OWL)](https://www.w3.org/TR/owl2-syntax/); (4) no formalism (property graphs, non-semantic use cases). We will briefly discuss the implications of each for your use cases.

- SPARQL/RDF(S) is a very general semantic framework that allows query across [property paths](https://www.w3.org/TR/sparql11-property-paths/). Many SPARQL engines provide at least RDFS entailment regime, which allows for some (basic) semantic reasoning (subClassOf, property domains). This is the most likely semantic framework of choice if your use case involves semantic queries such as those involving sub-class groupings.
- SKOS is a semantic framework that layers on top of RDF and specifies semantics for a handful of properties that are useful for building taxonomies that do not seek to follow the rigorous semantics of the class-level modelling constructs such as subClassOf. We have no experience with SKOS reasoners, and do not know if there are any out there. This means, in effect, that this "case" (semantic framework) has the same exact considerations as the SPARQL/RDF(S) one above.
- OWL is a very powerful semantic framework that is based on formal logic. Ontologies represented in OWL offer support for complex expressions of knowledge, way beyond what RDFS and SKOS can do. OWL is the semantic framework of choice if the goal is to build **and reason** over an integrated (merged) ontology. An example use case where OWL is the appropriate framework is integration of species-specific anatomy ontologies under species-neutral ones, see for example [Uberon](https://github.com/obophenotype/uberon). A basic rule of thumb is: unless you know positively that you have to reason over the _merged_ graph, i.e. set of all ontologies you have mapped across, OWL is probably overkill and should be avoided.
- Using no semantic framework does not mean semantic mappings are useless! Many extremely useful applications exist for mappings which do not involve a semantic framework, such as those related to [Labelled Property Graphs](https://www.oxfordsemantic.tech/fundamentals/what-is-a-labeled-property-graph) (for example [neo4j](https://neo4j.com/)). Even if you just want to translate your data into a graph, it is useful to know the semantics of your mappings as they can inform your graph queries.

Other semantic frameworks exist such as rule-based systems (e.g. Datalog, SWRL), but they are not used as widely as the above in our domain.

<a id="uc-semantic"></a>

#### Instance vs Property vs Concept-level mapping

To pick the correct mapping predicate, it is important to understand whether you are mapping concepts or instances:

- Concept-level: the entity being mapped constitutes a class or a concept. A concept can be thought of a collection or set of individuals. For example, "Apple" could refer to the class of all apples.
- Instance-level: the entity being mapped constitutes an individual or an instance. An instance is a single real-world entity, such as Barack Obama. Instances are members of classes/concepts. For example, Barack Obama belongs to the class of "Person", or "Former Presidents". Another example is an individual apple on a shelf in a supermarket ("Gala Apple 199999"), which is an instance of the "Apple" class.

Note that notions like `broad` or `narrow` make no sense when mapping instances. We typically try to avoid the SKOS vocabulary for mapping instances, and make use of `owl:sameAs` instead. Note that `owl:sameAs` does have implications for reasoning, but it is also the preferred property when within the "RDF/SPARQL" semantic framework.

If the mapping involves an instance _and_ a class, you have hit a corner case of the SSSOM use case. This case can still be represented, but instance-concept relationships are not widely thought of as "mappings".

In much the same way as concepts and instances, you can also map properties or "relationships":

- Property-level: the entities being mapped are both properties, like, for example, rdfs:label, skos:prefLabel, RO:0000050 (part of). 

Note that it does not make sense to try to map instances of concepts, or concepts, directly to properties. There are no relationships that would support such a mapping.

<a id="uc-typical"></a>

#### Typical use cases

Typical use cases for mappings include:

1. _Semantic data integration_. This often involves linking data to ontologies or semantic layers in knowledge graphs. Data from one source (such as an EHR) is translated to another (such as OMOP, see above). To analyse the data semantically, the most valuable links are `exact` and `broad` as these allow you to directly query the ontology to retrieve instance data. `close` and `narrow` matches are less useful for such a use case, but maybe be consulted as the "next best thing" to an exact mapping. Often, a low level of noise is acceptable.
2. _Data translation_. Similar to data integration, but we want to map as precisely as possible. Only `exact` matches really matter if we want to make sure that data annotated with one ontology means the exact same thing as data annotated with another. Noise in the mappings is often not acceptable. An example for this is if one source has annotated all its genes using the HUGO Gene Nomenclature Committee (HGNC) while another is using NCBI Gene Database identifiers. `broad`, `narrow` and even `close` matches are mostly meaningless - we need a 1:1 translation table with next to zero noise.
3. _Ontology and knowledge graph merging_. Here, the key issue is that `exact` matches matches have as little noise as possible. Some merging approaches use probabilistic algorithms to weed out out potentially bad mappings (low levels of noise may be acceptable, see for example [boomer](https://github.com/INCATools/boomer)), but any naive merging approach, which is still prevalent in the knowledge graph world, will usually do the following: (1) Merge all `exact` matches into one "node" in the knowledge graph and (2) redirect all data against all these `exact` matches to that newly created node.

<a id="tenstep"></a>

## The 3-step process for selecting an appropriate mapping predicate

The following 3-step process condenses the sections above into a simple to follow algorithm.

Given two terms A and B:

1. Target: semantic framework: Does your use case require OWL reasoning over the merged subject and object sources?
    - If yes, use OWL vocabulary for properties
    - If no, use RDF/SPARQL/SKOS vocabulary for properties
1. Are A and B instances, properties or concepts?
    - If A and B are instances, use only vocabulary suitable for instances
    - If A and B are concepts, use only vocabulary suitable for concepts
    - If A and B are properties, use only vocabulary suitable for properties
    - If either one of A or B is an instance and the other is a concept, use only vocabulary suitable for describing instance-class relationships
1. Is A roughly the same as B?
    - If yes, does the difference between "truly exact" and your understanding of `A` and `B` constitute "acceptable noise level"?
        - If yes: the mapping is `exact`.
        - If no: the mapping is `close`.
    - If no, determine if the precision as described above.

You can now select the mapping predicate based on the table below:

| Mapping Predicate      | Precision   | Suitable for semantic framework | Suitable entity types? | Acceptable noise |
|------------------------|-------------|---------------------------------|------------------------|------------------|
| skos:exactMatch        | exact       | SKOS/RDF(S)/SPARQL/NO           | Concept                | low              |
| skos:relatedMatch      | related     | SKOS/RDF(S)/SPARQL/NO           | Concept                | low              |
| skos:broadMatch        | broad       | SKOS/RDF(S)/SPARQL/NO           | Concept                | low              |
| skos:narrowMatch       | narrow      | SKOS/RDF(S)/SPARQL/NO           | Concept                | low              |
| skos:closeMatch        | close       | SKOS/RDF(S)/SPARQL/NO           | Concept                | low              |
| owl:sameAs             | exact       | SKOS/RDF(S)/SPARQL/OWL/NO       | Instance               | low              |
| owl:equivalentClass    | exact       | OWL                             | Concept                | no               |
| rdfs:subClassOf        | broad       | RDF(S)/SPARQL/OWL               | Concept                | no               |
| owl:equivalentProperty | exact       | OWL                             | Property               | no               |
| rdfs:subPropertyOf     | broad       | OWL                             | Property               | no               |
| oboInOwl:hasDbXref     | exact       | SKOS/RDF(S)/SPARQL              | Any                    | high             |
| rdfs:seeAlso           | close       | SKOS/RDF(S)/SPARQL              | Any                    | high             |
| rdf:type               | exact/broad | RDF(S)/SPARQL/OWL               | Instance-Concept       | no               |

Note that "acceptable noise" refers to "what is acceptable for the target semantic framework". When using OWL, even a bit of noise can have huge consequences for reasoning, so it is not advisable to use the OWL vocabulary in cases where there is a lot of noise.

<a id="faq"></a>

## Frequently asked questions

1. None of the mapping predicates listed here seem to fit for my use case. Can I define my own?

The SSSOM specification is currently open to specifying new mapping predicates. However, it is always advisable to open an [issue](https://github.com/mapping-commons/sssom/issues) to discuss such cases with the wider community - there may be some benefit in standardising predicates from the start!

