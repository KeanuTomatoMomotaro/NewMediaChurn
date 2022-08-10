# NewMediaChurn Research Project

This repository contains a python script that collects Indonesian headline news on 10th of August 2022 using the
[newsapi.com API](https://newsapi.org/), and visualizes the amount of content published by certain media outlets.
For reference, the data fetched using the newsapi request can be observed in the `headlines.xlsx` spreadsheet.

## Prerequisites
- Python 3.9.
- Newsapi.com api key.
- Substitute the following line in `main.py` with your actual newsapi.com key:
```
api_key = "your_api_key"
```
- Install `requests, matplotlib, numpy, pandas` python libraries.