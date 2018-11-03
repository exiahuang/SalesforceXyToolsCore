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


"""retrieve"""
result = meta_api.startRetrieve()
pprint.pprint(result)
# print(result["done"])
# print(result["id"])
# print(result["state"])


"""checkRetrieveStatus"""
retrieve_id = result["id"]
check_result = meta_api.checkRetrieveStatus(retrieve_id)
pprint.pprint(check_result)
