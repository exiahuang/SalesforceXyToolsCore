"""Simple-Salesforce Package"""

from .myconsole import MyConsole

from .api import (
    Salesforce,
    SalesforceAPI,
    SFType,
    SalesforceError,
    SalesforceMoreThanOneRecord,
    SalesforceExpiredSession,
    SalesforceRefusedRequest,
    SalesforceResourceNotFound,
    SalesforceGeneralError,
    SalesforceMalformedRequest
)

from .login import (
    SalesforceLogin, SalesforceAuthenticationFailed
)


from .core import (
    Soap,
    MetadataApi,
    RestApi,
    ToolingApi,
    SoapException
)




from .bulk import Bulk
