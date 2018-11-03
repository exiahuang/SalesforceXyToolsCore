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

print('hello SalesforceXytoolsCore Test start')
Account = soap_api.get_sobject("Account")

"""
get a Sobject in Salesforce
"""
acc_id="set your sobject id"
account1 = Account.get(acc_id)
pprint.pprint(account1)

"""
create a new Sobject in Salesforce
"""
new_account = Account.create({'Name':'Exia.Huang'})
pprint.pprint(new_account)

"""
update a Sobject in Salesforce
"""
acc_id="set your sobject id"
account1 = Account.update(acc_id,{'LastName': 'sfdc'})
pprint.pprint(account1)

"""
delete a Sobject in Salesforce
"""
acc_id="set your sobject id"
Account.delete(acc_id)


"""
get a Sobject by External ID
"""
account1 = Account.get_by_custom_id('My_Custom_ID__c', 'custom_id')
pprint.pprint(account1)
