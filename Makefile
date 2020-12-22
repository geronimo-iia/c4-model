# Project settings
PACKAGE := c4_model
REPOSITORY := geronimo-iia/c4-model
PACKAGES := $(PACKAGE) tests
MODULES := $(wildcard $(PACKAGE)/*.py)

# const
.DEFAULT_GOAL := help
FAILURES := .cache/v/cache/lastfailed
DIST_FILES := dist/*.tar.gz dist/*.whl
SPHINX_BUILD_DIR = .cache/sphinx

# MAIN TASKS ##################################################################

.PHONY: all
all: install

.PHONY: ci
ci: check test ## Run all tasks that determine CI status

.PHONY: debug-info
debug-info:  ## Show poetry debug info
	poetry debug:info

.PHONY: help
help: all
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# PROJECT DEPENDENCIES ########################################################

install: .install .cache ## Install project dependencies

.install: poetry.lock
	poetry install
	poetry check
	@touch $@

poetry.lock: pyproject.toml
	poetry lock
	@touch $@

.cache:
	@mkdir -p .cache

requirements.txt: poetry.lock ## Generate requirements.txt
	poetry export --without-hashes -f requirements.txt > requirements.txt


# CHECKS ######################################################################

.PHONY: check
check: install   ## Run linters and static analysis
	poetry run isort $(PACKAGES)
	poetry run black $(PACKAGES)
	poetry run flakehell lint $(PACKAGES)
	poetry run mypy $(PACKAGE)

# TESTS #######################################################################

.PHONY: test
test: install ## Run unit tests
	@if test -e $(FAILURES); then poetry run pytest tests --last-failed --exitfirst; fi
	@rm -rf $(FAILURES)
	poetry run pytest



# BUILD #######################################################################

.PHONY: build
build: install check test $(DIST_FILES) ## Builds the source and wheels archives
$(DIST_FILES): $(MODULES) pyproject.toml
	@rm -f $(DIST_FILES)
	poetry build

# RELEASE #####################################################################

.PHONY: publish
publish: build ## Publishes the package, previously built with the build command, to the remote repository
	@git diff --name-only --exit-code
	poetry publish
	@PROJECT_RELEASE=$$(poetry run python -c "import c4_model; print(c4_model.__version__);") && \
		git tag "v$$PROJECT_RELEASE" && \
		git push origin "v$$PROJECT_RELEASE"
	@echo "open https://pypi.org/project/c4"

# DOC #########################################################################

.PHONY: docs
docs:  ## Build and publish sit documentation.
	@rm -rf docs/
	@rm -rf $(SPHINX_BUILD_DIR)/
	@mkdir -p $(SPHINX_BUILD_DIR)
	@poetry run sphinx-build -M html "sphinx" "$(SPHINX_BUILD_DIR)"
	@mv $(SPHINX_BUILD_DIR)/html docs/
	@touch docs/.nojekyll


# CLEANUP #####################################################################

.PHONY: clean
clean:  ## Delete all generated and temporary files
	@rm -rf *.spec dist build .eggs *.egg-info .install
	@rm -rf .cache .pytest .coverage htmlcov
	@find $(PACKAGES) -name '__pycache__' -delete
	@rm -rf *.egg-info
