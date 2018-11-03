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

"""get apex log"""
log_id = '07LXXXXXXXXXXXXXXXXXXXX'
result = tooling_api.getLog(log_id)
pprint.pprint(result)