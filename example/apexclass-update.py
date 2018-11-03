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

apexclass_id = "set your apex class id"
body = """public class HelloWorld {
        private String mystr1;
}"""
tooling_api.updateApexClass(apexclass_id, body)