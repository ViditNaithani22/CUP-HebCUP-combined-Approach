# CUP-HebCUP-combined-Approach

## Instructions:
### (1) After cloning the repository to your desired location, go to Data/Jasonl-RAW-data and extract the HebCUP_clean_dataset.zip file
### (2) run all the python scripts in Python-Scripts/RAW-Jasonl-To-CSV-script directory, to convert the given dataset from Jasonl files to csv files.
```
python training.py
python testing.py
python validating.py

```
### (3) run all the python scripts in Python-Scripts/CSV-file-labeling-script directory, to create new csv files where each row is labelled for CUP or HebCUP. 
```
python train_label.py
python test_label.py
python valid_label.py

```
### (4) run all the python scripts in Python-Scripts/Create-CUP-Jasonl-data directory, to create new Jasonl files for CUP. 
```
python filtering_CUP_train.py
python filtering_CUP_test.py
python filtering_CUP_valid.py

```
