## Add your own custom Makefile targets here
# Added by H2
EXCEL_DIR = $(DEST)/excel
DUP_SCHEMA_DIR = $(SRC)/linkml

gen-excel:
	mkdir -p $(EXCEL_DIR)
	$(RUN) gen-excel --output $(EXCEL_DIR)/sssom_schema.xlsx $(SOURCE_SCHEMA_PATH)

clean-yaml:
	rm -rf $(SRC)/$(SCHEMA_NAME)/src

build:
	poetry build
	make clean-yaml

deploy:
	poetry publish