## Add your own custom Makefile targets here
# Added by H2
EXCEL_DIR = $(DEST)/excel
DUP_SCHEMA_DIR = $(SRC)/linkml

move-yaml:
	mkdir -p $(SRC)/$(SCHEMA_NAME)/$(DUP_SCHEMA_DIR)
	cp $(SOURCE_SCHEMA_PATH) $(SRC)/$(SCHEMA_NAME)/$(DUP_SCHEMA_DIR)/$(SCHEMA_NAME).yaml

gen-excel:
	mkdir -p $(EXCEL_DIR)
	$(RUN) gen-excel --output $(EXCEL_DIR)/sssom_schema.xlsx $(SOURCE_SCHEMA_PATH)

clean::
	rm -rf $(SRC)/$(SCHEMA_NAME)/src