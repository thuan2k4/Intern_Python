from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()
    password = fields.String()

"""
- Serialization: Dict -> JSON
- Deserialization: JSON -> Dict (check validation)
- Validation: check data type
"""