from pyramid.httpexceptions import HTTPFound

from pyramid.renderers import get_renderer

from substanced.sdi import mgmt_view
from substanced.form import FormView
from substanced.interfaces import IRoot

from .resources import (
    ContactSchema,
    Contact,
    )


## SDI "add" view for contacts
@mgmt_view(
    context=IRoot,
    name='add_contact',
    tab_title='Add Contact', 
    permission='sdi.add-content', 
    renderer='substanced.sdi:templates/form.pt',
    tab_condition=False,
    )
class AddContactView(FormView):
    title = 'Add Contact'
    schema = ContactSchema()
    buttons = ('add',)

    def add_success(self, appstruct):
        registry = self.request.registry
        name = appstruct.pop('name')
        contact = registry.content.create('Contact', **appstruct)
        self.context[name] = contact
        return HTTPFound(
            self.request.sdiapi.mgmt_path(self.context, '@@contents')
            )


## Retail view for contacts
@view_config(
    context=Contact,
    renderer='templates/contact.pt',
    )
def contact_view(context, request):
    return {'title': context.firstname + ' ' + context.lastname,
            'body': context.bio,
            'master': get_renderer('templates/master.pt').implementation(),
           }

