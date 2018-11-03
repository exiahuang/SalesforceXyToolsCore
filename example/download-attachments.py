import os,sys
sys.path.append("..")
from SalesforceXytoolsCore import *
from config import config
import pprint

SAVE_DIR = './attachments_download'
if not os.path.exists(SAVE_DIR):
    os.mkdir(SAVE_DIR)

rest_api = RestApi(username=config["username"], 
                password=config["password"], 
                security_token=config["security_token"], 
                sandbox=config["is_sandbox"],
                version=config["api_version"]
                )

attachments = rest_api.query("SELECT Id, Name, Body FROM Attachment LIMIT 2000")
print("添付ファイル件数 : " + str(len(attachments)))

for attachment in attachments["records"]:
    print("start to download : " + attachment["Name"])
    """
    Run Rest API : download attachment
    """
    rest_path = "/services/data/v42.0/sobjects/Attachment/{id}/Body".format(id=attachment["Id"])
    result = rest_api.call_rest(
        method='GET',
        path=rest_path, 
        params={},
    )
    with open(os.path.join(SAVE_DIR, attachment["Id"] + "_" + attachment["Name"]), mode='wb') as f:
        f.write(result.content)