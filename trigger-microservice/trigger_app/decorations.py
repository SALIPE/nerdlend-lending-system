import jwt
from django.conf import settings
from django.http import JsonResponse

JWT_SECRET = settings.SECRET_KEY
JWT_ALGORITHM = "HS256"

def validate_jwt(view_func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Unauthorized"}, status=401)

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            user_email = payload.get("email")

            if user_email is None:
                return JsonResponse({"error": "Invalid token"}, status=404)
            else:
                request.email = user_email

        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

        return view_func(request, *args, **kwargs)

    return wrapper
