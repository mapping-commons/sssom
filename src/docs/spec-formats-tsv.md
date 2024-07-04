# The SSSOM/TSV serialisation format

The SSSOM/TSV format is intended as the main format for exchanging SSSOM mapping set objects.

The RECOMMENDED filename extension for a SSSOM/TSV file is `.sssom.tsv`, but SSSOM/TSV parsers MUST accept SSSOM/TSV files regardless of their extension.


## Structure

A SSSOM/TSV file contains one, and only one, mapping set object. It is made of two different parts:

* the _metadata block_, which contains essentially all the slots of the [`MappingSet` class](MappingSet.md) except the `mappings` slot;
* the _mappings block_ (also called the _TSV section_), which contains the individual mappings.

A SSSOM/TSV file MUST NOT contain anything other than those two blocks.


### Metadata block

The metadata block is written as the [YAML 1.2](https://yaml.org/spec/1.2.2/) serialisation of the `MappingSet` object, except that the `mappings` slot is _not_ included (since it contains the mappings, that are serialised in the mappings block instead).

The metadata block MUST appear at the beginning of the file. Every line of the block MUST be preceded by a `#` character; the `#` character MAY be followed by one or several space characters (U+0020) before the YAML content – if so, every line MUST have the same number of space characters.

The metadata block ends with the first line that does not begin with a `#` character, which marks the beginning of the mappings block.

The metadata block SHOULD only contain the slots that do have a value. SSSOM/TSV writers SHOULD skip slots with no value when serialising the mapping set object.

#### Multi-valued slots with a single value

As an exception to the standard YAML rules regarding the serialisation of sequences, a multi-valued slot that happens to contain a single value MAY be serialised as a scalar value rather than as sequence containing only one item.

For example, a `creator_id` slot with the single value `ORCID:1111-2222-3333-4444` MAY be serialised as

```yaml
creator_id: "ORCID:1111-2222-3333-4444"
```

This is, strictly speaking, invalid according the YAML specification; the correct serialisation would be either

```yaml
creator_id: [ "ORCID:1111-2222-3333-4444" ]
```

or

```yaml
creator_id:
  - "ORCID:1111-2222-3333-4444"
```

but the scalar form is frequently found in existing SSSOM/TSV files, so SSSOM/TSV parsers SHOULD accept it. SSSOM/TSV writers SHOULD favour one of the correct YAML serialisations, however.

#### Forbidden YAML features

The following features of the YAML 1.2 specification MUST NOT be used within the metadata block:

* YAML directives ([YAML 1.2 §6.8.1](https://yaml.org/spec/1.2.2/#681-yaml-directives));
* TAG directives ([YAML 1.2 §6.8.2](https://yaml.org/spec/1.2.2/#682-tag-directives));
* Node tags ([YAML 1.2 §6.9.1](https://yaml.org/spec/1.2.2/#691-node-tags));
* Node anchors ([YAML 1.2 §6.9.2](https://yaml.org/spec/1.2.2/#692-node-anchors));
* Alias nodes ([YAML 1.2 §7.1](https://yaml.org/spec/1.2.2/#71-alias-nodes)).

SSSOM/TSV writers MUST NOT generate any of those when writing the metadata block. The expected behaviour of SSSOM/TSV parsers upon encountering them is unspecified.


### Mappings block

The mappings block contains the mappings, serialised as a matrix where each line represents an individual mapping and each column (separated by tab characters, U+0009) represents one of the slots of the [`Mapping` class](Mapping.md).

The mappings block MUST follow immediately the metadata block within a SSSOM/TSV file. It starts with a header line containing the column names, which are the names of the slots in the `Mapping` class.

There SHOULD be no empty columns. If none of the mappings in a set has a value for a given slot, that slot SHOULD be skipped when writing the header line and the individual mappings.

Multi-valued slots MUST be serialised as a list of values separated by `|` characters.

#### Quoting

Within the mappings block, the following quoting rules, adapted from [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180), apply:

1. Any value MAY be enclosed in double quotes (`"`).
2. Values containing line breaks, double quotes, or tabs (U+0009) MUST be enclosed in double quotes.
3. When a value is enclosed in double quotes, a double quote appearing within the value MUST be escaped by preceding it with another double quote.

SSSOM/TSV parsers MUST strip any enclosing double quotes and escaping double quotes before passing the parsed objects to the application code.


## External metadata mode

The metadata block MAY be stored in a separate file from the TSV section, instead of preceding it in the same file as described above. This is called the _external metadata mode_ (by contrast, when the two blocks are in the same file, this is called the _embedded metadata mode_).

In external mode, the metadata block follows the same rules as described in the [Metadata block](#metadata-block) section above, except that lines MUST NOT start with a `#` character.

It is RECOMMENDED that the file containing the metadata block has the same basename as the file containing the TSV section, with a `.sssom.yml` extension.

When an external metadata file is used, the file containing the TSV section MUST NOT contain anything else than the TSV section. That is, the first line of that file MUST be the header line containing the column names.

Implementations SHOULD support reading SSSOM/TSV files in external metadata mode; they MAY support writing SSSOM/TSV files in that mode.


## Encoding

SSSOM/TSV files MUST be encoded in UTF-8 ([RFC 3629](https://datatracker.ietf.org/doc/html/rfc3629#section-13)). They MUST NOT start with a byte order mark (U+FEFF). This applies to external metadata files as well, when the [external metadata mode](#external-metadata-mode) is used.


## Identifiers

All identifiers in a SSSOM/TSV file, that is, all the values of slots typed as [EntityReference](EntityReference.md), MUST be serialised in [CURIE syntax](https://www.w3.org/TR/curie/). SSSOM/TSV parsers SHOULD reject files containing identifiers serialised as IRIs.

To allow unambiguous resolution of all CURIEs present in a SSSOM/TSV file, the metadata block MUST contain an additional `curie_map` field, which is a map of prefix names to IRI prefixes. The `curie_map` field SHOULD appear at the beginning of the metadata block.

Any prefix name used in a SSSOM/TSV file MUST be declared with a corresponding entry in the CURIE map. SSSOM/TSV parsers MUST reject a file with undeclared prefix names.

Prefix names listed in the table found in the [IRI prefixes](spec-intro.md#iri-prefixes) section are considered “built-in”. As such, they MAY be omitted from the CURIE map. If they are not omitted, they MUST point to the same IRI prefixes as in the aforementioned table.


## Propagatable slots

As [explained in another section](spec-model.md#propagation-of-mapping-set-slots), some slots in the `MappingSet` class are intended, not to describe the mapping set itself, but to store values that are shared by all mappings in the set. These slots are called the “propagatable slots”, because their values should be “propagated” from the mapping set down to the individual mappings.

### Propagation

“Propagation” is the operation of assigning to individual mappings in a set the values from the propagatable slots of the set. That operation SHOULD be performed by a SSSOM/TSV parser before passing the parsed objects to the application code.

For any given propagatable slot, propagation is only allowed if none of the individual mappings already have their own value in that slot. If any mapping (even only one mapping) has a value in that slot, then the slot MUST be considered as non-propagatable. Otherwise, a propagating SSSOM/TSV parser MUST (1) copy over the value of the propagatable slot on the `MappingSet` object to the corresponding slot of every individual `Mapping` objects, and (2) remove the propagated value from the `MappingSet` object.

Implementations that support propagation MUST also support condensation.

### Condensation

“Condensation” is the opposite of “propagation”. It is the operation of assigning common values to the propagatable slots of the set, based on the values of these slots on individual mappings. That operation SHOULD be performed by a SSSOM/TSV writer prior to writing a set into a SSSOM/TSV file, but that behaviour, if available, MUST be deactivatable.

For any given propagatable slot, condensation is only allowed if (1) all mappings in the set have the same value, and (2) the mapping set does not already have a value in the slot, unless that value happens to be the same as the value in all mappings. If those two conditions are met, then a condensating SSSOM/TSV writer MUST (1) set the value of the slot on the `MappingSet` object to the common value of the slot in all mappings, and (2) remove the condensed value from the individual `Mapping` object.

Implementations that support condensation MUST also support propagation.


## Compatibility with previous versions of the specification

Implementations MUST support the current version of the specification. However, SSSOM/TSV parsers MAY additionally accept to parse files that were compliant to a previous version. This section provides advice for implementations willing to support older versions.

### Compatibility with pre-1.0 versions

#### `match_type` slot

Initial versions of this specification defined a `match_type` slot on the `Mapping` class. The slot was intended to describe the kind of match that led to the mapping, and accepted values from a specific enumeration. In SSSOM 0.9.1, this slot was replaced by the `mapping_justification` slot, and the enumeration was replaced by terms from the [SEMAPV vocabulary](https://mapping-commons.github.io/semantic-mapping-vocabulary/).

Upon encountering a `match_type` slot, implementations supporting pre-1.0 versions MUST silently transform it into a `mapping_justification` slot and convert the enumeration values using the following table:

| `match_type` value | `mapping_justification` value |
| ------------------ | ----------------------------- |
| Lexical            | semapv:LexicalMatching        |
| Logical            | semapv:LogicalMatching        |
| HumanCurated       | semapv:ManualMappingCuration  |
| Complex            | semapv:CompositeMatching      |
| Unspecified        | semapv:UnspecifiedMatching    |
| SemanticSimilarity | semapv:SemanticSimilarityThresholdMatching |

Any other value in the `match_type` slot MUST be treated as an error.

If the set contains both `match_type` and `mapping_justification` slots, it is advised to simply ignore the former.


#### `match_term_type` slot

Initial versions of this specification defined a `match_term_type` slot on the `Mapping` class. The slot was intended to describe what was being matched. In SSSOM 0.9.1, this slot was replaced by two distinct slots called `subject_type` and `object_type` (this notably allowed for the case where the subject and the object are of a different type, something the `match_term_type` slot did not support).

Upon encountering a `match_term_type` slot, implementations supporting pre-1.0 versions MUST silently transform it into a pair of `subject_type` and `object_type` slots, both slots having the same value derived from the original value using the following table:

| `match_term_type` value | `subject_type` and `object_type` value |
| ----------------------- | -------------------------------------- |
| ConceptMatch            | skos concept                           |
| ClassMatch              | owl class                              |
| ObjectPropertyMatch     | owl object property                    |
| IndividualMatch         | owl named individual                   |
| DataPropertyMatch       | owl data property                      |
| TermMatch               | rdfs literal                           |

Any other value in the `match_term_type` slot MUST be treated as an error.

If the set already contains `subject_type` and `object_type` slots, any `match_term_type` slot can be silently ignored.


## Canonical SSSOM/TSV format

This section defines a “canonical” variant of the SSSOM/TSV format, which has stricter serialisation rules. The purpose of the canonical SSSOM/TSV format is to minimise differences across SSSOM/TSV files that would be induced by small diverging behaviours between different SSSOM/TSV implementations.

The rules in this section apply to SSSOM/TSV writers only. SSSOM/TSV writers SHOULD write files in the canonical format, but SSSOM/TSV readers MUST NOT reject a file solely because it does not follow the canonical rules.

### General rules

A canonical SSSOM/TSV writer:

* MUST use line breaks made of only the U+000A character (no U+000D, and no U+000D + U+000A sequences);
* MUST condense the slots whenever possible, as described in the [Condensation](#condensation) section.


### Rules for the metadata block

When writing the metadata block, a canonical SSSOM/TSV writer:

* MUST embed the metadata block in the same file as the TSV section (no external metadata);
* MUST NOT insert additional space characters between the initial `#` character and the YAML content;
* MUST serialise multi-valued slots as YAML “block sequences” ([YAML Specification §8.2.1](https://yaml.org/spec/1.2.2/#821-block-sequences)) – even when the list of values contains only one item;
* MUST serialise scalar values in YAML “plain style” ([YAML Specification §7.3.3](https://yaml.org/spec/1.2.2/#733-plain-style)) whenever possible, otherwise in “double-quoted style” ([YAML Specification §7.3.1](https://yaml.org/spec/1.2.2/#731-double-quoted-style));
* MUST serialise the slots in the order they appear in the [“Slots” table](MappingSet.md#slots), in the documentation for the `MappingSet` class;
* MUST write the `curie_map` at the beginning of the block, before any other slots;
* MUST NOT include in the CURIE map the prefix names that are considered “built-in”;
* MUST NOT include in the CURIE map any prefix name that is not used anywhere in the set;
* MUST sort the prefix names in the CURIE map in lexicographical order.


### Rules for the mappings block

When writing the mappings block, a canonical SSSOM/TSV writer:

* MUST quote values only when needed, as per the rules in the [Quoting](#quoting) section;
* MUST serialise floating point values with up to three digits as needed after the decimal point, rounding the last digit to the nearest neighbour (rounding up if both neighbours are equidistant);
* MUST write the columns in the order the slots appear in the [“Slots” table](Mapping.md#slots), in the documentation for the `Mapping` class;
* MUST sort the mappings in lexicographical order on all their slots, in the order the slots appear in the [“Slots” table](Mapping.md#slots).


## Examples

This section is _non-normative_.

A SSSOM/TSV file in embedded metadata mode:

```
#curie_map:
#  FOODON: http://purl.obolibrary.org/obo/FOODON_
#  KF_FOOD: https://kewl-foodie.inc/food/
#  orcid: https://orcid.org/
#mapping_set_id: https://w3id.org/sssom/tutorial/example1.sssom.tsv
#mapping_set_description: Manually curated alignment of KEWL FOODIE INC internal food and nutrition database with Food Ontology (FOODON). Intended to be used for ontological analysis and grouping of KEWL FOODIE INC related data.
#license: https://creativecommons.org/licenses/by/4.0/
#mapping_date: 2022-05-02
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification	author_id	confidence	comment
KF_FOOD:F001	apple	skos:exactMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	0.95	"We could map to FOODON:03310788 instead to cover sliced apples, but only ""whole"" apple types exist."
KF_FOOD:F002	gala	skos:exactMatch	FOODON:00003348	Gala apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	1	
KF_FOOD:F003	pink	skos:exactMatch	FOODON:00004186	Pink apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	0.9	"We could map to FOODON:00004187 instead which more specifically refers to ""raw"" Pink apples. Decided against to be consistent with other mapping choices."
KF_FOOD:F004	braeburn	skos:broadMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	1	
```

The same set in external metadata mode: first the file containing the metadata block:

```yaml
curie_map:
  FOODON: http://purl.obolibrary.org/obo/FOODON_
  KF_FOOD: https://kewl-foodie.inc/food/
  orcid: https://orcid.org/
mapping_set_id: https://w3id.org/sssom/tutorial/example1.sssom.tsv
mapping_set_description: Manually curated alignment of KEWL FOODIE INC internal food and nutrition database with Food Ontology (FOODON). Intended to be used for ontological analysis and grouping of KEWL FOODIE INC related data.
license: https://creativecommons.org/licenses/by/4.0/
mapping_date: 2022-05-02
```

then the file containing the mappings block:

```
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification	author_id	confidence	comment
KF_FOOD:F001	apple	skos:exactMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	0.95	"We could map to FOODON:03310788 instead to cover sliced apples, but only ""whole"" apple types exist."
KF_FOOD:F002	gala	skos:exactMatch	FOODON:00003348	Gala apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	1	
KF_FOOD:F003	pink	skos:exactMatch	FOODON:00004186	Pink apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	0.9	"We could map to FOODON:00004187 instead which more specifically refers to ""raw"" Pink apples. Decided against to be consistent with other mapping choices."
KF_FOOD:F004	braeburn	skos:broadMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	1	
```

### Invalid examples

Illegal case 1: the metadata block cannot contains comments that are not part of the metadata.

```
# This is a comment that does not belong here.
#curie_map:
#  HP: "http://purl.obolibrary.org/obo/HP_"
#  MP: "http://purl.obolibrary.org/obo/MP_"
#  orcid: "https://orcid.org/"
# This is another comment that also does not belong here.
#creator_id:
#  - "orcid:0000-0002-7356-1779"
```

Illegal case 2: there should be no empty lines.

```
#curie_map:
#  HP: "http://purl.obolibrary.org/obo/HP_"
#  MP: "http://purl.obolibrary.org/obo/MP_"
#  orcid: "https://orcid.org/"

#creator_id:
#  - "orcid:0000-0002-7356-1779"
```
