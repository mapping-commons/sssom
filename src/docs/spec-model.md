# The SSSOM data model

The SSSOM data model (hereafter “the model”) defines the data structure to represent and manipulate SSSOM concepts. The model is formally described as a [LinkML](https://linkml.io/) schema, from which the [documentation](linkml-index.md) is derived.

This section provides an overview of the model and supplementary informations that may not be found in the schema (and its derived documentation) itself. Of note, the schema, not this section, is always the authoritative source of truth for all questions pertaining to the model.

## Overview

The model consists in a handful of classes, the most important of them being the [`Mapping` class](Mapping.md) and the [`MappingSet` class](MappingSet.md). Any SSSOM implementation MUST support those two classes and all their slots; support for the other classes is OPTIONAL.

The `Mapping` class represents an individual mapping. Fundamental slots in that class are:

* `subject_id` and `object_id`, referring to the entities being mapped to each other;
* `predicate_id`, referring to the relationship between the mapped entities;
* `mapping_justification`, which should provide the justification for the mapping.

Those slots are mandatory (including the `mapping_justification` slot: the SSSOM standard posits that there can be no mapping without some form of justification) and an implementation MUST NOT allow the creation of a mapping object that does not have a value for any one of them.

Other slots are intended to provide further details about a mapping. Those “further details” are sometimes referred to as “mapping metadata”, though the SSSOM standard makes no formal distinction between “data” and “metadata” – there are only “data about a mapping”.

The `MappingSet` class represents, well, a set of individual mappings, which are contained in the `mappings` slot (a list of `Mapping` instances). Other slots in that class are intended either to provide further details about the set itself (sometimes referred to as “mapping set metadata”, with the same caveat as above regarding the data/metadata distinction), or to provide common details for all the mappings in the set (see the [Propagation of mapping set slots](#propagation-of-mapping-set-slots) section further below for details).

Of note, within a set, a mapping may not necessarily be uniquely identified by the combination of its four mandatory slots (`subject_id`, `predicate_id`, `object_id`, and `mapping_justification`). A set may very well contain several mappings with the same subject, predicate, object, and justification, but that differ on some of the other, complementary slots.


## Identifiers

Throughout the model, identifiers to external resources are represented using the custom type [`EntityReference`](EntityReference.md) (based on the LinkML type [`uriorcurie`](https://w3id.org/linkml/Uriorcurie)), which accepts both full-length IRIs and [CURIEs](https://www.w3.org/TR/curie/) as possible identifier formats. (Note however that serialisation formats may mandate the use of one identifier format over the other; for example, the [SSSOM/TSV](spec-formats-tsv.md) format requires the systematic use of CURIEs, whereas the [OWL/RDF](spec-formats-owl.md) format conversely requires the systematic use of IRIs).

Whenever the CURIE syntax is used in a mapping set (whether this is by choice of the SSSOM producer, or because it is mandated by the serialisation format), all CURIEs MUST be unambiguously resolvable into corresponding full-length IRIs without requiring any external resources. This means that any prefix name used MUST be properly declared in the set’s `curie_map` slot, which is a dictionary associating a prefix name to an IRI prefix.

By exception, prefix names listed in the table found in the [IRI prefixes](spec-intro.md#iri-prefixes) section are considered “built-in”. As such, they MAY be omitted from the `curie_map`. If they are not omitted, they MUST point to the same IRI prefixes as in the aforementioned table.


## Propagation of mapping set slots

As mentioned briefly above, there are two different types of slots in the `MappingSet` class:

* slots that provide informations about the set itself;
* slots that provide informations about all the mappings in the set.

The latter are called “propagatable slots”. In the LinkML model, they are marked with a `propagated` annotation whose value is set to `true`.

For convenience, here is the current list of propagatable slots:

* `mapping_date`,
* `mapping_provider`,
* `mapping_tool`,
* `mapping_tool_version`,
* `object_match_field`,
* `object_preprocessing`,
* `object_source`,
* `object_source_version`,
* `object_type`,
* `subject_match_field`,
* `subject_preprocessing`,
* `subject_source`,
* `subject_source_version`,
* `subject_type`.

When a mapping set object has a value in one of its propagatable slots, this MUST be interpreted as if all mappings within the set had that same value in their corresponding slot. For example, if a set has the value _foo_ in its `mapping_tool` slot, all the mappings in that set MUST be treated as if they had the value _foo_ in their `mapping_tool` slot.

This mechanism is intended as a convenience, so that a slot which has the same value for all mappings in a set can be specified only once at the level of the set rather than for each individual mapping.

Slots that are not in the above list (“non-propagatable slots”) describe the mapping set itself, not the mappings it contains, even if the slot also exists on the `Mapping` class. For example, the `creator_id` slot, when used in the `MappingSet` class, is intended to refer to the creators of the set, _not_ the creators of the individual mappings (which may be different, and which are listed in the `creator_id` slot of every mapping).


## Allowed and common mapping predicates

Implementations MUST accept any arbitrary predicate in the `predicate_id` slot.

The following mapping predicates are considered common, and implementations MAY encourage users to use them:

| Predicate | Description |
| --------- | ----------- |
| owl:sameAs | The subject and the object are instances (OWL individuals), and the two instances are the same. |
| owl:equivalentClass | The subject and the object are OWL classes, and the two classes are the same. |
| owl:equivalentProperty | The subject and the object are OWL object, data, or annotation properties, and the two properties are the same. |
| rdfs:subClassOf | The subject and the object are OWL classes, and the subject is a subclass of the object. |
| rdfs:subPropertyOf | The subject and the object are OWL object, data, or annotation properties, and the subject is a subproperty of the object. |
| skos:relatedMatch | The subject and the object are associated in some unspecified way. |
| skos:closeMatch | The subject and the object are sufficiently similar that they can be used interchangeably in some information retrieval applications. |
| skos:exactMatch | The subject and the object can, with a high degree of confidence, be used interchangeably across a wide range of information retrieval applications. |
| skos:narrowMatch | The object is a narrower concept than the subject. |
| skos:broadMatch | The object is a broader concept than the subject. |
| oboInOwl:hasDbXref | Two terms are related in some way. The meaning is frequently consistent across a single set of mappings. Note this property is often overloaded even where the terms are of a different nature (e.g. interpro2go). |
| rdfs:seeAlso | The subject and the object are associated in some unspecified way. The object IRI often resolves to a resource on the web that provides additional information. |

In addition, predicates from the following sources MAY also be encouraged:

* any relation from the [Relation Ontology (RO)](https://obofoundry.org/ontology/ro.html);
* any relation under [skos:mappingRelation](http://www.w3.org/2004/02/skos/core#mappingRelation) in the [Semantic Mapping Vocabulary](https://mapping-commons.github.io/semantic-mapping-vocabulary/).
