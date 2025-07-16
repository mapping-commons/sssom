# Frequently Asked Questions (FAQ)

<a id="why"></a>
## Why should our mappings be FAIR and carefully standardised?

Mappings are frequently created on an ad-hoc basis, using simple two-column spreadsheets where the first column corresponds to the subject of the mapping, and the second column to the object of the mapping. This is insufficient for a variety of reasons:

- non-transparent precision: While the assumption is that the subject "sort of mostly exactly" maps to the object, in practice this is rarely the case. Matches can `exact`, where the subject corresponds 100% to the object, `broad`, where the object is broader than the subject, and others. Qualifiers like `exact`, `broad`, `narrow`, `related` and `close` qualify the *precision* of the mapping (not to be mistaken for fuzziness of confidence). Without knowing the precision, we cannot accurately transform our data, nor can we use the mappings to "walk", i.e. move from one mapping to another, see [SSSOM 5-Star recommendation for mappings](5star-mappings.md)
- non-transparent incompleteness: We don't know when the mapping was created, on the basis of what version of the terminological source of the subject or object. As time passes, we also lose confidence whether there would now be more suitable mappings, or whether there are new terms that are now fully covered by the mappings.
- non-transparent confidence: whether a tool or a human propose the mapping, there is always a bit of a risk the mapping call may be wrong. As consumers of the mappings we need to know how confident the mapping authors were (confidence score), and why they confident (curation rules, mapping justification).

Currently, mappings are created by a variety of systems, manually curated and automatic, and we need a way to efficiently collect and combine them. Mapping sets and mappings with quality provenance metadata allow us to trace faulty mappings to the source and correct them in a way that _all_ users of the mapping set will profit from it.

## Is there a central repository of SSSOM files?
The idea of a mapping commons is to provide mappings in a decentralised fashion akin to OBO ontologies. A mapping commons collects 
mappings relevant to a particular community, either by reference (i.e. pulling in mapping sets already published elsewhere), or directly
maintained at the mapping commons ([example](https://github.com/mapping-commons/mh_mapping_initiative)). 
Their integration as part of a repository (mapping server) would look like [EBI's Ontology X-ref Browser](https://www.ebi.ac.uk/spot/oxo/) 
or [BioPortal](https://www.bioontology.org/wiki/BioPortal_Mappings),
but the exact scope of these repositories is _use case dependent_ - EBI may chose to show cross references from and to ontologies loaded into OLS, 
while BioPortal chooses to show a different set of mappings. The plan is to update EBI's OxO to support the full SSSOM data model, drawing curated
mappings from a variety of mapping commons, by Summer 2022 - but its unlikely that one central place will index all available mappings.

## Who is responsible for the conversion into SSSOM - the primary developers of an artefact, or a mapping commons?
Like with everything on the web, the closer to the source the SSSOM mappings are curated, the better. Ideally, mappings are maintained as 
part of ontology release pipelines or by primary mapping creators, rather than derived from a secondary source such as a database, further downstream.
The reason for this is that ideally, we would want mappings to be reviewable and editable in much the same way as open ontologies, 
offering issue trackers and an active community incorporating changes.

That said, it is unlikely that all existing mappings will be maintained by the source directly. For example, we expect to maintain the SSSOM mappings
derived from the vast majority of OBO ontology xrefs as a downstream task ([example](https://github.com/mapping-commons/ols-mapping-commons)).

## How dependent are we on the sssom-py toolkit?
SSSOM follows the core design principle that mapping tables should be (a) self-contained, i.e. including its prefix maps similar to a turtle file, 
and (b) readable by normal data science toolkits. An SSSOM table can be read with pandas using the `comment='#'` parameter 
(with one caveat, which is that `#` must be used as a character _solely_ to denote comments), or a very simply combination of a yaml reader and pandas. 

The SSSOM toolkit however offers some extra functionality, like export to JSON-LD, or RDF or import from other frequently used format.

## Is the concept of a "mapping server" equivalent, complementary, or antagonistic to the existing ontology repositories? 
A (SSSOM) mapping server is a repository for mappings that enables the browsing of existing mappings, exposing all (or some relevant subset of) SSSOM metadata as search
facets. In that sense, it should be considered complementary, as it enables the search for accurate mappings from a specific term or set of terms,
something that goes beyond what most ontologies would offer. However, the concept of ontology mappings can be _perceived_ as antagonistic to Open Ontology
principles, as its goal is _not the logical integration of knowledge, but the association or linking of terms across controlled semantic spaces_. 
The OBO vision involves the building of a coherent, non-redundant semantic space of logically interconnected ontologies, which in particular
wants to avoid the introduction of overlapping concepts. The mapping world specifically embraces heterogeneous semantic spaces and overlapping concepts,
and seeks to bridge the semantic gaps using well-defined mapping relations such as "skos:broadMatch" or "owl:equivalentClass".


