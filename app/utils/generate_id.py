import bson


def generate_id():
    """Generate a unique ID using BSON ObjectId."""
    return str(bson.ObjectId())