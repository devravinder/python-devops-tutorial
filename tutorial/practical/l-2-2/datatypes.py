"""
-> there are many(4) instances & every instance has name, region, tags, os_type


"""

instnaces = [
    {
        "name": "dev-1",
        "region": "us-east-1",
        "tags": ["dev", "us-east"],
        "os_type": "linux",
    },
    {
        "name": "dev-2",
        "region": "us-west-1",
        "tags": ["dev", "us-west"],
        "os_type": "linux",
    },
    {
        "name": "prod-1",
        "region": "us-east-1",
        "tags": ["prod", "us-east"],
        "os_type": "linux",
    },
    {
        "name": "prod-2",
        "region": "us-west-1",
        "tags": ["prod", "us-west"],
        "os_type": "linux",
    },
]


skills = ["java", "js"]


firstInstance = instnaces[0]

print("firstInstance", firstInstance)


print("firstInstance name", firstInstance["name"])
