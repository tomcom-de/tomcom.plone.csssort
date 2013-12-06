from tomcom.browser.public import *
from AccessControl import Unauthorized

from Products.GenericSetup.context import TarballExportContext
from export import TCCSSRegistryNodeAdapter

class ICSSSort(Interface):

    def export(self):
        """ """

class Browser(BrowserView):

    implements(ICSSSort)

    def export(self):
        """ """
        context=self.context
        portal=context.getAdapter('portal')()
        portal_setup=context.portal_setup
        portal_css=context.portal_css
        tec=TarballExportContext(portal_setup)

        string_=TCCSSRegistryNodeAdapter(portal_css,tec)._exportBody()

        REQUEST  = context.REQUEST
        RESPONSE = REQUEST.RESPONSE
        RESPONSE.setHeader('Content-Disposition','filename="cssregistry.xml"')
        RESPONSE.setHeader('Content-Type', 'text/plain; charset=utf-8')
        RESPONSE.setHeader('Content-Length', len(string_))
        RESPONSE.write(string_)