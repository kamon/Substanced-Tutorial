import colander
import deform.widget

from persistent import Persistent

from substanced.content import content
from substanced.property import PropertySheet
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
    )
class Contact(Persistent):

    name = renamer()
    
    def __init__(self, firstname='', lastname='', email='', telephone='', bio=''):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.telephone = telephone
        self.bio = bio
