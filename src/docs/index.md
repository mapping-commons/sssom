# Simple Standard for Sharing Ontological Mappings (SSSOM)

![SSSOM banner](images/sssom-banner.png)

**SSSOM** is the Simple Standard for Sharing Ontological Mappings. It comprises three distinct components that are intended to be used together to facilitate the exchange of semantic mappings:

1. a machine-readable and extensible vocabulary to describe metadata of mappings;
2. a data model to represent mappings and their associated metadata;
3. several file formats to represent sets of mappings on disk and on the network.

Beyond defining the standard itself, the **SSSOM Core Team** also aims to implement open and community-driven collaborative workflows designed to evolve the standard continuously to address changing requirements and mapping practices, and to provide reference tools and software libraries for working with the standard.

## SSSOM at a glance

### Basic concepts

The [data model](spec-model.md) of SSSOM is centered around two fundamental concepts: mappings and mapping sets.

A **SSSOM mapping** is a statement that there is a correspondence of some sort between two semantic entities. It comprises two components:

1. The **core mapping** (or **raw mapping**), which is a triple `<subject, predicate, object>` that represents the correspondence itself between a subject entity, for example a class in an ontology, and an object entity, for example an identifier in some database, via a semantic mapping predicate, for example `skos:exactMatch`.
2. **Metadata** that provide supplementary pieces of information about the core mapping. This notably includes information pertaining to the *provenance* of the statement (for example, who emitted the statement, in other words who decided that the subject and the object should be mapped) and its *justification* (why should the subject and the object be mapped).

A **SSSOM mapping set** is a collection of SSSOM mappings, with its own metadata.

### The SSSOM/TSV format

The main format proposed by the SSSOM standard to exchange mapping sets is the [SSSOM/TSV format](spec-formats-tsv.md). Here is a basic example of a file in that format:

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

### Quick links

**General**

- [GitHub page](https://github.com/mapping-commons/sssom)
- [Detailed description](introduction.md)
- [Formal specification](spec-intro.md)

**Publications**

- [A Simple Standard for Sharing Ontological Mappings (SSSOM)](https://doi.org/10.1093/database/baac035) (initial publication in _Database_)
- [A Simple Standard for Ontological Mappings 2022: Updates of data model and outlook](https://zenodo.org/record/7672104) (paper and presentation at the Ontology Matching Workshop 2022)
- [A Simple Standard for Ontological Mappings 2023: Updates on data model, collaborations and tooling](https://zenodo.org/record/8202395) (paper and presentation at the Ontology Matching Workshop 2023)
- [Other presentations](presentations.md)

**Related software**

- [SSSOM Toolkit](https://mapping-commons.github.io/sssom-py/) (reference implementation of the standard, in Python)

## The SSSOM Core Team

### Contact

The preferred way to contact the SSSOM team is through the [issue tracker](https://github.com/mapping-commons/issues) (for problems with SSSOM) or the [GitHub discussion forums](https://github.com/mapping-commons/sssom/discussions) (for general questions).

You can find any of the members of the SSSOM core team [on GitHub](https://github.com/orgs/mapping-commons/teams/sssom-core). Their GitHub profiles usually also provide email addresses.

You can also reach us in the [OBO Foundry Slack](https://obo-communitygroup.slack.com/archives/C01DP18L5GW), in the `#sssom` channel.

### Documentation/specification editors

* [Nicolas Matentzoglu](https://orcid.org/0000-0002-7356-1779) (Semanticly Ltd; [@matentzn](https://github.com/matentzn))
* [Chris Mungall](https://orcid.org/0000-0002-6601-2165) (LBL)
* [Ernesto Jimenez-Ruiz](https://orcid.org/0000-0002-9083-4599) (City, University of London)
* [John Graybeal](https://orcid.org/0000-0001-6875-5360) (Stanford)
* [William Duncan](https://orcid.org/0000-0001-9625-1899) (LBL)
* [David Osumi-Sutherland](https://orcid.org/0000-0002-7073-9172) (EMBL-EBI)
* [Simon Jupp](https://orcid.org/0000-0002-0643-3144) (SciBite)
* [James McLaughlin](https://orcid.org/0000-0002-8361-2795) (EMBL-EBI)
* [Henriette Harmse](https://orcid.org/0000-0001-7251-9504) (EMBL-EBI)
* [Tiffany Callahan](https://orcid.org/0000-0002-8169-9049) ([@callahantiff](https://github.com/callahantiff))
* [Charlie Hoyt](https://orcid.org/0000-0003-4423-4370) (Harvard Medical School; [@cthoyt](https://github.com/cthoyt))
* [Thomas Liener](https://orcid.org/0000-0003-3257-9937) (Pistoia Alliance)
* [Harshad Hegde](https://orcid.org/0000-0002-2411-565X) (LBL)

### Contributors

* [Alasdair Gray](https://orcid.org/0000-0002-5711-4872)
* [Alex Wagner](https://orcid.org/0000-0002-2502-8961)
* [Amelia L. Hoyt](https://orcid.org/0000-0003-1307-2508)
* [Andrew Williams](https://orcid.org/0000-0002-0692-412X)
* [Anne Thessen](https://orcid.org/0000-0002-2908-3327)
* [Benjamin M. Gyori](https://orcid.org/0000-0001-9439-5346)
* [Bill Baumgartner](https://orcid.org/0000-0001-6717-5313)
* [Christopher Chute](https://orcid.org/0000-0001-5437-2545)
* [Chris T. Evelo](https://orcid.org/0000-0002-5301-3142)
* [Damion Dooley](https://orcid.org/0000-0002-8844-9165)
* [Davera Gabriel](https://orcid.org/0000-0001-9041-4597)
* [Harold Solbrig](https://www.wikidata.org/wiki/Q44607574)
* [HyeongSik Kim](https://orcid.org/0000-0002-3002-9838)
* [Ian Harrow](https://orcid.org/0000-0003-0109-0522)
* [James Malone](https://orcid.org/0000-0002-1615-2899)
* [James Overton](https://orcid.org/0000-0001-5139-5557)
* [James P. Balhoff](https://orcid.org/0000-0002-8688-6599)
* [James Stevenson](https://orcid.org/0000-0002-2568-6163)
* [Jiao Dahzi](https://orcid.org/0000-0001-5052-3836)
* [Joe Flack](https://orcid.org/0000-0002-2906-7319)
* [Jooho Lee](https://orcid.org/0000-0002-2955-3405)
* [Julie McMurry](https://orcid.org/0000-0002-9353-5498)
* [Kori Kuzma](https://orcid.org/0000-0002-9954-7449)
* [Kristin Kostka](https://orcid.org/0000-0003-2595-8736)
* [Lauren Chan](https://orcid.org/0000-0002-7463-6306)
* [Melissa Haendel](https://orcid.org/0000-0001-9114-8737)
* [Monica Munoz-Torres](https://orcid.org/0000-0001-8430-6039)
* [Nicole Vasilevsky](https://orcid.org/0000-0001-5208-3432)
* [Nomi Harris](https://orcid.org/0000-0001-6315-3707)
* [Núria Queralt-Rosinach](https://orcid.org/0000-0003-0169-8159)
* [Sabrina Toro](https://orcid.org/0000-0002-4142-7153)
* [Sebastian Koehler](https://orcid.org/0000-0002-5316-1399)
* [Shahim Essaid](https://orcid.org/0000-0003-2338-2550)
* [Sierra Moxon](https://orcid.org/0000-0002-8719-7760)
* [Sue Bello](https://orcid.org/0000-0003-4606-0597)
* [Tim Putman](https://orcid.org/0000-0002-4291-0737)

## Acknowledgements

- See [Funding](funding.md) for details on direct contributions.
- We thank the [Link Model Language (LinkML) project](https://github.com/linkml) and team for their great framework and the LinkML team for their support developing the schema.
