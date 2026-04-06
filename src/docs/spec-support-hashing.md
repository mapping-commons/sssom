# Hashing a SSSOM mapping record

SSSOM implementations SHOULD provide a function to compute a hash on a
SSSOM mapping record. That function is hereafter called “the SSSOM
hashing function” and defined below.

## Rationale and purpose
The SSSOM hashing function defined here is intended to allow mapping
records to be quickly compared and, in particular, to quickly determine
whether two records are identical.

The function is intended for **interoperability** between SSSOM
implementations. Its point is to ensure that one can always compute the
same hash for the same mapping record regardless of which SSSOM
implementation is used.

When an implementation needs to assert whether two records are identical
**for its own internal purposes** (for example, to store records into a
hash table), it may use whatever method is best suited without regard
for the SSSOM hashing function.

## Hashing procedure

The general principle of the SSSOM hashing function is to compute a
ZBase32-encoded SHA2-256 hash of a canonical S-expression representing
the mapping record.

### Step 0: Propagate all condensed slots
If the mapping set the mapping record to hash belongs to contains
condensed slots, they MUST be propagated to the mapping record [as per
the standard rules](spec-model.md#propagation).

### Step 1: Turn the mapping record into a canonical S-expression
This step creates a representation of the mapping record into a
canonical S-expression as per [RFC 9804](https://www.rfc-editor.org/rfc/rfc9804#name-canonical-representation).

The S-expression MUST be assembled as follows:

1. Start with `(7:mapping(`,
2. Iterate over all slots of the `Mapping` class, in the order in which
they are [listed](../Mapping/#slots) in the LinkML model. Exclude the
`record_id` slot and the `mapping_cardinality` slot. For all other
slots:
    1. If the slot has no value for the mapping record to hash, skip to
    next slot.
    2. Append to the S-expression `(N:SLOTNAME`, where _SLOTNAME_ is the
    LinkML name for the slot and _N_ is the length of the slot name (so,
    for rxample, `(10:subject_id`, `(9:author_id`, `(10:confidence`,
    etc.).
    3. If the slot is defined as a multi-valued slot (and even if it has
    only one value in the mapping record to hash):
        1. Append `(`.
        2. Sort the list of values in lexicographical order and iterate
        over the sorted values. For each value _V_, append `N:V`, where
        _N_ is the length of _V_.
        c. Append `)`.
    4. If the slot is typed as a floating point number (e.g.
    `confidence`), convert the value to a string _V_ by truncating the
    floating point number to up to 3 digits after the decimal point,
    rounding the last digit to the nearest neighbour (rounding up if
    both neighbours are equidistant). Then append `N:V`, where _N_ is
    the length of _V_.
    5. If the slot is typed as an enumeration (e.g. `subject_type`),
    append `N:ENUMVALUE`, where _ENUMVALUE_ is the allowed value in the
    enumeration as specified in the LinkML model, and _N_ is the length
    of _ENUMVALUE_ (e.g. `9:owl class` for a possible value for the
    `subject_type` slot).
    6. If the slot is typed as a date, append `10:YYYY-MM-DD`, where
    _YYYY-MM-DD_ is the representation of the value in ISO-8601 format.
    7. If the slot is typed as an entity reference, ensure the value is
    expanded according to the mapping set’s prefix map and append `N:V`,
    where _V_ is the expanded reference and _N_ is the length of the
    expanded reference.
    8. If the slot is of any other type, append `N:V`, where _V_ is the
    string value of the slot and _N_ is the length of the string value.
    9. Append `)`.
3. If the implementation support [extension slots](spec-model.md#non-standard-slots)
and the mapping record does have such slots:
    1. Append `(10:extensions(`.
    2. Sort extension values by their properties in lexicographical
    order.
    3. For each extension value:
        1. Append `(N:PROP`, where _PROP_ is the property identifying
        the extension and _N_ is the length of the property.
        2. Append `N:V`, where _V_ is the extension value proper and _N_
        its length.
    4. Append `))`.
4. Append `))`.

### Step 2: Compute the SHA2-256 hash of the S-expression
Encore the S-expression assembled in step 1 into UTF-8 (if it was not
already assembled directly in UTF-8). Then hash the array of bytes
containing the UTF-8 representation of the S-expression using the
standard SHA2-256 hash function as defined in
[NIST FIPS-180-4](https://doi.org/10.6028/NIST.FIPS.180-4).

### Step 3: Encode the hash into a ZBase32 string
Encode the hash computed in step 2 into its representation in the
ZBase32 encoding ([RFC 6189](https://tools.ietf.org/html/rfc6189#section-5.1.6)).

## Example

> This section is not normative. It provides a step-by-step example of
how to apply the above procedure.

Given the following mapping set in SSSOM/TSV format:

```
#curie_map:
#  FBbt: http://purl.obolibrary.org/obo/FBbt_
#  UBERON: http://purl.obolibrary.org/obo/UBERON_
#  orcid: https://orcid.org/
#  semapv: https://w3id.org/semapv/vocab/
#  skos: http://www.w3.org/2004/02/skos/core#
subject_id	predicate_id	object_id	mapping_justification	creator_id
FBbt:00001234	skos:exactMatch	UBERON:0005678	semapv:ManualMappingCuration	orcid:0000-0000-5678-1234|orcid:0000-0000-1234-5678
```

Applying step 1 of the above procedure to the only mapping record of
that set would yield the following canonical S-expression (**whitespaces
added for clarity**, they MUST NOT appear in the actual S-expression):

```
(7:mapping(
           (10:subject_id44:http://purl.obolibrary.org/obo/FBbt_00001234)
           (12:predicate_id46:http://www.w3.org/2004/02/skos/core#exactMatch)
           (9:object_id45:http://purl.obolibrary.org/obo/UBERON_0005678)
           (21:mapping_justification51:https://w3id.org/semapv/vocab/ManualMappingCuration)
           (10:creator_id(
                          37:https://orcid.org/0000-0000-1234-5678
                          37:https://orcid.org/0000-0000-5678-1234
            ))
))
```

Applying the SHA2-256 hash function to the above S-expression would
yield the following hash (in hexadecimal):
`e3bc1b4b586c6e86d0caf369d49c161163e255c4a779821f448a8e4fbd616522`.

Finally, encoding the binary SHA2-256 hash in ZBase32 would yield the
following final value:
`hq6bs14aptzepwgk6pw7j8ysnft6riqrw7har84rtk8r9xmbcwty`.

## Test vectors

> This section is not normative. It provides examples of SSSOM mapping
sets along with the canonical S-expression and the ZBase32-encoded hash
value of the set’s only record.

**Source set:**
```
#curie_map:
#  FOODON: http://purl.obolibrary.org/obo/FOODON_
#  KF_FOOD: https://kewl-foodie.ince/food/
#  semapv: https://w3id.org/semapv/vocab/
#  skos: http://www.w3.org/2004/02/skos/core#
#  wikidata: https://www.wikidata.org/wiki/
#subject_source: KF_FOOD:DB
#object_source: wikidata:Q55118395
#object_source_version: http://purl.obolibrary.org/obo/foodon/releases/2022-02-01/foodon.owl
subject_id	predicate_id	object_id	mapping_justification	confidence	mapping_date
KF_FOOD:F001	skos:exactMatch	FOODON:00002473	semapv:ManualMappingCuration	0.95	2022-05-02
```

S-expression:
```
(7:mapping((10:subject_id34:https://kewl-foodie.ince/food/F001)(12:predicate_id46:http://www.w3.org/2004/02/skos/core#exactMatch)(9:object_id46:http://purl.obolibrary.org/obo/FOODON_00002473)(21:mapping_justification51:https://w3id.org/semapv/vocab/ManualMappingCuration)(14:subject_source32:https://kewl-foodie.ince/food/DB)(13:object_source39:https://www.wikidata.org/wiki/Q55118395)(21:object_source_version68:http://purl.obolibrary.org/obo/foodon/releases/2022-02-01/foodon.owl)(12:mapping_date10:2022-05-02)(10:confidence4:0.95)))
```
Hash value:
```
cdxs1je5rcwpiqnarmojsqmxmpfe9tj43sbahp8u6txk5rssoduo
```

**Source set:**
```
#curie_map:
#  FBbt: http://purl.obolibrary.org/obo/FBbt_
#  UBERON: http://purl.obolibrary.org/obo/UBERON_
#  semapv: https://w3id.org/semapv/vocab/
#  skos: http://www.w3.org/2004/02/skos/core#
#  example: https://example.org/sets/record-id#
record_id	subject_id	predicate_id	object_id	mapping_justification
example:0000001	FBbt:0009124	skos:exactMatch	UBERON:0000003	semapv:LexicalMatching
```

S-expression:
```
(7:mapping((10:subject_id43:http://purl.obolibrary.org/obo/FBbt_0009124)(12:predicate_id46:http://www.w3.org/2004/02/skos/core#exactMatch)(9:object_id45:http://purl.obolibrary.org/obo/UBERON_0000003)(21:mapping_justification45:https://w3id.org/semapv/vocab/LexicalMatching)))
```
Hash value:
```
qn1bra45hjtazt664husfgah5ewzo3oamh4swj5gomuka88rrqgo
```

**Source set:**
```
#curie_map:
#  HP: http://purl.obolibrary.org/obo/HP_
#  MP: http://purl.obolibrary.org/obo/MP_
#  semapv: https://w3id.org/semapv/vocab/
#  skos: http://www.w3.org/2004/02/skos/core#
#mapping_provider: https://w3id.org/sssom/core_team
subject_id	predicate_id	object_id	mapping_justification	similarity_score
HP:0009124	skos:exactMatch	MP:0000003	semapv:LexicalSimilarityThresholdMatching	0.8
```

S-expression:
```
(7:mapping((10:subject_id41:http://purl.obolibrary.org/obo/HP_0009124)(12:predicate_id46:http://www.w3.org/2004/02/skos/core#exactMatch)(9:object_id41:http://purl.obolibrary.org/obo/MP_0000003)(21:mapping_justification64:https://w3id.org/semapv/vocab/LexicalSimilarityThresholdMatching)(16:mapping_provider32:https://w3id.org/sssom/core_team)(16:similarity_score3:0.8)))
```
Hash value:
```
bsat1g1mxe564n5rtoy5usdifybheqxgpes53rtbrue5uu3ac19o
```

**Source set:**
```
#curie_map:
#  COMENT: https://example.com/entities/
#  EXPROP: https://example.org/properties/
#  ORGENT: https://example.org/entities/
#  semapv: https://w3id.org/semapv/vocab/
#  skos: http://www.w3.org/2004/02/skos/core#
#extension_definitions:
#  - slot_name: ext_bar
#    property: EXPROP:barProperty
#    type_hint: xsd:integer
#  - slot_name: ext_baz
#    property: EXPROP:bazProperty
#    type_hint: linkml:Uriorcurie
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification	ext_bar	ext_baz
ORGENT:0001	alice	skos:closeMatch	COMENT:0011	alpha	semapv:ManualMappingCuration	111	ORGENT:BAZ_0001
```

S-expression:
```
(7:mapping((10:subject_id33:https://example.org/entities/0001)(13:subject_label5:alice)(12:predicate_id46:http://www.w3.org/2004/02/skos/core#closeMatch)(9:object_id33:https://example.com/entities/0011)(12:object_label5:alpha)(21:mapping_justification51:https://w3id.org/semapv/vocab/ManualMappingCuration)(10:extensions((42:https://example.org/properties/barProperty3:111)(42:https://example.org/properties/bazProperty37:https://example.org/entities/BAZ_0001)))))
```
Hash value:
```
o5tsbozxxc6i66nezy7rm679waam1f9mxbemqpbyeyiz4q53sqjo
```
