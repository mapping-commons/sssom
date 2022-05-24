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