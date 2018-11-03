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


"""createApexComponent"""
tooling_api.createApexComponent(MasterLabel, name, markup)
