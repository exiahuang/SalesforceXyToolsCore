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


"""listAllMetadata """
for meta in meta_api.listAllMetadata():
    pprint.pprint(meta)
