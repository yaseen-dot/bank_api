def success_response(message, data=None):
    response = {"status": "success", "message": message}
    if data is not None:
        response["data"] = data
    return response

def error_response(message, code):
    return {"status": "error", "message": message}, code
