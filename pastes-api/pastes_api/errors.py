def not_found_error(message):
    return {
        "type": "NotFound",
        "message": message
    }


def validation_error(errors):
    return {
        "type": "Validation",
        "message": "There were validation errors.",
        "errors": errors
    }

def internal_error():
    return {
        "type": "Internal",
        "message": "Internal server error. Something went wrong, that's all we know."
    }
