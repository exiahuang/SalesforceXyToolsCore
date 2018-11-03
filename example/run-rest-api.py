import os,sys
sys.path.append("..")
from SalesforceXytoolsCore import *
from config import config
import pprint

rest_api = RestApi(username=config["username"], 
                password=config["password"], 
                security_token=config["security_token"], 
                sandbox=config["is_sandbox"],
                version=config["api_version"]
                )

"""
Run Rest API : query apexclass
"""
sel_string = "Select Id, Name From ApexClass Limit 3"
params = {'q': sel_string}
result = rest_api.restful('tooling/query', params)
pprint.pprint(result)


"""
Run Rest API : query ApexCodeCoverage
"""
sel_string = "SELECT Id, ApexTestClassId, TestMethodName, ApexClassorTriggerId, NumLinesCovered, NumLinesUncovered, Coverage FROM ApexCodeCoverage"
params = {'q': sel_string}
result = rest_api.restful(
    path='tooling/query', 
    params=params,
    method='GET'
)
pprint.pprint(result)


"""
Run Rest API : search sobjects
"""
result = rest_api.call_rest(
    method='GET',
    path='/services/data/v37.0/sobjects', 
    params={},
)
pprint.pprint(result)


