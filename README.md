# Inspire

## spideref.py
This code scraps the inspire web in order to download the references of a given paper.  The url provided should be there references itself:
   http://inspirehep.net/record/_PAPER-ID_/references

### Usage
python spideref.py "http://inspirehep.net/record/1495568/references"

## mybibtex.py
This code scraps the inspire web in order to download all the papers by a given author.  The url provided should point to the whole list of references, like:
   http://inspirehep.net/search?ln=en&ln=en&p=exactauthor%3A_AUTHOR-NAME_.1&of=hb&action_search=Search&sf=earliestdate&so=d&rm=&rg=250&sc=0

### Usage
python mybibtex.py "http://inspirehep.net/search?ln=en&ln=en&p=exactauthor%3AJ.Doe.1&of=hb&action_search=Search&sf=earliestdate&so=d&rm=&rg=250&sc=0"
