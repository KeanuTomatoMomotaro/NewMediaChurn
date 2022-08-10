# NewMediaChurn Research Project

This repository contains a python script that collects Indonesian headline news on 10th of August 2022 using the
[newsapi.com API](https://newsapi.org/), and visualizes the amount of content published by certain media outlets. [Chomsky](https://chomsky.info/consent01/) suggests that content published by large media outlets cooperating with the government influences public perception by pushing certain news agendas. Thus, this script can help us identify Indonesian large media outlets from the amount of published headlines, since it is hypothesized that readers are likely to be influenced by headline news. 

For reference, the data fetched using the newsapi request can be observed in the `headlines.xlsx` spreadsheet. In addition, `Figure_1`
contains the output of the python script.

## Prerequisites
- Python 3.9.
- Newsapi.com api key.
- Substitute the following line in `main.py` with your actual newsapi.com key:
```
api_key = "your_api_key"
```
- Install `requests, matplotlib, numpy, pandas, openpyxl` python libraries.

## Quickstart
- Import the project to an IDE such as [pycharm](https://www.jetbrains.com/pycharm/),
