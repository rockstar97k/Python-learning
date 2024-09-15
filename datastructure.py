list_of_cloud = ["Aws", "GCP", "oracle"]

list_of_env= ["Dev", "Operations"]

#list iteration
for env in list_of_env:
    print(list_of_env)

#dictionary
dict_of_cloud= {
    "aws": "Amazon Web Services",
    "azure": "Microsoft Azure"
}
print(dict_of_cloud["aws"])
print(dict_of_cloud.get("linux","not found"))
