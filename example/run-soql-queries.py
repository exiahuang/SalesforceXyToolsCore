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
Run Soql Queries
"""
soql_string = "SELECT Id, Name FROM User LIMIT 3"
result = soap_api.query(soql_string)
pprint.pprint(result)
