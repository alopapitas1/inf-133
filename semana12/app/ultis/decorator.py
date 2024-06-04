import json
from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request,get_jwt_identity

def jwt_required(fn):
    @wraps(fn)
    def warpped(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args,*kwargs)
        except Exception as e:
            return jsonify({"error":str(e)}),401
    return warpped

def roles_required(roles=[]):
    def decorator(fn):
        @wraps(fn)
        def warpeds(*args,**kwargs):
            try:
                verify_jwt_in_request()
                current_user=get_jwt_identity()
                roles_user=json.loads(current_user.get("roles",[]))
                if not set(roles).intersection(roles_user):
                    return jsonify({"error":" unatirizado"}),401
                return fn(*args,**kwargs)
            except Exception as e:
                return jsonify({"error":str(e)}),401
        return warpeds
    return decorator

