# How to set up a Mapping Commons

A mapping commons is an open, collaborative space for managing and reconciling mappings. The goal is to collect mappings from a variety of sources into a _mapping set registry_, standardise them into a common representation, curate some basic metrics such as "confidence" (how much does the community managing the commons trust a specific mapping source?) and provenance (where exactly did this mapping come from before it was integrated).

There is no agreed upon standard for mapping registries yet. SSSOM itself provides a [lightweight metadata model for mapping registries](https://mapping-commons.github.io/sssom/) which is, as of August 2023, under active development.

## Typical setup of a mapping commons

We recommend to base your mapping commons on a combination of GitHub (or GitLab) collaborative workflows (issues and discussions for the community, access management etc) and a git repository based on the [Mapping Commons Cookiecutter Template](https://github.com/mapping-commons/mapping-commons-cookiecutter) for version control of the mappings. 

Using the template system above allows you to: 

1. make use of basic CI and quality control for your mappings, 
2. provides a standard way to document metadata about your mapping sets
3. provides a basic ETL system based on `gnu make` (which you dont have to use, its just convenient)
4. Provides a standardised registry format that can be reused/imported by others.

Examples of Mapping Commons are:

1. https://github.com/mapping-commons/mh_mapping_initiative
1. https://gitlab.c-path.org/c-pathontology/mapping-commons
