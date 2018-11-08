from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from xml.dom.minidom import parseString


# Create your views here.

@csrf_exempt
def get_integration_services(request):
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        xmlrequest = request.body
        dom = parseString(xmlrequest)
        isTest = dom.getElementsByTagName('mes:isTest')

        try:
            if len(isTest):
                xmlresponse = """<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
                              <env:Header/>
                              <env:Body>
                                  <paga:getIntegrationServicesResponse xmlns:paga="http://pagatech.com/merchant/messages">
                                      <paga:services>SUBMIT_PAYMENT</paga:services>
                                      <paga:services>VALIDATE_CUSTOMER</paga:services>
                                      <paga:services>QUERY_PAYMENTS</paga:services>
                                  </paga:getIntegrationServicesResponse>
                              </env:Body>
                          </env:Envelope>"""
                return HttpResponse(status=200, content=xmlresponse)
            else:
                return HttpResponse(status=400, content='Invalid request')


        except Exception as e:
            return HttpResponse(status=500, content='Internal Server Error')
