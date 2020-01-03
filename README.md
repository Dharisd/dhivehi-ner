# Dhivehi NER
attempt at implementing Name entity recogniton for dhivehi

https://medium.com/@dharisd/dhivehi-name-entity-recogniton-e4b23a34bee3

# Installation
```
pip install spacy
``` 
## To add dhivehi to spacy

1.Find where spacy is installed with 
```
python -c "import os; import spacy; print(os.path.dirname(spacy.__file__))"
```
2.move the "di" folder in this repo to lang folder in spacy 

