# Change Log

## [v0.2.0]() - 2024-06-05

### Changes

* ENV: upgraded to stlite 0.57.0 and treat-sim 2.1.0
* IMG: upgraded process flow image to be consistent with docs
* CHANGES: modified changlog format to be based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

## [v0.1.0](https://github.com/pythonhealthdatascience/stars-stlite-example/releases/tag/v0.1.0) - 2024-04-24 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11060532.svg)](https://doi.org/10.5281/zenodo.11060532)

### Changes

* FORKED: `stars-streamlit-example` at v3.0.0. https://github.com/pythonhealthdatascience/stars-streamlit-example 
* DEPLOY: Modified code to use `stlite` v0.52.4 and run locally in the browser instead of deploying a `streamlit` app via streamlit community cloud.
* ENV: Introduced PyPi `treat-sim` v1.1.0 dependency
* CITE: Updated CITATION.cff meta data 
* PAGES: Information updates to About page.

### Removed

* DOCKER: removed all docker support and associated files.
* MODEL: removed model.py as replaced by `treat-sim`
* ENV: Dropped all support for `matplotlib` and removed all `matplotlib` code from `more_plot.py`

