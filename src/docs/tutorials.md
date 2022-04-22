# Tutorials

As a reminder, a SSSOM mapping comprises three major components:

1. The **mapping** itself, that is, a triple `<subject, predicate, object>` that reflects a correspondence of a `subject` entity, for example a class in an ontology, to an `object` entity, for example an identifier in some database, via a semantic mapping `predicate`, such as `skos:exactMatch`.
2. A **mapping justification**, the process or activity that led us to consider the mapping to be correct or reasonable (typical examples: labels match exactly; two classes are logically equivalent; a domain expert determined that two terms reflect the same real world concept).
3. **Provenance metadata**, including information about `author` and `mapping_tool`.

In the following, we will describe how SSSOM mappings are created.

Table of contents:

- [How to create an SSSOM mapping set from scratch](#scratch)

<a id="scratch"></a>
## How to create an SSSOM mapping set from scratch

SSSOM mapping sets can be created as part of automated processes, like ontology matchers, or manually by ontology curators. While there is overlap, it makes sense to look at both cases separately. To remind yourself why you should build SSSOM mapping sets in the first place, please refer to [the FAQ](faq.md#why).

### Manually curating mapping sets

To get a good sense of the most important metadata to consider for your project, refer to [SSSOM 5-Star recommendation for mappings](spec.md#minimum)

For the sake of this tutorial, we will focus on producing a solid 3-Star mapping set with the following metadata:

**Core mapping metadata**:

- `subject_id`: The ID of the subject of the mapping
- `predicate_id`: The ID of the predicate of the mapping
- `object_id`: The ID of the object of the mapping

**Mapping justification metadata**:

- `mapping_justification`: the process or activity that led us to consider the mapping to be correct or reasonable

**Basic provenance metadata**:

- `mapping_date`: The date the mapping was asserted. This is different from the date the mapping was published or compiled in a SSSOM file.
- `author_id`: Identifies the persons or groups responsible for asserting the mappings. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible.
- `subject_source`: URI of source the subject.
- `subject_source_version`: The version of the source of the subject.
- `object_source`: URI of source the subject.
- `object_source_version`: The version of the source of the object.
- `confidence`: the level of certainty you have for the mapping to be true.

**Some convenience metadata**

- `subject_label`: The human readable label of the subject.
- `object_label`: The human readable label of the object.

#### The tutorial scenario

You are charged with aligning your organisations internal database about food and nutrition with Food Ontology (FOODON). In your database, you have a table with food items:

| ID | LABEL |
| --- | ---- |
| F:001 | apple |
| F:002 | brae burn |
| F:003 | brae burn |

#### Getting the tools together

To complete this tutorial, we need the following tools:

1. The SSSOM toolkit installed (required python 3.9+).
2. A table editor. In this tutorial we will use [Google Sheets](https://docs.google.com/spreadsheets/u/0/). Manually curating mappings is often done in a collaborative fashion. We like Google Sheets because it allows multiple people to edit the same mapping set at once.

#### Creating a first draft of the mappings

First create a google sheet with the following columns:




