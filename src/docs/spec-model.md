# The SSSOM data model

The SSSOM data model (hereafter “the model”) defines the data structure to represent and manipulate SSSOM concepts. The model is formally described as a [LinkML](https://linkml.io/) schema, from which the [documentation](linkml-index.md) is derived.

This section provides an overview of the model and supplementary information that may not be found in the schema (and its derived documentation) itself. Of note, the schema, not this section, is always the authoritative source of truth for all questions pertaining to the model.

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

* slots that provide information about the set itself;
* slots that provide information about all the mappings in the set.

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
* `subject_type`,
* `predicate_type`,
* `similarity_measure`.

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


## Literal mappings

<a id="literal-mappings"></a>

The SSSOM model is primarily intended to represent mappings between semantic entities. However, it may also be used to represent mappings where at least one side is a literal string that does not have an identifier of its own. Any such mapping is henceforth called a _literal mapping_.

To represent a mapping whose subject (resp. object) is a literal:

* the `subject_type` (resp. `object_type`) slot MUST be set to `rdfs literal`;
* the `subject_label` (resp. `object_label`) slot MUST be set to the literal itself;
* the `subject_id` (resp. `object_id`) slot MAY be left empty.

The last point is an exception to the normal rules about required slots, which state that a mapping must always have a `subject_id` and an `object_id`. Implementations MUST accept a mapping without a `subject_id` (resp. `object_id`) _if and only if_ the `subject_type` (resp. `object_type`) slot is set to `rdfs literal`.

All other slots in the `Mapping` class may be used normally in a literal mapping, with the same meaning as for a non-literal mapping.

When computing the cardinality of mappings in a set (e.g. to set the value of the `mapping_cardinality` slot), if the mapping has a literal subject (resp. object), then the `subject_label` (resp. `object_label`) slot must be used for determining the number of occurrences of the subject (resp. object) in the set.


## Representing unmapped entities

The special value `sssom:NoTermFound` MAY be used as the `object_id` of a mapping to explicitly state that the subject of said mapping cannot be mapped to any entity in the domain represented by the `object_source` slot.

Likewise, the `sssom:NoTermFound` value MAY be used as the `subject_id` of a mapping to state that the object of said mapping cannot be mapped to any entity in the domain represented by the `subject_source` slot.

When that special value is used as the `subject_id` (respectively `object_id`), the `subject_source` (respectively `object_source`) slot SHOULD be defined.

The `sssom:NoTermFound` value MUST NOT be used in any other slot than `subject_id` or `object_id`.

The meaning of the NOT predicate modifier in a mapping that refers to `sssom:NoTermFound` is unspecified.

When computing cardinality values (to fill the `mapping_cardinality` slot), mappings that refer to `sssom:NoTermFound` MUST be ignored.


## Non-standard slots

<a id="non-standard-slots"></a>

Implementations are only REQUIRED to support the standard metadata slots defined in the SSSOM LinkML schema.

However, implementations MAY support the use of supplementary, non-standard slots (hereafter called _extension slots_ or simply _extensions_). There are two types of extension slots: _defined_ extension slots and _undefined_ extension slots.

### Defined extensions

Defined extensions are non-standard slots that are explicitly declared (or, _defined_) before being used. Implementations SHOULD support the use of defined extensions.

Extensions are defined in the `extension_definition` slot of the `MappingSet` object. Each definition is comprised of three elements:

* the name of the slot, as it will appear when used in a mapping set (`slot_name`);
* a property intended to specify the meaning of the slot (`property`);
* the type of values expected by the slot (`type_hint`).

A definition MUST have at least a `slot_name`. The name MUST be a XML “non-colonized name” (“NCName”, see [Namespaces in XML, §2](https://www.w3.org/TR/1999/REC-xml-names-19990114/#NT-NCName)). The name MUST NOT match the name of an existing standard slot.

To avoid any conflicy with a future version of the SSSOM specification (which could introduce new standard slot names), implementations are strongly encouraged to craft extension slot names that start with the `ext_` prefix. No new standard slot with a name starting with `ext_` will ever be introduced in any future version of the standard. (This is an advice for SSSOM producers only; SSSOM consumers MUST NOT reject an extension slot solely on the basis that its name does not start with `ext`.)

A definition SHOULD have a `property`. If it does not, implementations MUST automatically construct a default property by concatenating the prefix `http://sssom.invalid/` with the name of the extension.

The slot name and the property MUST be unique to each definition. No two definitions can share the same name and/or the same property.

A definition MAY have a `type_hint`. If it does not, a default type of `http://www.w3.org/2001/XMLSchema#string` is assumed.

Once defined, an extension slot may be used as a supplementary slot in either the `Mapping` class or the `MappingSet` class (or both), as if it was a normal, standard slot. How those slots are represented internally and provided to client code is left at the discretion of the implementations.

### Undefined extensions

Undefined extensions are non-standard slots that are not explicitly defined as described in the previous section. Implementations MAY support undefined extensions.

Upon encountering a non-standard slot that is not a defined extension, an implementation that supports undefined extensions MUST behave as if the slot had been defined with:

* a `property` constructed by catenating the prefix `http://sssom.invalid/` to the name of the slot;
* a `type_hint` of `http://www.w3.org/2001/XMLSchema#string`.

### Restrictions on the values of extension slots

#### General restrictions

The following restrictions apply to all extension slots, regardless of whether they are defined or undefined.

Each mapping set and each mapping can have at most _one_ value for each extension slot. The expected behaviour upon encountering a repeated extension slot is unspecified.

An extension value MUST be either a string or an instance of a simple data type such as a numerical value (integer or floating point), a boolean value, or a date or datetime value. In particular, composite data structures (e.g. lists or dictionaries) MUST NOT be used as extension values.

It is always possible to use arbitrarily complex values by encoding them as literal strings. However, how complex values would be encoded is out of scope of this specification; implementations MUST treat such values as opaque strings.

#### Further restrictions for typed defined extensions

If a defined extension slot has a `type_hint` other than `http://www.w3.org/2001/XMLSchema#string`, implementations MAY enforce further constraints on extension values based on the type hint, according to the following table:

| Type hint | Constraints |
| --------- | ----------- |
| http://www.w3.org/2001/XMLSchema#integer  | Implementations MAY check that the value is an integer |
| http://www.w3.org/2001/XMLSchema#double   | Implementations MAY check that the value is a floating number |
| http://www.w3.org/2001/XMLSchema#boolean  | Implementations MAY check that the value is either `true` or `false` |
| http://www.w3.org/2001/XMLSchema#date     | Implementations MAY check that the value is a date in the ISO 8601 format (`yyyy-mm-dd`) |
| http://www.w3.org/2001/XMLSchema#datetime | Implementations MAY check that the value is a date and time value in the ISO 8601 format (`yyyy-mm-ddThh:mm:ssTZ`) |

Implementations MAY decide to recognise more types and to enforce type-specific constraints. For example, an implementation could recognise the type `http://www.w3.org/2001/XMLSchema#negativeInteger` and check that the value starts with a minus sign.
