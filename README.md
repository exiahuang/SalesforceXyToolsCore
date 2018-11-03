
SalesforceXytoolsCore is the core of [SalesforceXytools-for-sublime](https://github.com/exiahuang/SalesforceXyTools).
It is base on [simple-salesforce](https://github.com/simple-salesforce/simple-salesforce).

# Support
* Sobject Record Management : sobject create, get, get_by_custom_id, update, delete
* Sobject Queries : query, query_more, search, query_allsearch
* Sobject Bulk action
* Run Apex Script
* Metadata Control : describeMetadata, listAllMetadata, getAllMetadataMap, listmeta, listFolder, retrieve, etc.
* Package.xml builder.
* Retrieve Metadata to memory, Retrieve Metadata zip file.
* ApexClass, Trigger, ApexComponent, ApexPage: create, update, delete, get
* Get Apex Log 
* Run test class

# Usage

## Requirement
* Python3
* [requests](http://requests-docs-ja.readthedocs.io/en/latest/)

## download it , and import to your project
```
from SalesforceXytoolsCore import *
```

## sobject create, get, get_by_custom_id, update, delete 
```python
username = ""
password = ""
soap_api = Soap(username=username, 
                password=password, 
                security_token='', 
                sandbox=True,
                version='40.0'
                )

sobject_name = "Account"
sobject = soap_api.get_sobject(sobject_name)

"""
create a new Sobject in Salesforce
"""
new_account = sobject.create({'Name':'Exia.Huang'})
sobject_id = new_account["id"]
print(new_account)

"""
get a Sobject in Salesforce
"""
sobject1 = sobject.get(sobject_id)
print(sobject1)

"""
get a Sobject by External ID
"""
sobject2 = sobject.get_by_custom_id('My_Custom_ID__c', '22')

"""
update a Sobject in Salesforce
"""
sobject3 = sobject.update(sobject_id,{'LastName': 'Huangxy'})

"""
delete a Sobject in Salesforce
"""
sobject.delete(sobject_id)
```


## Run Apex Script
```python
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
print(result)
```

## Metadata Control : describeMetadata, listAllMetadata, getAllMetadataMap, listmeta, listFolder, retrieve, etc.
```python
meta_api = MetadataApi(username=username, 
                password=password, 
                security_token='', 
                sandbox=True,
                version='40.0'
                )

"""
describeMetadata :
    This call retrieves the metadata that describes your organization. 
    This information includes Apex classes and triggers, custom objects, custom fields on standard objects, tab sets that define an app, and many other metadata types.
"""
result = meta_api.describeMetadata()
print(json.dumps(result, indent=4))



"""listAllMetadata """
for meta in meta_api.listAllMetadata():
    print(meta)
    print(meta['type'] + " : " + meta['fullName'] + " : " + meta['fileName'])

"""getAllMetadataMap"""
all_metadata_map = meta_api.getAllMetadataMap()

"""listmeta"""
query_option_list = [
{
    "metadata_type" : "EmailFolder",
    "folder" : ""
},
{
    "metadata_type" : "ApexClass",
    "folder" : ""
}
]
listmeta_result = meta_api.listMetadata(query_option_list)
print(len(listmeta_result))
for meta in listmeta_result:
    print(meta)


"""packageTypeList"""
print('>>>packageTypeList')
print(meta_api.packageTypeList())


"""listFolder"""
folder = meta_api.listFolder("EmailTemplate")

"""checkRetrieveStatus"""
retrieve_id = '09Sxxxxxxxxxxxx'
result = meta_api.checkRetrieveStatus(retrieve_id)
print(result)
```

## Retrieve Metadata to memory
```python
"""retrieve"""
result = meta_api.startRetrieve()
print(result)
print(result["done"])
print(result["id"])
print(result["state"])
```

## Retrieve Metadata zip file
```python
"""retrieve zip file"""
meta_api.retrieveZip("C:\\Users\\exia\\workspace","test20180615.zip")
```


## Package.xml builder.
```python
"""buildPackageXml"""
packagexml = meta_api.buildPackageXml()
print('>' * 80)
print('>>>buildPackageXml')
print(packagexml)
```


## Tooling API

ApexClass, Trigger, ApexComponent, ApexPage: create, update, delete, get
```python
tooling_api = ToolingApi(username=username, 
                password=password, 
                security_token='', 
                sandbox=True,
                version='40.0'
                )

"""createApexClass"""
name = "HelloWorld"
body = """public class HelloWorld {
        private String hee;
}"""
status_code, result = tooling_api.createApexClass(name, body)
print(status_code)
print(result)


"""getApexClass"""

"""deleteApexClass"""
id="01pxxxxx"
status_code, result = tooling_api.deleteApexClass(id)
print(status_code)
print(result)

"""updateApexClass"""
body = """public class HelloWorld3 {
        private String hee4;
}"""
print(tooling_api.updateApexClass("01p5D000000FXc5", body))


"""createTrigger"""
tooling_api.createTrigger(tableEnumOrId, name, body)

"""createApexComponent"""
tooling_api.createApexComponent(MasterLabel, name, markup)

"""createApexPage"""
tooling_api.createApexPage(MasterLabel, name, markup)


"""run test class"""
id_list = ['xxx', 'xxxx']
tooling_api.runTestSynchronous(id_list)

"""get apex log"""
log_id = ''
tooling_api.getLog(log_id)

```

