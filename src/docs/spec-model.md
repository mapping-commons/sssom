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

The `MappingSet` class represents, well, a set of individual mappings, which are contained in the `mappings` slot (a list of `Mapping` instances). Other slots in that class are intended either to provide further details about the set itself (sometimes referred to as “mapping set metadata”, with the same caveat as above regarding the data/metadata distinction), or to provide common details for all the mappings in the se (see the [Propagation of mapping set slots](#propagation-of-mapping-set-slots) section further below for details).

Of note, within a set, a mapping may not necessarily be uniquely identified by the combination of its four mandatory slots (`subject_id`, `predicate_id`, `object_id`, and `mapping_justification`). A set may very well contain several mappings with the same subject, predicate, object, and justification, but that differ on some of the other, complementary slots.


## Propagation of mapping set slots

As mentioned briefly above, there are two different types of slots in the `MappingSet` class:

* slots that provide informations about the set itself;
* slots that provide informations about all the mappings in the set.

The latter are called “propagatable slots”. The propagatable slots are:

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

(In a future version of this specification, this information will be formally specified directly within the LinkML schema.)

When a mapping set object has a value in one of its propagatable slots, this MUST be interpreted as if all mappings within the set had that same value in their corresponding slot. For example, if a set has the value _foo_ in its `mapping_tool` slot, all the mappings in that set MUST be treated as if they had the value _foo_ in their `mapping_tool` slot.

This mechanism is intended as a convenience, so that a slot which has the same value for all mappings in a set can be specified only once at the level of the set rather than for each individual mapping.

Slots that are not in the above list (“non-propagatable slots”) describe the mapping set itself, not the mappings it contains, even if the slot also exists on the `Mapping` class. For example, the `creator_id` slot, when used in the `MappingSet` class, is intended to refer to the creators of the set, _not_ the creators of the individual mappings (which may be different, and which are listed in the `creator_id` slot of every mapping).
