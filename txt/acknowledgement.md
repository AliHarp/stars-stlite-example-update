# About

This work is part of the **S**haring **T**ools and **A**rtefacts for **R**eproducible **S**imulations (STARS) in Healthcare study.  

> 💡 This study is a fork of [`stars-streamlit-example`: a study investigated deploying Python DES models via streamlit.](https://github.com/pythonhealthdatascience/stars-streamlit-example)

This study is funded [UK Research and Innovation (UKRI)](https://www.ukri.org/) Medical Research Council's (MRC) [*Better Methods, Better Research* programme](https://www.ukri.org/opportunity/better-methods-better-research/).

> 📝 **Note:** The model presented here is part of STARS version 1.5.

## STARS Team

| Member      | ORCID |
| ----------- | ----------- |
| Thomas Monks      | [![ORCID: Monks](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481) |
| Alison Harper      | [![ORCID: Harper](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037)
| Navonil Mustafee      | [![ORCID: Mustafee](https://img.shields.io/badge/ORCID-0000--0002--2204--8924-brightgreen)](https://orcid.org/0000-0002-2204-8924)
| Andrew Mayne   | TBA |
| Amy Heather      | [![ORCID: Heather](https://img.shields.io/badge/ORCID-0000--0002--6596--3479-brightgreen)](https://orcid.org/0000-0002-6596-3479)|


## Modelling and Simulation Software

The model is written in `python3` and `simpy`.  The simulation libary `simpy` uses a **process based model worldview**.  Given its simplicity it is a highly flexible discrete-event simulation package.

One of the benefits of a package like `simpy` is that it is written in standard python and is free and open for others to use.  

* For research this is highly beneficial:
    * models and methods tested against them can be shared without concerns for commerical licensing.  
    * experimental results (either from model or method) can be recreated by other research teams.
* The version of `simpy` in use can also be controlled.  This avoids backwards compatibility problems if models are returned to after several years.

> Detailed documentation for `simpy` and additional models can be found here: https://simpy.readthedocs.io/en/latest/

## Simulation model interface

The interactive web application was developed in `stlite` a port of `streamlit` to [WebAssembly](https://webassembly.org/) and powered by [`pyodide`](https://pyodide.org/en/stable/). 


> Details and documentation for `stlite` can be found here: https://github.com/whitphx/stlite 
