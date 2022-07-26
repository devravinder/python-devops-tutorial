import json

variables = open('data.json') # plin rext ( io.TextIOWrapper )

data = json.load(variables)

Values = data["tags"]
region = data["region"]

filters= [{
    "name":"tagName:doc", "Values":Values
}]