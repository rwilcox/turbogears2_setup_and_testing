# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_

from turbo_scrape.lib.base import BaseController
from turbo_scrape.model import DBSession, metadata
from turbo_scrape.controllers.error import ErrorController

# for CatWalk
from catwalk.tg2 import Catwalk
import turbo_scrape.model #import *

# end for AdminController

from turbo_scrape.controllers.contacts import ContactsController
__all__ = ['RootController']
class UnSecuredCatwalk(Catwalk):
    allow_only = None

class RootController(BaseController):
    """
    The root controller for the turbo-scrape application.
    
    All the other controllers and WSGI applications should be mounted on this
    controller. For example::
    
        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()
    
    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.
    
    """
    
    error = ErrorController()
    catwalk = UnSecuredCatwalk( turbo_scrape.model, DBSession)
    contacts = ContactsController(DBSession)
    
    @expose('turbo_scrape.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('turbo_scrape.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')


