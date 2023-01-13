# USE AT YOUR OWN RISK: ACCOUNT MIGHT GET FLAGGED:

## JournalScraper
This program can be used to download an entire issue of a journal:

# installation:
1. Install Python3
```
sudo apt-get update
sudo apt-get install python3.9
```
2. Create virtual environment
```
python3 -m venv CHOOSE/YOUR/OWN/PATH/JournalScraper
```
3. Upgrade pip
```
CHOOSE/YOUR/OWN/PATH/JournalScraper/bin/python3 -m pip install --upgrade pip
```
4. Activate environment
```
source CHOOSE/YOUR/OWN/PATH/JournalScraper/bin/activate
```
5. install requirements
```
pip install -r requirements.txt
```

Example use:
```
./JournalScraper.py --url https://www.nature.com/nature/volumes/613/issues/7943
```
