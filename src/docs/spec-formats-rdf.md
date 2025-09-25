# The SSSOM/RDF serialisation format

This section defines how to represent a SSSOM mapping set as a
[RDF model](https://www.w3.org/TR/rdf11-concepts/).

## RDF formats

The RDF model that represents a SSSOM mapping set is independent of the concrete
format that may be used to serialise the model.

It is RECOMMENDED that implementations support reading and writing a SSSOM set
from and to the [RDF Turtle](https://www.w3.org/TR/turtle/) format at least.
They MAY support any other RDF concrete format (e.g. RDF/XML, TriG, N-Triples,
etc.).

This specification does not mandate how a concrete RDF syntax is to be used. For
example, if the RDF syntax allows named resources and predicates to be
serialised as either IRIs or CURIEs, if is left at the discretion of the
implementations (or their users) to decide which form to use.

<a id="sssom-slots"></a>

## Representation of slots

A metadata slot on any given SSSOM object (such as a `Mapping` or a
`MappingSet`) MUST be represented as a RDF triple where:

- the subject is the resource representing the SSSOM object;
- the predicate is either:
  - the property indicated by the `URI` field in the LinkML description of the
    slot, if such a field is present;
  - or a property constructed by concatenating the `https://w3id.org/sssom/`
    namespace and the name of the slot;
- the object is the value of the slot.

### Representation of slot values

The following rules determine how the value of a slot is represented as the
object of a RDF triple.

#### For slots typed as `sssom:EntityReference`

(e.g. `subject_id`, `mapping_justification`, `subject_source`…)

The value MUST be represented as a named RDF resource (IRI).

#### For slots typed as `sssom:NonRelativeURI`

(e.g. `license`, `mapping_provider`, `issue_tracker`…)

The value MUST be represented as a named RDF resource (IRI).

#### For slots typed as `linkml:date`

(e.g. `mapping_date`, `publication_date`)

The value MUST be represented as a `xsd:date` literal.

#### For slots typed as `linkml:double`

(e.g. `mapping_set_confidence`, `confidence`, `similarity_score`)

The value MUST be represented as a `xsd:double` literal.

#### For slots typed as an enumeration

(e.g. `sssom_version`, `mapping_cardinality`, `subject_type`…)

If the permissible values for the enumeration are defined in the LinkML model as
having an associated `meaning` property, then the value MUST be represented as a
named RDF resource with the indicated property. Otherwise, the value MUST be
represented as a `xsd:string` literal.

#### For slots typed as a SSSOM object

(e.g. `mappings`, `extension_definitions`)

The value MUST be represented as a RDF resource. Whether the resource is named
(IRI) or not (blank node) will depend on the type of the object, see the
[section on representing SSSOM objects](#sssom-objects) below for details.

### Representation of multi-valued slots

(e.g. `creator_id`, `see_also`, `object_match_field`…)

As an exception to the general principle that slots are represented by a single
RDF triple, multi-valued slots MUST be represented by as many triples as there
are values, each value being the object of one triple.

> Non-normative notes:
>
> 1. This means, in particular, that RDF complex structures intended to
>    represent collections of values, such as `rdfs:Container` or `rdfs:List`,
>    MUST NOT be used to represent multi-valued SSSOM slots.
> 2. This also implies that values in multi-valued slots are _not_ ordered.

The other rules above apply to determine how each single value is to be
represented.

> Example:
>
> A `creator_id` slot with the values `https://example.org/people/0001` and
> `https://example.org/people/0002` is represented by the following two triples:
>
> ```ttl
> ?object dcterms:creator <https://example.org/people/0001> .
> ?object dcterms:creator <https://example.org/people/0002> .
> ```

<a id="extension-slots"></a>

### Representation of extension slots

An [extension slot](spec-model.md#non-standard-slots) MUST be represented in a
similar way to a standard slot, with the following specific rules.

The predicate is the property associated to the extension slot, as indicated by
the `property` slot in the set’s [definition](ExtensionDefinition.md) of the
extension.

The value of the extension MUST be represented:

- as a named RDF resource, if the `type_hint` of the extension definition is
  `linkml:uriOrCurie`;
- otherwise, as a literal of the type indicated by the `type_hint`.

<a id="sssom-objects"></a>

## Representation of SSSOM objects

### Representation of a `Mapping` object

The RDF type of a `Mapping` object is `owl:Axiom`.

If the `Mapping` object has a `record_id` slot, then the value of that slot MUST
be used as the named RDF resource that represents the object (and consequently,
that slot MUST NOT be represented using the [general rules](#sssom-slots) for
the representation of slots as defined above). Otherwise, the `Mapping` object
is represented as a blank node.

### Representation of a `MappingSet` object

The RDF type of a `MappingSet` object is `sssom:MappingSet`.

A `MappingSet` object MUST be represented by a named RDF resource corresponding
to the value of the `mapping_set_id` slot (which consequently MUST NOT be
represented using the [general rules](#sssom-slots) for the representation slots
as defined above).

The `curie_map` slot MUST NOT be represented using the
[general rules](#sssom-slots). Instead, if it is needed it MUST be represented
using whatever mechanism is provided by the concrete RDF serialisation format
(e.g. `@prefix` declarations in [RDF Turtle](https://www.w3.org/TR/turtle/) or
[RDF TriG](https://www.w3.org/TR/trig/), or `xmlns` namespace declarations in
[RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/)).

> Non-normative notes
>
> 1. The CURIE map may not be needed at all if all named resources and
>    predicates are always serialised as full-length IRIs.
> 2. If at least some named resources or predicates are serialised as CURIEs,
>    the RDF requirement that all used prefix names must be declared (using the
>    appropriate mechanism for the chosen concrete syntax) takes precedence over
>    the possibility of omitting the declarations of prefix names that are
>    considered [built-in](spec-intro.md#iri-prefixes) in the context of SSSOM.

### Representation of a `ExtensionDefinition` object

The RDF type of a `ExtensionDefinition` object is `sssom:ExtensionDefinition`.

A `ExtensionDefinition` object has no identifier of any kind and is always
represented by a blank node.

## Special considerations for serialising to RDF

When serialising a mapping set to SSSOM/RDF, implementations should consider how
the resulting RDF file is intended to be used. In particular, they should ponder
whether it is expected that the RDF serialisation can at any time be converted
back to any other SSSOM format (e.g. SSSOM/TSV), or if it is only intended to be
used by “generic”, non-SSSOM-aware RDF applications.

Depending on that intended usage (if it is known), implementations may adopt
slightly different behaviours as described in the following subsections.

### Serialisations of identifiers

If the serialisation is intended to be convertible back to another SSSOM format
(especially the SSSOM/TSV format), implementations MUST declare all the prefixes
found in the CURIE map and SHOULD serialise all identifiers as CURIEs using said
declared prefixes.

> Non-normative explanation
>
> This is because, if all identifiers are serialised as full-length IRIs, then
> even if the RDF file includes prefix declarations, they may be stripped away
> by a RDF reader, since they are not needed. And without those prefix
> declarations, it would not be possible to serialise the set back as a
> SSSOM/TSV file (remember that the SSSOM/TSV format _requires_ that identifiers
> be serialised as CURIEs).

Conversely, if the ability to convert the RDF file back to another SSSOM format
is not required, implementations can freely decide whether to serialise
identifiers as IRIs or CURIEs (assuming the concrete RDF syntax allows that of
course).

### Extension definitions

Extension definitions MAY be omitted if the RDF file is only intended to be used
by RDF applications.

Conversely, they SHOULD be included if the set is intended to be convertible
back to another SSSOM format.

> Non-normative explanation
>
> The whole point of an extension definition in SSSOM is to provide (1) a
> property that confers some meaning to the extension, and (2) the type of the
> expected values. In RDF, as described [above](#extension-slots), those two
> bits of information are already contained in the triple that represent the
> extension slot, so there is no need for an additional definition.
>
> But the extension definition also provides the `slot_name` which is used to
> represent the extension slot in other formats (especially SSSOM/TSV), so if
> conversion back to other SSSOM formats is required, ensuring that the
> extension definitions are present in the RDF serialisation is helpful.

### Propagation and condensation

Propagatable slots can be represented in RDF indifferently in their propagated
or condensed form, following the
[normal rules](spec-model.md##propagation-of-mapping-set-slots) for propagation
and condensation.

But if the RDF file is intended to be used by generic, non-SSSOM-aware RDF
applications, then implementations SHOULD serialise propagatable slots in their
propagated form.

> Non-normative explanation
>
> Propagation is a SSSOM-specific concept. If a RDF application is provided with
> a RDF file representing a set with condensed slots, the application will not
> know to propagate the condensed slots at the set level down to the level of
> the individual mappings, which will result in the application having an
> incomplete view of the mappings.

### Representation of mappings as “direct triples”

For every single mapping record in a set, implementations MAY _additionally_
inject a single triple of the form:

```ttl
?subject_id ?predicate_id ?object_id .
```

If so, that behaviour MUST be optional.

When that behaviour is enabled, implementations SHOULD NOT inject such triples
in the following cases:

- when the record represents a literal mapping (that is, `subject_type` or
  `object_type` – or both – is set to `rdfs literal`);
- when the record represents a negated mapping (that is, `predicate_modifier` is
  set to `Not`);
- when the record represents an absence of match (that is, `subject_id` or
  `object_id` – or both – is set to `sssom:NoTermFound`).

In any case, a SSSOM/RDF reader MUST NOT expect the presence of such triples,
and if they are present MUST NOT use them to construct mapping records.

> Non-normative explanations
>
> Such “direct triples” are merely a convenience for downstream RDF
> applications, allowing them to find a direct link (as a single triple) between
> the subject and the object of a mapping, without having to construct such a
> link by following the `owl:annotatedSource`, `owl:annotatedProperty`, and
> `owl:annotatedTarget` triples.
>
> It is recommended not to inject such direct triples for literal mapping
> records, even if they do have a `subject_id` and a `object_id`, because by
> definition the subject and/or the object of such records is not an
> identifiable semantic entity and has no business being represented in a RDF
> graph.
>
> It is recommended not to inject such direct triples for negated mapping
> records because they would seem to convey a meaning that is the exact opposite
> of what the records mean.
>
> It is recommended not to inject such direct triples for no-match mapping
> records since they do not represent a real mapping.

## Compatibility with pre-standard RDF representations

The present specification of the SSSOM/RDF format differs slightly from what
several implementations of SSSOM have been producing before the format was
formally specified.

In the name of backward compatibility, implementations MAY support the
alternative rules described in the following subsections when deserialising from
RDF.

Implementations MUST NOT follow these rules when serialising to RDF.

### Representation of slots typed as `sssom:NonRelativeURI`

Implementations MAY accept a value represented as a `xsd:anyURI` literal.

### Representation of slots typed as an enumeration

Implementations MAY accept a value represented as a string literal, even if the
value is defined in the LinkML model as having an associated `meaning` property.

For example, implementations MAY accept

```ttl
?mapping sssom:predicate_modifier "Not"^^xsd:string .
```

as an alternative to

```ttl
?mapping sssom:predicate_modifier sssom:NegatedPredicate .
```

### Representation of a `MappingSet` object

Implementations MAY accept a `MappingSet` object represented as a blank node,
with the `mapping_set_id` slot being represented as any other slot.

For example, instead of

```ttl
<https://example.org/myset> a sssom:MappingSet .
```

implementations MAY accept

```ttl
[] a sssom:MappingSet ;
   sssom:mapping_set_id <https://example.org/myset> .
```

or even (by also applying the alternative rule regarding the representation of
slots typed as `sssom:NonRelativeURI`)

```ttl
[] a sssom:MappingSet ;
   sssom:mapping_set_id "https://example.org/myset"^^xsd:anyURI .
```

## Examples

> This section is non-normative.

Considering the following set in the SSSOM/TSV format:

```
#curie_map:
#  EXT: https://example.org/properties/
#  FOODON: http://purl.obolibrary.org/obo/FOODON_
#  KF_FOOD: https://kewl-foodie.inc/food/
#  ORCID: https://orcid.org/
#mapping_set_id: https://example.org/sample-set
#mapping_set_description: Manually curated alignment of KEWL FOODIE INC internal food and nutrition database with Food Ontology (FOODON). Intended to be used for ontological analysis and grouping of KEWL FOODIE INC related data.
#license: https://creativecommons.org/licenses/by/4.0/
#mapping_date: 2025-07-14
#extension_definitions:
#  - slot_name: ext_fooable
#    property: EXT:isFooable
#    type_hint: xsd:boolean
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification	author_id	confidence	ext_fooable
KF_FOOD:F001	apple	skos:exactMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	ORCID:0000-0002-7356-1779	0.95	true
KF_FOOD:F002	gala	skos:exactMatch	FOODON:00003348	Gala apple (whole)	semapv:ManualMappingCuration	ORCID:0000-0002-7356-1779	1	false
```

A valid serialisation of that set in RDF/Turtle would be:

```ttl
@prefix EXT: <https://example.org/properties/> .
@prefix FOODON: <http://purl.obolibrary.org/obo/FOODON_> .
@prefix KF_FOOD: <https://kewl-foodie.inc/food/> .
@prefix ORCID: <https://orcid.org/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix pav: <http://purl.org/pav/> .
@prefix semapv: <https://w3id.org/semapv/vocab/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sssom: <https://w3id.org/sssom/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/sample-set> a sssom:MappingSet;
  dcterms:description "Manually curated alignment of KEWL FOODIE INC internal food and nutrition database with Food Ontology (FOODON). Intended to be used for ontological analysis and grouping of KEWL FOODIE INC related data.";
  dcterms:license <https://creativecommons.org/licenses/by/4.0/>;
  sssom:extension_definitions [
      sssom:property EXT:isFooable;
      sssom:slot_name "ext_fooable";
      sssom:type_hint xsd:boolean
    ];
  sssom:mappings [ a owl:Axiom;
      pav:authoredBy ORCID:0000-0002-7356-1779;
      dcterms:created "2025-07-14"^^xsd:date;
      owl:annotatedProperty skos:exactMatch;
      owl:annotatedSource KF_FOOD:F001;
      owl:annotatedTarget FOODON:00002473;
      EXT:isFooable true;
      sssom:confidence 9.5E-1;
      sssom:mapping_justification semapv:ManualMappingCuration;
      sssom:object_label "apple (whole)";
      sssom:subject_label "apple"
    ], [ a owl:Axiom;
      pav:authoredBy ORCID:0000-0002-7356-1779;
      dcterms:created "2025-07-14"^^xsd:date;
      owl:annotatedProperty skos:exactMatch;
      owl:annotatedSource KF_FOOD:F002;
      owl:annotatedTarget FOODON:00003348;
      EXT:isFooable false;
      sssom:confidence 1.0E0;
      sssom:mapping_justification semapv:ManualMappingCuration;
      sssom:object_label "Gala apple (whole)";
      sssom:subject_label "gala"
    ] .
```

Note that the two `Mapping` objects are represented as blank nodes, since the
original set does not contain any `record_id` slot.

Note also that (1) identifiers are serialised as CURIEs whenever possible, and
(2) the definition for the `EXT:isFooable` extension is included. This means
that the set can be fully converted back to SSSOM/TSV without any loss of
information.
