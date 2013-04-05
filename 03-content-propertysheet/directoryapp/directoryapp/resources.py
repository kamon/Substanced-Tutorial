import colander
import deform.widget

from substanced.property import PropertySheet
from substanced.schema import (
    Schema,
    NameSchemaNode
    )

        
## The Content object PropertySheet definition

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
    
