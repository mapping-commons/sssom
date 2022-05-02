# Tutorials

As a reminder, a SSSOM mapping comprises three major components:

1. The **mapping** itself, that is, a triple `<subject, predicate, object>` that reflects a correspondence of a `subject` entity, for example a class in an ontology, to an `object` entity, for example an identifier in some database, via a semantic mapping `predicate`, such as `skos:exactMatch`.
2. A **mapping justification**, the process or activity that led us to consider the mapping to be correct or reasonable (typical examples: labels match exactly; two classes are logically equivalent; a domain expert determined that two terms reflect the same real world concept).
3. **Provenance metadata**, including information about `author` and `mapping_tool`.

In the following, we will describe how SSSOM mappings are created.

Table of contents:

- [Background](#background)
   - [Ontology alignment](#align)
   - [What are we mapping?](#what)
   - [CURIEs, URIs and databases](#curie)
- [How to create an SSSOM mapping set from scratch](#scratch)

## Background

<a id="align"></a>

### Ontology alignment/matching

Ontology alignment is the process of determining correspondences between ontological concepts. The usage of "alignment", "matching" and "mapping" is fuzzy in practice. From the perspective of SSSOM, alignment usually involves determining _all_ (or a more or less complete set of) correspondences between ontological concepts of two or more source ontologies. The most important resource on the subject is ["Ontology Matching"](https://link.springer.com/book/10.1007/978-3-642-38721-0) by Jérôme Euzenat and Pavel Shvaiko. If you are interested in really diving into the subject, there is no avoiding this book!

This 25 minute course unit by the OpenHPI gives a nice overview over the area, which is relevant to all mapping activities:

<iframe width="560" height="315" src="https://www.youtube.com/embed/VJHKcq_GuxY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Another useful overview is this one by the Knowledge and Data VU Amsterdam. Especially after minute 12, we learn a bit about the differences of OWL and SKOS.

<iframe width="560" height="315" src="https://www.youtube.com/embed/gnq9I0OTjRo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

A 10 minute deep-dive into Jerome Euzenat classification of ontology matching techniques can be seen here:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Jag9hHCZRj8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

A 10 minute overview of Clinical Terminology Mappings by Michael Kahn at CU Anschutz can be seen in the following. This video is highly optional and reveals a very non-semantic webby perspective on the subject. It is focussed on OMOP mappings, one of the many terminology standards in the medical domain.

<iframe width="560" height="315" src="https://www.youtube.com/embed/J3_2WbUAOF4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<a id="what"></a>

### What are we mapping?

In SSSOM we are concerned with mapping _information entities_, i.e. representations of a real world entities. Examples of such entities are:

- Classes, Individuals and Properties in an ontology.
- Entities in Databases, such as a specific person in a "Person" table of a relational database.
- A specific value in the slot of a data model, for example the "UNIVERSITY" constant in the `highest-degree` enumeration for a demographics survey data model.
- A specific code from a code system or terminology such as ICD10CM.

Information entities represent _real world objects_ such as diseases (e.g. Alzheimer's, Diabetes), kinds of vegetables (Asparagus, Broccoli), concrete instances of vegetables (a specific broccoli that was sold in your local supermarket yesterday).

<a id="curie"></a>

### CURIEs, URIs and databases

A mapping involves three information entities: 

1. A subject
1. An object (the entity the subject is mapped to)
1. A semantic "mapping predicate", such as "skos:exactMatch" which defines how the subject entity is mapped to the object entity.

All three _must_ be referred to by an **identifier in CURIE syntax** ([Compact URI](https://www.w3.org/TR/2010/NOTE-curie-20101216/)) when using the SSSOM table format or JSON, or an IRI (Internationalized Resource Identifier) when you are using the RDF representation of SSSOM. This is necessary to ensure that entities are globally unique and mapping sets are fully interoperable across an organisation and beyond. While these concepts are common practice in the Semantic Web world, they may be less well understood in the database world. In fact, they can be quite awkward: 
- Your database my use `p9787869` to identify a specific person in a "Person" table of a relational database.
- Your data model for a demographics survey uses, among others, the `UNIVERSITY` constant in the `highest-degree` enumeration.

To be compliant with SSSOM, such values must be "curified". While this process sounds daunting at first, it is essential: Both the `p9787869` identifier and the `UNIVERSITY` constant may be used in different contexts (different databases or data models) to refer to entirely different entities! While there is no 100% reliable guide for "curification", we usually recommend the following steps:

* Choose a globally unique URI prefix which can unambiguously define the context of your entity. For example (1) `http://embl.org/ebi/person/p9787869` to refer to the person in your `Person` table and (2) `http://embl.org/demographics-survey-datamodel/demographics.highest_education#UNIVERSITY`. In an ideal world, these can be de-referenced (i.e. you can look them up in a web-browser), but the important thing is that they are globally unique (and persistent), so that they cannot be confused with, for example, the `UNIVERSITY` code in another data model.
* We select a reasonable prefix for the code, for example (1) `embl.ebi.person` and (2) `demographics-survey-datamodel.demographics.highest_education`. Note these do not need to be globally unique anymore. Indeed, you could, if you wanted to, use (much) shorter prefixes. (NOTE: some people disagree with this and strive for globally unique prefixes. In the biomedical domain, for example, we try to coordinate prefixes at http://bioregistry.io/. This is not however, necessary when using SSSOM).
* We record the prefixes and their URI prefixes (sometimes called URI expansions) in the `curie_map` of our SSSOM file:

```
curie_map:
  embl.ebi.person: "http://embl.org/ebi/person/"
  demographics-survey-datamodel.demographics.highest_education: "http://embl.org/demographics-survey-datamodel/demographics.highest_education#"
```

* Now we can refer to our entities in the SSSOM mapping table like this: (1) `embl.ebi.person:p9787869` and (2) `demographics-survey-datamodel.demographics.highest_education:UNIVERSITY`.

This may strike some users as verbose - but the concept of unique identifiers for all information entities is _at the heart of SSSOM_. There is an initial cost to carefully defining namespaces for the various vocabularies and contexts (data model enums, value sets), but the ability to unambiguously refer to an entity will pay of as the organisation grows and data needs to be integrated from a wide variety of sources. See [here](https://hl7.org/fhir/conceptmap-example.ttl.html) for an example how FHIR deals with this: Rather than using a lot of prefixes, FHIR chooses to have one small namespace for `fhir`, and then having the path to the data model element all the way to its value as the local identifier.

<a id="scratch"></a>
## How to create an SSSOM mapping set from scratch

SSSOM mapping sets can be created as part of automated processes, like ontology matchers, or manually by ontology curators. While there is overlap, it makes sense to look at both cases separately. To remind yourself why you should build SSSOM mapping sets in the first place, please refer to [the FAQ](faq.md#why).

### Manually curating mapping sets

To gradually improve terminological mapping practices we are proposing a [5-star system for mappings](spec.md#minimum). For the sake of this tutorial, we will focus on producing a [solid 3-Star mapping set](spec.md#minimum) with the following metadata:

**Core mapping metadata**:

- `subject_id`: The ID of the subject of the mapping
- `predicate_id`: The ID of the predicate of the mapping
- `object_id`: The ID of the object of the mapping

**Mapping justification metadata**:

- `mapping_justification`: the process or activity that led us to believe the mapping to be correct or reasonable.

**Basic provenance metadata**:

- `mapping_date`: The date the mapping was asserted. This is different from the date the mapping was published or compiled in a SSSOM file.
- `author_id`: Identifies the persons or groups responsible for asserting the mappings. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible.
- `mapping_set_description`: A description of the mapping set, providing context and motivation.
- `subject_source`: URI of source the subject.
- `subject_source_version`: The version of the source of the subject.
- `object_source`: URI of source the subject.
- `object_source_version`: The version of the source of the object.
- `confidence`: the level of certainty you have for the mapping to be true (based on the process used to confirm or generate it).

**Some convenience metadata**

- `subject_label`: The human readable label of the subject.
- `object_label`: The human readable label of the object.

#### The tutorial scenario

You are charged with aligning your organisations (KEWL FOODIE INC) internal database about food and nutrition with Food Ontology (FOODON). In your database, you have a table with food items:

| ID | LABEL |
| --- | ---- |
| F001 | apple |
| F002 | gala |
| F003 | pink |
| F004 | braeburn |

As a first pass, you are tasked to map the food items (kinds of apples) in your database to classes in the FOODON ontology.

#### Getting the tools together

To complete this tutorial, we need the following tools:

1. A table editor. In this tutorial we will use [Google Sheets](https://docs.google.com/spreadsheets/u/0/). Manually curating mappings is often done in a collaborative fashion. We like Google Sheets because it allows multiple people to edit the same mapping set at once.
1. OPTIONAL: The [SSSOM toolkit](https://mapping-commons.github.io/sssom-py) installed (requires python 3.9+).

#### Creating a first draft of the mappings

First create a google sheet with the following columns:

| subject_id | subject_label | predicate_id | object_id | object_label | mapping_justification | mapping_date | author_id | subject_source | subject_source_version | object_source | object_source_version | confidence |
|------------|---------------|--------------|-----------|--------------|-----------------------|--------------|-----------|----------------|------------------------|---------------|-----------------------|------------|

As we are mapping database identifiers, our first step is _curiefy our database identifiers_. Read up in detail on why this is done [here](#curie).

We chose to use the following URI prefix for our food database: http://kewl-foodie.com/foods/, with the `KF_FOODS:` prefix (for now, we just document this information in the side, but later, we will add this to our mapping table).

Next, we will add all the entities we hope to align to the mapping table above (we removed some columns here for readability, we will get back to these later):

| subject_id   | subject_label | predicate_id | object_id | object_label | confidence |
|--------------|---------------|--------------|-----------|--------------|-----------------------|
| KF_FOOD:F001 | apple         |              |           |              |                       |
| KF_FOOD:F002 | gala          |              |           |              |                       |
| KF_FOOD:F003 | pink          |              |           |              |                       |
| KF_FOOD:F004 | braeburn      |              |           |              |                       |

While not necessary from a computational perspective, we recommend to document the labels of both the subject and the object to make the mapping table easier to process for human curators.

The next step is now to try and identify suitable terms from FOODON to map to. In the biomedical domain, most curators will [search OLS](https://www.ebi.ac.uk/ols/search?q=apple&groupField=iri&start=0&ontology=foodon) or [Ontobee](https://www.ontobee.org/search?ontology=FOODON&keywords=apple&submit=Search+terms), but some more technically advanced users may choose to use [SPARQL over ontobee](https://api.triplydb.com/s/nq_xvl3JQ) or another endpoint:

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT * WHERE {
  ?sub rdfs:label ?obj .
  FILTER(regex(str(?obj), "apple"))
  FILTER(STRSTARTS(str(?sub),"http://purl.obolibrary.org/obo/FOODON_"))
}
```

##### Mapping "apple", attempt 1

Our first attempt is to try and map `KF_FOOD:F001` (apple). At the time of writing, a search for the string "apple" just across the labels in FOODON reveals more than 300 results. There are no exact matches for the search string "apple", i.e. there is no entity in FOODON that has the label "apple" exactly. Rather than sifting through the large set of results, we move on to try to map a more specific element first. As FOODON is an ontology, having a mapping to a more specific element (e.g. `gala`) may help us to find an appropriate mapping for the more general concept (e.g. `apple`), which should be hierarchically related to the more specific term.

##### Mapping "gala"

Indeed, a [search for "gala"](https://www.ebi.ac.uk/ols/search?q=gala&groupField=iri&start=0&ontology=foodon) reveals one single result: [Gala apple (whole)](https://www.ebi.ac.uk/ols/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_00003348). How do we know if this is a good mapping for our own database entity `gala`? This is a very difficult question, and there is no perfect answer. It is important to remember that mappings should not be judged in terms of "correct" or "wrong", but in terms of "fit for purpose", or, in the case of SSSOM, "fit for most purposes". The following thoughts should cross the curators mind:

- There does not seem to be another FOODON class concerned with "Gala".
- From the description, "A pome fruit of a Gala apple tree cultivar." it seems like we are indeed talking about a kind of apple. ([The picture in the OLS Term information box also helps.](https://www.ebi.ac.uk/ols/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_00003348))
- A quick email to our product team at KEWL FOODIE INC confirms that indeed, our `gala` database entity and FOODON's `Gala apple (whole)` class seem to refer to the same entity. As apples in our database are usually considered "whole", we do not concern ourselves further with the that slightly ambiguous part of the label. (Can I map my apple snack pack which has the "whole" apple cut in slices to `FOODON:00003348`?)

We add the new mapping to our mapping table. Due to our domain expertise and consultation with the product team of our company, we are very confident (1.0 or 100%) that the mapping between `KF_FOOD:F002` and `FOODON:00003348` is exact (for exact matches, we use `skos:exactMatch` as per [SSSOM convention](https://mapping-commons.github.io/sssom/spec/#common-mapping-predicates)).

| subject_id   | subject_label | predicate_id    | object_id       | object_label       | confidence |
|--------------|---------------|-----------------|-----------------|--------------------|------------|
| KF_FOOD:F001 | apple         |                 |                 |                    |            |
| KF_FOOD:F002 | gala          | skos:exactMatch | FOODON:00003348 | Gala apple (whole) |          1 |
| KF_FOOD:F003 | pink          |                 |                 |                    |            |
| KF_FOOD:F004 | braeburn      |                 |                 |                    |            |

##### Mapping "apple", attempt 2

Given our mapping of [Gala apple (whole)](https://www.ebi.ac.uk/ols/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_00003348) we take a better look at the class hierarchy around. We notice three things:

- There is indeed a class called "apple (whole)" which seems to fit our purpose. This also seems to be consistent with our choice of "Gala apple (whole)".
- What is, however, annoying is that there is also a ["apple (whole or parts)"](https://www.ebi.ac.uk/ols/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03310788&viewMode=All&siblings=false) class. KEWL FOODS INC definitely has plans to introduce products involving sliced Gala apples!
- FOODON does not have a concept of a sliced Gala apple.

Again, our judgement as curators is asked here. There is no "correct" or "wrong". To keep things consistent, we decide to map to the "whole" apple, but we take a mental note that this might change in the future. We also take a physical note to _document this design decision_ as a comment.

| subject_id   | subject_label | predicate_id    | object_id       | object_label       | confidence | comment                                                                                             |
|--------------|---------------|-----------------|-----------------|--------------------|------------|-----------------------------------------------------------------------------------------------------|
| KF_FOOD:F001 | apple         | skos:exactMatch | FOODON:00002473 | apple (whole)      |       0.95 | We could map to FOODON:03310788 instead to cover sliced apples, but only "whole" apple types exist. |
| KF_FOOD:F002 | gala          | skos:exactMatch | FOODON:00003348 | Gala apple (whole) |          1 |                                                                                                     |
| KF_FOOD:F003 | pink          |                 |                 |                    |            |                                                                                                     |
| KF_FOOD:F004 | braeburn      |                 |                 |                    |            |                                                                                                     |

##### Mapping "pink"

In the same hierarchy as `apple (whole)`, we find [Pink apple (whole)](https://www.ebi.ac.uk/ols/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_00004186). This is seems like an excellent match, consistent with our previous design decisions. However two observations leave us uncertain:

- The [Pink apple (whole)](https://www.ebi.ac.uk/ols/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_00004186) class has no definition (at the time of writing this tutorial at least) and no pictures, so we cannot be 100% certain that our notion of "pink" is the same as Foodon. A search on Wikipedia reveals different names, like "Pink Pearl" and "Pink Lady", which makes us a bit uncertain.
- In contrast to "Gala apple (whole)", "Pink apple (whole)" has a further subclass, "Pink apple (whole, raw)". What does that mean? All data in our KEWL FOODS INC database pertains to raw apple, so is this now a better match? Raw as opposed to what? Cooked?

Again, there is no great recipe to solve this dilemma. We chose our default recipe:

1. prefer consistent mapping rules over occasionally increased precision (not always a good idea)
2. document design decision

| subject_id   | subject_label | predicate_id    | object_id       | object_label       | confidence | comment                                                                                                                                                   | mapping_justification |
|--------------|---------------|-----------------|-----------------|--------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| KF_FOOD:F001 | apple         | skos:exactMatch | FOODON:00002473 | apple (whole)      |       0.95 | We could map to FOODON:03310788 instead to cover sliced apples, but only "whole" apple types exist.                                                       | sempav:HumanCuration  |
| KF_FOOD:F002 | gala          | skos:exactMatch | FOODON:00003348 | Gala apple (whole) |          1 |                                                                                                                                                           | sempav:HumanCuration  |
| KF_FOOD:F003 | pink          | skos:exactMatch | FOODON:00004186 | Pink apple (whole) |        0.9 | We could map to FOODON:00004187 instead which more specifically refers to "raw" Pink apples. Decided against to be consistent with other mapping choices. | sempav:HumanCuration  |
| KF_FOOD:F004 | braeburn      |                 |                 |                    |            |                                                                                                                                                           | sempav:HumanCuration  |

##### Mapping "braeburn"

We now turn our attention to the last database entity: `KF_FOOD:F004` (braeburn).

Unfortunately, our search for `braeburn`, `brae-burn` yields no results in Foodon. We search Wikipedia and Google for potential synonyms of Braeburn that might have been missed by the FOODON developers, but are unsuccessful. In the end, we give up and decide that there is no matching concept for `KF_FOOD:F004` (braeburn) in FOODON. Now we have to make a choice and how to reflect that in our mapping set:

- We can document directly the fact that there is no `skos:exactMatch` in our SSSOM table.
- We can map `KF_FOOD:F004` (braeburn) to a more general concept, i.e. `apple (whole)`.
- We can do both.

For our data integration efforts, it is generally useful to know if no exact match could be found. Here, again, we have two options:

- we can convey this information by omission. By not including a mapping in the dataset, it does not exist. The downside is that we do not know further down the line if (a) we have looked and there really was no suitable code and (b) we have not looked.
- we can convey this information by using a special code `sssom:NoMapping`. (NOTE as of 2 May 2022, the final decision on how this is represented has not been made. Follow [this discussion](https://github.com/mapping-commons/sssom/issues/28)).

In our case, we have plans to extend our manual mapping efforts with automated ones. We want to use manual non-mapping assertions to filter out false positive mappings with our automated approaches, so we decide to go with the second option and make the non-mapping explicit.

The second question is whether to include a _less precise_ mapping. This depends heavily on the target use case. As a rule of thumb, if the target use case requires precise 1:1 mappings (for example, data transformation use cases often do), we do not include any broad mappings. If our use case is data aggregation, broad matches can still be very useful: At least, we will be able to use the hierarchical structure of FOODON to retrieve all kinds of apples in our FOOD database! We are interested in data aggregation, so we decide to include the mapping.

| subject_id   | subject_label | predicate_id    | object_id       | object_label       | confidence | comment                                                                                                                                                   |
|--------------|---------------|-----------------|-----------------|--------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| KF_FOOD:F001 | apple         | skos:exactMatch | FOODON:00002473 | apple (whole)      |       0.95 | We could map to FOODON:03310788 instead to cover sliced apples, but only "whole" apple types exist.                                                       |
| KF_FOOD:F002 | gala          | skos:exactMatch | FOODON:00003348 | Gala apple (whole) |          1 |                                                                                                                                                           |
| KF_FOOD:F003 | pink          | skos:exactMatch | FOODON:00004186 | Pink apple (whole) |        0.9 | We could map to FOODON:00004187 instead which more specifically refers to "raw" Pink apples. Decided against to be consistent with other mapping choices. |
| KF_FOOD:F004 | braeburn      | skos:exactMatch | sssom:NoMapping |                    |          1 |                                                                                                                                                           |
| KF_FOOD:F004 | braeburn      | skos:broadMatch | FOODON:00002473 | apple (whole)      |          1 |                                                                                                                                                           |

#### Adding rich metadata

| subject_id   | subject_label | predicate_id    | object_id       | object_label       | confidence | comment                                                                                                                                                   | mapping_justification | mapping_date | author_id                 | subject_source | subject_source_version | object_source | object_source_version                                                |
|--------------|---------------|-----------------|-----------------|--------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------|---------------------------|----------------|------------------------|---------------|----------------------------------------------------------------------|
| KF_FOOD:F001 | apple         | skos:exactMatch | FOODON:00002473 | apple (whole)      |       0.95 | We could map to FOODON:03310788 instead to cover sliced apples, but only "whole" apple types exist.                                                       | sempav:HumanCuration  |   2022-05-02 | orcid:0000-0002-7356-1779 | KF_FOOD        |                        | FOODON        | http://purl.obolibrary.org/obo/foodon/releases/2022-02-01/foodon.owl |
| KF_FOOD:F002 | gala          | skos:exactMatch | FOODON:00003348 | Gala apple (whole) |          1 |                                                                                                                                                           | sempav:HumanCuration  |   2022-05-02 | orcid:0000-0002-7356-1779 | KF_FOOD        |                        | FOODON        | http://purl.obolibrary.org/obo/foodon/releases/2022-02-01/foodon.owl |
| KF_FOOD:F003 | pink          | skos:exactMatch | FOODON:00004186 | Pink apple (whole) |        0.9 | We could map to FOODON:00004187 instead which more specifically refers to "raw" Pink apples. Decided against to be consistent with other mapping choices. | sempav:HumanCuration  |   2022-05-02 | orcid:0000-0002-7356-1779 | KF_FOOD        |                        | FOODON        | http://purl.obolibrary.org/obo/foodon/releases/2022-02-01/foodon.owl |
| KF_FOOD:F004 | braeburn      | skos:exactMatch | sssom:NoMapping |                    |          1 |                                                                                                                                                           | sempav:HumanCuration  |   2022-05-02 | orcid:0000-0002-7356-1779 | KF_FOOD        |                        | FOODON        | http://purl.obolibrary.org/obo/foodon/releases/2022-02-01/foodon.owl |
| KF_FOOD:F004 | braeburn      | skos:broadMatch | FOODON:00002473 | apple (whole)      |          1 |                                                                                                                                                           | sempav:HumanCuration  |   2022-05-02 | orcid:0000-0002-7356-1779 | KF_FOOD        |                        | FOODON        | http://purl.obolibrary.org/obo/foodon/releases/2022-02-01/foodon.owl |