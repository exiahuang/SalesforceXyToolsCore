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

"""createApexClass"""
name = "HelloWorld"
body = """public class HelloWorld {
        private String mystr;
}"""
status_code, result = tooling_api.createApexClass(name, body)
print(status_code)
pprint.pprint(result)