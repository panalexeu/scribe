from bson import ObjectId
from bson.errors import InvalidId


def is_valid_obj_id(obj_id):
    try:
        obj_id = str(obj_id)
        ObjectId(obj_id)
        return obj_id
    except InvalidId as e:
        raise ValueError(e)
