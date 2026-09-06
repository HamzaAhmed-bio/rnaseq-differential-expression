# add_gene_names.py
# Turn Ensembl IDs into human gene symbols using the MyGene.info API.

import json
import urllib.request
import urllib.parse

ids = [
    "ENSG00000179593",
    "ENSG00000277196",
    "ENSG00000109906",
    "ENSG00000171819",
    "ENSG00000127954",
    "ENSG00000163884",
    "ENSG00000168481",
    "ENSG00000152583",
    "ENSG00000274944",
    "ENSG00000101342",
    "ENSG00000162692",
    "ENSG00000146006",
    "ENSG00000118729",
    "ENSG00000223687",
]

url = "https://mygene.info/v3/query"

params = {
    "q": ",".join(ids),
    "scopes": "ensembl.gene",
    "fields": "symbol,name",
    "species": "human",
}

body = urllib.parse.urlencode(params).encode("utf-8")
request = urllib.request.Request(url, data=body)

with urllib.request.urlopen(request) as response:
    text = response.read().decode("utf-8")

results = json.loads(text)

for item in results:
    query = item.get("query", "?")
    symbol = item.get("symbol", "NOT FOUND")
    name = item.get("name", "")
    print(query, "=", symbol, "|", name)
