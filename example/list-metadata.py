import os,sys
sys.path.append("..")
from SalesforceXytoolsCore import *
from config import config
import pprint

meta_api = MetadataApi(username=config["username"], 
                password=config["password"], 
                security_token=config["security_token"], 
                sandbox=config["is_sandbox"],
                version=config["api_version"]
                )

"""listmeta"""
query_option_list = [
    {
        "metadata_type" : "EmailFolder",
        "folder" : ""
    },
    {
        "metadata_type" : "ApexClass",
        "folder" : ""
    }
]
listmeta_result = meta_api.listMetadata(query_option_list)
print(len(listmeta_result))
for meta in listmeta_result:
    pprint.pprint(meta)