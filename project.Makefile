## Add your own custom Makefile targets here
# Added by H2
EXCEL_DIR = $(DEST)/excel

gen-excel:
	mkdir -p $(EXCEL_DIR)
	$(RUN) gen-excel --output $(EXCEL_DIR)/sssom_schema.xlsx $(SOURCE_SCHEMA_PATH)

build:
	poetry build

pypi:
	poetry publish

#######################################
##### Mapping validation  #############
#######################################

MAPPING_DIR_SCHEMA=examples/schema
MAPPING_DIR_EMBEDDED=examples/embedded
TMPDIR = tmp

validate-example-schema-%:
	mkdir -p $(TMPDIR)
	tsvalid $(MAPPING_DIR_SCHEMA)/$*.sssom.tsv --comment "#" --skip E1
	sssom validate $(MAPPING_DIR_SCHEMA)/$*.sssom.tsv
	sssom convert $(MAPPING_DIR_SCHEMA)/$*.sssom.tsv -o $(TMPDIR)/schema-$*.sssom.ttl

validate-example-embedded-%:
	mkdir -p $(TMPDIR)
	tsvalid $(MAPPING_DIR_EMBEDDED)/$*.sssom.tsv --comment "#" --skip E1
	sssom validate $(MAPPING_DIR_EMBEDDED)/$*.sssom.tsv
	sssom convert $(MAPPING_DIR_EMBEDDED)/$*.sssom.tsv -o $(TMPDIR)/embedded-$*.sssom.ttl

MAPPINGS_SCHEMA=$(notdir $(wildcard $(MAPPING_DIR_SCHEMA)/*.sssom.tsv))
VALIDATE_MAPPINGS_SCHEMA=$(patsubst %.sssom.tsv, validate-example-schema-%, $(notdir $(wildcard $(MAPPING_DIR_SCHEMA)/*.sssom.tsv)))

MAPPINGS_EMBEDDED=$(notdir $(wildcard $(MAPPING_DIR_EMBEDDED)/*.sssom.tsv))
VALIDATE_MAPPINGS_EMBEDDED=$(patsubst %.sssom.tsv, validate-example-embedded-%, $(notdir $(wildcard $(MAPPING_DIR_EMBEDDED)/*.sssom.tsv)))

validate_mappings: 
	$(MAKE) $(VALIDATE_MAPPINGS_SCHEMA)
	$(MAKE) $(VALIDATE_MAPPINGS_EMBEDDED)
