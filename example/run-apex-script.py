import os,sys
sys.path.append("..")
from SalesforceXytoolsCore import *
from config import config
import pprint

soap_api = Soap(username=config["username"], 
                password=config["password"], 
                security_token=config["security_token"], 
                sandbox=config["is_sandbox"],
                version=config["api_version"]
                )

"""
Run Apex Script
"""
apex_string = "System.debug('hello world');"
debug_levels = {
        "DB": "Info", 
        "System": "DEBUG", 
        "Workflow": "INFO", 
        "Callout": "INFO", 
        "Validation": "INFO", 
        "Apex_Code": "DEBUG", 
        "Apex_Profiling": "INFO"
    }
result = soap_api.execute_anonymous(apex_string, debug_levels)
pprint.pprint(result)
