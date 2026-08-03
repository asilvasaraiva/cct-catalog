from django.db import connections
from django.db.utils import OperationalError
from django.http import JsonResponse


def liveness(request):
    return JsonResponse({"status": "UP"})


def readiness(request):
    try:
        connections["default"].cursor()
    except OperationalError:
        return JsonResponse({"status": "DOWN"}, status=503)
    return JsonResponse({"status": "UP"})
