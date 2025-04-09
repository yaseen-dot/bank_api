from flask_smorest import abort

def conflict(message="Conflict"):
    abort(409, message=message)

def unauthorized(message="Unauthorized"):
    abort(401, message=message)

def not_found(message="Not found"):
    abort(404, message=message)

def bad_request(message="Bad request"):
    abort(400, message=message)
