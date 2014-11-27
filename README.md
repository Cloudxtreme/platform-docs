# Ushahidi Platform Docs

Ushahidi Platform docs pulled from the confluence wiki and scripts to import them

## Usinging the scripts

* Copy `wiki.cfg-template` to `.wiki.cfg`
* Edit `.wiki.cfg` to use your confluence username and password
* Set up the python env
```
cd scripts
virtualenv env
cd env
. bin/activate
cd ..
pip install -r requirements.txt
```

### Crawler script

```
./wiki-crawl-tree.py WIKI TopLevelPageTitle
```

This script will pull the Top level page and all its children to Markdown files
in the current directory.

### Get script

```
./wiki-get-page.py WIKI SomePageTitle
```

This script will pull the page, convert it to markdown and dump to stdout

