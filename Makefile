MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run
# get values from about.yaml file
SCHEMA_NAME = sssom_schema
SOURCE_SCHEMA_PATH = src/sssom_schema/schema/sssom_schema.yaml
SRC = src
DEST = project
PYMODEL = $(SRC)/$(SCHEMA_NAME)/datamodel
DOCDIR = docs
TEMPLATE_DIR = $(SRC)/doc-templates

# basename of a YAML file in model/
.PHONY: all clean

help: status
	@echo ""
	@echo "make all -- makes site locally"
	@echo "make install -- install dependencies"
	@echo "make setup -- initial setup"
	@echo "make test -- runs tests"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make deploy -- deploys site"
	@echo "make update -- updates linkml version"
	@echo "make help -- show this help"
	@echo ""

status: check-config
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

setup: install gen-project gendoc git-init-add

install:
	poetry install
.PHONY: install

all: gen-project gendoc gen-excel get-context
%.yaml: gen-project
deploy: all mkd-gh-deploy

# generates all project files
gen-project: $(PYMODEL)
	$(RUN) gen-project \
		--exclude owl \
		-d $(DEST) $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)

test:
	$(RUN) gen-project \
		--exclude owl \
		-d tmp $(SOURCE_SCHEMA_PATH) 

check-config:
	@(grep my-datamodel about.yaml > /dev/null && printf "\n**Project not configured**:\n\n  - Remember to edit 'about.yaml'\n\n" || exit 0)

convert-examples-to-%:
	$(patsubst %, $(RUN) linkml-convert  % -s $(SOURCE_SCHEMA_PATH) -C Person, $(shell find src/data/examples -name "*.yaml")) 

get-context:
	mkdir -p $(SRC)/$(SCHEMA_NAME)/context
	cp $(DEST)/jsonld/* $(SRC)/$(SCHEMA_NAME)/context

examples/%.yaml: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.json: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.ttl: src/data/examples/%.yaml
	$(RUN) linkml-convert -P EXAMPLE=http://example.org/ -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@

upgrade:
	poetry add -D linkml@latest

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@


$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
	cp -rf $(SRC)/docs/* $(DOCDIR) ; \
	$(RUN) jinjanate $(SRC)/doc-templates/frontpage.md.jinja2 $(SOURCE_SCHEMA_PATH) -o $(DOCDIR)/index.md
	$(RUN) gen-doc -d $(DOCDIR) $(SOURCE_SCHEMA_PATH) --template-directory $(TEMPLATE_DIR) --index-name linkml-index

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

PROJECT_FOLDERS = sqlschema shex shacl protobuf prefixmap owl jsonschema jsonld graphql excel
git-init-add: git-init git-add git-commit git-status
git-init:
	git init
git-add:
	git add .gitignore .github Makefile LICENSE *.md examples utils about.yaml mkdocs.yml poetry.lock project.Makefile pyproject.toml src/linkml/*yaml src/*/datamodel/*py src/data
	git add $(patsubst %, project/%, $(PROJECT_FOLDERS))
git-commit:
	git commit -m 'Initial commit' -a
git-status:
	git status

clean:
	rm -rf $(DEST)
	rm -rf tmp

include project.Makefile
