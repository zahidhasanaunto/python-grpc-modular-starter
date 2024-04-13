import src.shared.types.health_pb2 as health_pb2

class HealthService:
    def __init__(self):
        print("Health service initialized")

    def check_health(self, request, context):
        return health_pb2.HealthCheckResponse(status="OK")
