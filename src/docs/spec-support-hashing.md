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

Given the following mapping record (in JSON format):

```json
{"subject_id": "http://purl.obolibrary.org/obo/FBbt_00001234",
 "predicate_id": "http://www.w3.org/2004/02/skos/core#exactMatch",
 "object_id": "http://purl.obolibrary.org/obo/UBERON_0005678",
 "mapping_justification": "https://w3id.org/semapv/vocab/ManualMappingCuration",
 "creator_id": [
    "https://orcid.org/0000-0000-5678-1234",
    "https://orcid.org/0000-0000-1234-5678"
 ]}
```

Applying step 1 of the above procedure would yield the following
canonical S-expression (**whitespaces added for clarity**, they MUST NOT
appear in the actual S-expression):

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
records along with the corresponding hash value.

```json
{"subject_id": "https://kewl-foodie.inc/food/F001",
 "subject_label": "apple",
 "predicate_id": "http://www.w3.org/2004/02/skos/core#exactMatch",
 "object_id": "http://purl.obolibrary.org/obo/FOODON_00002473",
 "object_label": "apple (whole)",
 "mapping_justification": "https://w3id.org/semapv/vocab/ManualMappingCuration",
 "author_id": [
   "https://orcid.org/0000-0002-7356-1779"
 ],
 "subject_source": "https://kewl-foodie.inc/food/DB",
 "object_source": "https://www.wikidata.org/wiki/Q55118395",
 "object_source_version": "http://purl.obolibrary.org/obo/foodon/releases/2022-02-01/foodon.owl",
 "mapping_date": "2022-05-02",
 "confidence": 0.95
}
```

Hash value: `x4m9kcj8yjrrxh8ozwt83bkxcequb3fjqsamu9yyejyqft1gowao`

```json
{"record_id": "https://example.org/sets/record-id#0000001",
 "subject_id": "http://purl.obolibrary.org/obo/FBbt_0009124",
 "predicate_id": "http://www.w3.org/2004/02/skos/core#exactMatch",
 "object_id": "http://purl.obolibrary.org/obo/UBERON_0000003",
 "mapping_justification": "https://w3id.org/semapv/vocab/LexicalMatching"
}
```

Hash value: `qn1bra45hjtazt664husfgah5ewzo3oamh4swj5gomuka88rrqgo`

```json
{"subject_id": "http://purl.obolibrary.org/obo/HP_0009124",
 "predicate_id": "http://www.w3.org/2004/02/skos/core#exactMatch",
 "object_id": "http://purl.obolibrary.org/obo/MP_0000003",
 "mapping_justification": "https://w3id.org/semapv/vocab/LexicalSimilarityThresholdMatching",
 "mapping_provider": "https://w3id.org/sssom/core_team",
 "similarity_score": 0.8,
 "similarity_measure": "wikidata:Q865360"
}
```

Hash value: `is395b9nwm1rnz3nwkm89nmf563uw48sjspsx7ua8snjqzwz15ty`
