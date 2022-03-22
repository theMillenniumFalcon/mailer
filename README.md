# mass-mail
Tool that sends custom emails to the masses

## Structure

```
|
\-- constants.py        constants including email body
\-- data.csv            data for each email
\-- massmail.py         script entry point
\-- README.md           this document
\-- requirements.txt    python pkg requirements

```

## Setup

To setup the application, you will need python 3, pip, and virtualenv. You can run the application without pip or virtualenv if pandas is already installed.

### If using Mac OS / Linux
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### If using Windows
```
virtualenv env
env\Scripts\activate
pip install -r requirements.txt
```
