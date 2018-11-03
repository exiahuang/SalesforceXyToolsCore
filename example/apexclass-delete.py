import os,sys
sys.path.append("..")
from SalesforceXytoolsCore import *
from config import config
import pprint


tooling_api = ToolingApi(username=config["username"], 
                password=config["password"], 
                security_token=config["security_token"], 
                sandbox=config["is_sandbox"],
                version=config["api_version"]
                )

"""deleteApexClass"""
apexclass_id="set your apex class id"
status_code, result = tooling_api.deleteApexClass(apexclass_id)
print(status_code)
print(result)