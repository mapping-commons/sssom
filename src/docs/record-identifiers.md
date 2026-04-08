# Identifying mapping records

Since version 1.1, the SSSOM specification allows to explicitly assign an
identifier to every single mapping record within a given mapping set, through
the [record_id](../record-id.md) slot.

The specification is deliberately non-prescriptive about what record identifiers
should look like or how they should be generated. The only constraints on the
`record_id` slot are that:

- the value must be a URI;
- the URI must be representable in CURIE form in some serialisations (e.g. in
  SSSOM/TSV);
- either all records within a set have an identifier, or none have one;
- each identifier should be unique within the set that contains it.

Beyond those constraints, it is left to the creators of a SSSOM mapping set to
decide whether and how to mint identifiers for their records. This page is
intended to provide some non-normative guidance.

## Uniqueness scope

While the specification only mandates that record identifiers must be unique
**within a set**, it is probably a good idea to use identifiers that are
**globally** unique.

An easy way to do that is to construct the identifiers on top of the
`mapping_set_id` of the mapping set.

For example, if you have the following set:

```
#curie_map:
#  FOODON: http://purl.obolibrary.org/obo/FOODON_
#  KF_FOOD: https://kewl-foodie.inc/food/
#license: https://creativecommons.org/licenses/by/4.0/
#mapping_set_id: https://w3id.org/sssom/tutorial/example1
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification
KF_FOOD:F001	apple	skos:exactMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration
KF_FOOD:F002	gala	skos:exactMatch	FOODON:00003348	Gala apple (whole)	semapv:ManualMappingCuration
KF_FOOD:F003	pink	skos:exactMatch	FOODON:00004187	Pink apple (whole, raw)	semapv:ManualMappingCuration
KF_FOOD:F004	braeburn	skos:broadMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration
```

then you could construct the following identifiers, all derived by appending a
local part to the `mapping_set_id` URI:

- `https://w3id.org/sssom/tutorial/example1#001`
- `https://w3id.org/sssom/tutorial/example1#002`
- `https://w3id.org/sssom/tutorial/example1#003`
- `https://w3id.org/sssom/tutorial/example1#004`

Assuming the `mapping_set_id` URI is globally unique (which it should be), then
all record identifiers derived from it will necessarily be globally unique as
well.

The resulting set would then look as follows (keep in mind that record
identifiers must be in CURIE form in the SSSOM/TSV format):

```
#curie_map:
#  FOODON: http://purl.obolibrary.org/obo/FOODON_
#  KF_FOOD: https://kewl-foodie.inc/food/
#  example1: https://w3id.org/sssom/tutorial/example1#
#license: https://creativecommons.org/licenses/by/4.0/
#mapping_set_id: https://w3id.org/sssom/tutorial/example1
record_id   subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification
example1:001    KF_FOOD:F001	apple	skos:exactMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration
example1:002    KF_FOOD:F002	gala	skos:exactMatch	FOODON:00003348	Gala apple (whole)	semapv:ManualMappingCuration
example1:003    KF_FOOD:F003	pink	skos:exactMatch	FOODON:00004187	Pink apple (whole, raw)	semapv:ManualMappingCuration
example1:004    KF_FOOD:F004	braeburn	skos:broadMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration
```

> Again, this is **guidance** only. There is _no obligation_ for record
> identifiers to be derived from the `mapping_set_id`. It is simply a convenient
> way to achieve global uniqueness, should it be desired.

## Identifier generation methods

Here are some of the ways by which the local part of identifiers can be
generated.

### Opaque identifiers

#### Serially allocated numbers

This is the method used in the example above. The local part of the identifier
is a (typically fixed-width) number that is simply incremented whenever a new
identifier is needed.

This is arguably the simplest method, and one that is especially practical when
creating/editing a mapping set using a generic, non-SSSOM-aware spreadsheet
software. It requires keeping track of the last used number, but that should not
be a big hurdle when editing a set in a spreadsheet software.

#### Randomly allocated numbers

The local part of the identifier can be made of numbers that are randomly picked
rather than serially allocated. This dispenses of the need to keep track of the
last used number.

For this method to work, the random numbers must be picked (1) within a large
enough space and (2) using an established and solidly implemented pseudo-random
number generator (PRNG) software. In particular, they should _not_ be
hand-picked by a human editor (or a LLM). Humans (and the LLMs that try to mimic
them) are notoriously bad at producing random numbers.

Of note, this method can easily produce **globally unique** identifiers on its
own if the space in which the random numbers are picked is large enough.
Typically, using 128-bit numbers (and assuming a proper PRNG), the probability
of two random identifiers colliding is sufficiently low that for all purposes
the identifiers can be considered globally unique.

### Non-opaque identifiers

#### Manually crafted non-opaque strings

A human editor could mint an identifier that meaningfully represents some “key”
characteristics of the mapping record. For example, the first record in the
example mapping set above:

```
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification
KF_FOOD:F001	apple	skos:exactMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration
```

(not repeating the mapping set metadata _brevitatis causa_) could get assigned
an identifier like `example1:F001_exact_FOODON2473` – constructed by some
informal derivation of the subject ID (`F001`), the predicate ID (`exact`), and
the object ID (`FOODON2473`).

This might be perceived as useful to a human curator, as the record identifier
immediately gives a sense of what the record is about. It must be noted,
however, that embedding any kind of meaning into an identifier is generally a
bad idea
([McMurry _et al_., 2017](https://doi.org/10.1371/journal.pbio.2001414)).

#### Content-derived identifiers

An identifier can be automatically derived from the record by running the record
through some kind of condensation (“hash”) function that returns a value
calculcated in such a way that the probability that two different records could
yield the same value can be considered negligible.

The SSSOM specification defines [such a function](spec-support-hashing.md).

While the resulting value may appear meaningless, and not different from a
randomly picked number, it represents a non-opaque identifier nonetheless
because the value is still directly dependent on the content of the record.

##### Content-derived identifiers considered harmful

As noted at the very beginning of this page, the SSSOM specification is
non-prescriptive about how identifiers should be minted. It neither mandates nor
forbids any particular method, and all of the methods listed above (as well as
other methods not listed here) _can_ be used in a SSSOM mapping set.

However, the author of those lines strongly feels that content-derived
identifiers are a particularly bad idea, for the reasons given in this section.

**(A)** Content-derived identifiers make it impossible to write a mapping set
entirely by hand. The hash of a mapping record cannot be realistically computed
in someone’s head, whoever is editing the mapping will have to use a dedicated
tool to produce it. This breaks an important promise of SSSOM, which is that one
can always manually craft a SSSOM set with no specialised tooling at all – just
a plain old spreadsheet software.

**(B)** Content-derived identifiers are at risk of becoming “out-of-sync” with
the records they supposedly identify. If an editor modifies the record in any
way but forgets to re-run the ID-generating procedure, then they’ll end up with
identifiers that are no longer really derived from the content of the record.

**(C)** Content-derived identifiers deprive the set’s creators of the freedom to
decide the difference between “updating an existing record” and “creating a new
record”, because in fact there is no such thing as “updating a record” when
using content-derived identifiers – any change to a record would cause the
identifier to change, in effect always creating a _new_ independent record.

**(D)** As a direct consequence of **C**, content-derived identifiers are not
_stable_, because again any change to the record (even a semantically
meaningless change like fixing a typo) would cause the identifier to change.
This is turn means, for example, that consumers of records with content-derived
identifiers cannot _reliably_ refer to them, because the identifiers may change
at any time for even the slightest change made to the records.

**(E)** The instability of content-derived identifiers is even worse in the
specific case of SSSOM, because the content of a SSSOM record could change
because of something that is out of the control of the record’s creator.

Consider the following record:

```
subject_id  subject_label   predicate_id    object_id   object_label
FBbt:00000015   thorax  semapv:crossSpeciesExactMatch   UBERON:6000015  insect thorax
```

and now let’s imagine that Uberon curators decide to rename UBERON:6000015 from
“insect thorax” to “thorax sensu Insecta” (because they decided they prefer this
way of mentioning the species within the label). The next time the mapping is
updated to ensure it is using the latest labels, the record thus becomes:

```
subject_id  subject_label   predicate_id    object_id   object_label
FBbt:00000015   thorax  semapv:crossSpeciesExactMatch   UBERON:6000015  thorax sensu Insecta
```

In this scenario, the _meaning_ of the record has not changed at all.
UBERON:6000015 still represents the same concept as before, so this record still
represents the very same mapping between the very same entities. And yet,
because the _label_ of UBERON:6000015 has changed (something that the creator of
the set has no control upon), if records were identified using content-derived
identifiers we would have to consider the second record as a _different entity_,
identified with a different identifier, than the first.

Overall, content-derived identifiers can only be viable if some very specific
conditions are met:

- the data store (be it a database, a file, or whatever) where records are
  stored must be **append-only**; that is, it must not be possible to delete or
  modify existing records, you can only _add_ new records;
- whenever a new record is created by deriving from an existing record, there
  must be a way to get to the original record from the new record.

_If_ you use SSSOM that way, then _maybe_ content-derived identifiers can be
fine for your use case. Otherwise, you should stick to meaningless, opaque
identifiers that are not tied to the content of the record.
