[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11060532.svg)](https://doi.org/10.5281/zenodo.11060532)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100+/)
[![Read the Docs](https://readthedocs.org/projects/pip/badge/?version=latest)](https://pythonhealthdatascience.github.io/stars-simpy-example-docs)
[![License: MIT](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037)
[![License: MIT](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)

# 💫 Towards Sharing Tools and Artifacts for **Reproducible** Simulation **(v1.5)**: an `stlite` template for `simpy` models

## 1. Overview

The materials and methods in this repository support work towards developing the S.T.A.R.S healthcare framework version 1.5 (**S**haring **T**ools and **A**rtifacts for **R**eproducible **S**imulations in healthcare).  The code and written materials here are a work in progress to demonstrate the application of S.T.A.R.S' version to sharing a `simpy` discrete-event simuilation model and associated research artifacts. 

The model will run on a users browser without the need to manually install any components.  This is achieved using WebAssembly technology and serverless `streamlit` i.e. [stlite](https://github.com/whitphx/stlite).  A model and streamlit interface is downloaded to the users local machine and all dependencies are installed at runtime from `pyodide` using micropip. There is a short wait while the model is setup. Once this is complete the model is then executed on the local. No data entered leaves the local machine.

**Please note that `stlite` currently does not work in Mozilla FireFox**

> Try it in your browser now: https://pythonhealthdatascience.github.io/stars-stlite-example

## Author ORCIDs

[![ORCID: Harper](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037)
[![ORCID: Monks](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)

## Citation

> Monks, T., & Harper, A. (2024). Towards Sharing Tools and Artifacts for Reproducible Simulation **(v1.5)**: an `stlite` template for `simpy` models (v0.1.0). Zenodo. https://doi.org/10.5281/zenodo.11060532

```bibtex
@software{monks_harper_stlite_example,
  author       = {Monks, Thomas and
                  Harper, Alison},
  title        = {{Towards Sharing Tools and Artifacts for 
                   Reproducible  Simulation **(v1.5)**: an `stlite`
                   template for `simpy` models}},
  month        = apr,
  year         = 2024,
  publisher    = {Zenodo},
  version      = {v0.1.0},
  doi          = {10.5281/zenodo.11060532},
  url          = {https://doi.org/10.5281/zenodo.11060532}
}
```
## Funding

STARS is funded by the [UK Research and Innovation (UKRI)](https://www.ukri.org/) Medical Research Council's (MRC) [*Better Methods, Better Research* programme](https://www.ukri.org/opportunity/better-methods-better-research/).

> 🗒️ The original code from `stars-streamlit-example` is independent research supported by the National Institute for Health Research Applied Research Collaboration South West Peninsula. The views expressed in this publication are those of the author(s) and not necessarily those of the National Institute for Health Research or the Department of Health and Social Care.

## Case study model

**This example is based on exercise 13 from Nelson (2013) page 170.**

> *Nelson. B.L. (2013). [Foundations and methods of stochastic simulation](https://www.amazon.co.uk/Foundations-Methods-Stochastic-Simulation-International/dp/1461461596/ref=sr_1_1?dchild=1&keywords=foundations+and+methods+of+stochastic+simulation&qid=1617050801&sr=8-1). Springer.* 

We adapt a textbook example from Nelson (2013): a terminating discrete-event simulation model of a U.S based treatment centre. In the model, patients arrive to the health centre between 6am and 12am following a non-stationary Poisson process. On arrival, all patients sign-in and are triaged into two classes: trauma and non-trauma. Trauma patients include impact injuries, broken bones, strains or cuts etc. Non-trauma include acute sickness, pain, and general feelings of being unwell etc. Trauma patients must first be stabilised in a trauma room. These patients then undergo treatment in a cubicle before being discharged. Non-trauma patients go through registration and examination activities. A proportion of non-trauma patients require treatment in a cubicle before being discharged. The model predicts waiting time and resource utilisation statistics for the treatment centre. The model allows managers to ask question about the physical design and layout of the treatment centre, the order in which patients are seen, the diagnostic equipment needed by patients, and the speed of treatments. For example: “what if we converted a doctors examination room into a room where nurses assess the urgency of the patients needs.”; or “what if the number of patients we treat in the afternoon doubled” 

## Deployment

The model has been deployed to GitHub pages and uses `stlite`

* https://pythonhealthdatascience.github.io/stars-stlite-example


## Online documentation produced by Jupyter-book

[![Read the Docs](https://readthedocs.org/projects/pip/badge/?version=latest)](https://pythonhealthdatascience.github.io/stars-simpy-example-docs)

We have a separate artifact that documents the model. 

* The documentation can be access at [https://pythonhealthdatascience.github.io/stars-simpy-example-docs](https://pythonhealthdatascience.github.io/stars-simpy-example-docs)
