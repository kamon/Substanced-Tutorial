import colander
import deform.widget

from substanced.schema import (
    Schema,
    NameSchemaNode
    )

        
## The Content object schema

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
    
