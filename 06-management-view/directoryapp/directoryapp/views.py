from pyramid.httpexceptions import HTTPFound

from substanced.sdi import mgmt_view
from substanced.form import FormView
from substanced.interfaces import IFolder

from .resources import (
    ContactSchema,
    )


## SDI "add" view for contacts
@mgmt_view(
    context=IFolder,
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

