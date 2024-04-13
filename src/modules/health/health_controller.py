from src.modules.health.health_service import HealthService
import src.shared.types.health_pb2_grpc as health_pb2_grpc

class HealthController(health_pb2_grpc.HealthServiceServicer):
    def __init__(self):
        self.service = HealthService()
    
    def CheckHealth(self, request, context):
        return self.service.check_health(request, context)