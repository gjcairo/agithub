# Copyright 2012-2016 Jonathan Paugh and contributors
# See COPYING for license details
from agithub.base import API, ConnectionProperties, Client


class Bitbucket(API):
    """
    Bitbucket API

    More information can be found in https://developer.atlassian.com/bitbucket/api/2/reference/resource/

    Example usage:
    >>> bitbucket = Bitbucket(token)
    >>> bitbucket.repositories.get()
    """
    def __init__(self, token=None, *args, **kwargs):
        props = ConnectionProperties(
            api_url='api.bitbucket.org',
            url_prefix='/2.0',
            secure_http=True,
            extra_headers=self.generateAuthHeader(token),
        )
        self.setClient(Client(*args, **kwargs))
        self.setConnectionProperties(props)

    def generateAuthHeader(self, token):
        if token is not None:
            return {
                'Authorization': 'Bearer ' + token
            }
        return None
