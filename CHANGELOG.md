# Changelog for SSSOM

## Next

- Add the concept of "propagatable slots".
- Add the concept of "extension slots".

## SSSOM version 0.15.1

- Add recommendation to sort the keys in the YAML metadata block.
- Double-typed slots explicitly constrained to the [0.0,1.0] range, as per their description.

## SSSOM version 0.15.0

- Add issue_tracker_item and issue_tracker [model elements](https://github.com/mapping-commons/sssom/pull/259).

## SSSOM version 0.13.0

- The necessity of the "canonical column ordering" was downgraded from MUST to SHOULD (https://github.com/mapping-commons/sssom/pull/285)
- Documents clearly that built-in prefixes MUST NOT be redefined (https://github.com/mapping-commons/sssom/pull/285)

## SSSOM version 0.11.0

- see https://github.com/mapping-commons/sssom/releases/tag/0.11.0

### Summary

#### New elements:
- `mapping_set_title` to capture a human readable title for a mapping set
- `registry_title` and `registry_description` to capture the human readable title and description of an SSSOM mapping set registry
- `curation_rule` to capture a (potentially) complex (set of) condition(s) executed by an agent (usually human) that led to the establishment of a mapping. 

#### Updated elements:
- Adding mapping_source slot to Mapping by @matentzn in #230
- Improve documentation for `subject_category` and `object_category` elements

#### Documentation
- Compiled a list of all SSSOM talks: https://mapping-commons.github.io/sssom/presentations/
- Document chaining rules: https://mapping-commons.github.io/sssom/chaining_rules/

#### Quality control and Technical infrastructure

- Make adding a concrete SSSOM example part of the new element request
- Adding QC checks for example SSSOM files hosted in the repo

## SSSOM version 0.10.1

- see https://github.com/mapping-commons/sssom/releases/tag/0.10.1

## SSSOM version 0.9.4

- see https://github.com/mapping-commons/sssom/releases/tag/0.9.4

## SSSOM version 0.9.3

- see https://github.com/mapping-commons/sssom/releases/tag/0.9.3
- Major change: Changed `match_type` logic to `mapping_justification` ([issue](https://github.com/mapping-commons/sssom/issues/150)).


## SSSOM version 0.9.2

- see https://github.com/mapping-commons/sssom/releases/tag/0.9.2

## SSSOM version 0.9.1

- see https://github.com/mapping-commons/sssom/releases/tag/0.9.1

## SSSOM version 0.9.0
- Initial release
- see https://github.com/mapping-commons/sssom/releases/tag/0.9.0
