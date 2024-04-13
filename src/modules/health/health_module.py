from src.modules.health.health_controller import HealthController
import src.shared.types.health_pb2_grpc as health_pb2_grpc
from src.modules.health.health_controller import HealthController

controllers = [
    HealthController
]

class HealthModule:
    def __init__(self, server):
        self.controllers = controllers
        for controller in self.controllers:
            controller_instance = controller()
            health_pb2_grpc.add_HealthServiceServicer_to_server(controller_instance, server)
