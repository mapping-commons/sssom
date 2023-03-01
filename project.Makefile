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

tmp/sssom.py:
	$(MAKE) src/sssom_schema/datamodel/sssom_schema.py
	mv 

tests/output/out.json: $(SOURCE_SCHEMA_PATH) tests/input/mapping_set.ttl
	$(RUN) linkml-convert -f ttl -C MappingSet -t json -s $^ --output $@

tests/output/out.ttl: $(SOURCE_SCHEMA_PATH) tests/output/out.json
	$(RUN) linkml-convert -f json -C MappingSet -t ttl -s $^ --output $@

tests/output/out.jsonld: $(SOURCE_SCHEMA_PATH) tests/output/out.ttl tests/input/context.jsonld
	$(RUN) linkml-convert -f ttl -C MappingSet -t json-ld -c tests/input/context.jsonld -s $(SOURCE_SCHEMA_PATH) tests/output/out.ttl --output $@

test-convert: tests/output/out.jsonld
	cmp --silent tests/validate/out.ttl tests/output/out.ttl