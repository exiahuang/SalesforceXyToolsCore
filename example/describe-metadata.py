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

"""
describeMetadata :
    This call retrieves the metadata that describes your organization. 
    This information includes Apex classes and triggers, custom objects, custom fields on standard objects, tab sets that define an app, and many other metadata types.
"""
result = meta_api.describeMetadata()
pprint.pprint(result)
# print(json.dumps(result, indent=4))