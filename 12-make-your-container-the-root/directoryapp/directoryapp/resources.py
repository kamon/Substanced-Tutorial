import colander
import deform.widget

from persistent import Persistent

from zope.interface import (
    implementer,
    )

from pyramid.security import (
    Allow,
    Everyone,
    )
    
from substanced.content import content
from substanced.property import PropertySheet
from substanced.root import Root
from substanced.schema import (
    Schema,
    NameSchemaNode
    )
from substanced.util import renamer

        
## The Content object PropertySheet definition,
## based on the content schema.
class ContactSchema(Schema):
    name = NameSchemaNode(
        editing=lambda c, r: r.registry.content.istype(c, 'Contact'),
        )
    firstname= colander.SchemaNode(
        colander.String(),
        )
    lastname= colander.SchemaNode(
        colander.String(),
        )
    email= colander.SchemaNode(
        colander.String(),
        )
    telephone= colander.SchemaNode(
        colander.String(),
        )
    bio = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.RichTextWidget()
        )

class ContactPropertySheet(PropertySheet):
    schema = ContactSchema()


## The Content object (aka Model) class 
# Type registration
@content(
    'Contact',
    icon='icon-align-left',
    add_view='add_contact', 
    propertysheets = (
        ('Basic', ContactPropertySheet),
        ),
    catalog=True,
    )
class Contact(Persistent):

    name = renamer()
    
    def __init__(self, firstname='', lastname='', email='', telephone='', bio=''):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.telephone = telephone
        self.bio = bio



## Directory object, Root of the "Substance D" instance

class IDirectory(IFolder):
    pass


class DirectorySchema(Schema):
    """ The schema representing the directory root. """

    title = colander.SchemaNode(
        colander.String(),
        missing=''
        )
    description = colander.SchemaNode(
        colander.String(),
        missing=''
        )
    
class DirectoryPropertySheet(PropertySheet):
    schema = DirectorySchema()
    
@content(
    'Root',
    icon='icon-home',
    propertysheets = (
        ('', DirectoryPropertySheet),
        ),
    after_create= ('after_create', 'after_create2')
    )
@implementer(IDirectory)
class Directory(Root):
    title = ''
    description = ''

    @property
    def sdi_title(self):
        return self.title

    @sdi_title.setter
    def sdi_title(self, value):
        self.title = value
    
    def after_create2(self, inst, registry):
        acl = getattr(self, '__acl__', [])
        acl.append((Allow, Everyone, 'view'))
        self.__acl__ = acl
