"""Endpoints 2.0 sample"""

import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote

# [START messages]
class AcmeRequest(messages.Message):
    content = messages.StringField(1)


class AcmeResponse(messages.Message):
    content = messages.StringField(1)

@endpoints.api(name='Acme', version='v1')
class AcmeAPI(remote.Service):

    @endpoints.method(
        AcmeRequest,
        AcmeResponse,
        path='acme/content',
        http_method='POST',
        name='acme_post_content')
    def acme_post(self, request):
        content = 'ACME API --> POST :  {}'.format(request.content)
        return AcmeResponse(content=content)

    @endpoints.method(
        AcmeRequest,
        AcmeResponse,
        path='acme/content/{content}',
        http_method='GET',
        name='acme_get_content')
    def acme_get(self, request):
        content = 'ACME API --> GET :  {}'.format(request.content)
        return AcmeResponse(content=content)

api = endpoints.api_server([AcmeAPI])