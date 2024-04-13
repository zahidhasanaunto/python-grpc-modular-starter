from src.modules.health.health_module import HealthModule
import grpc
from concurrent import futures
from src.config.env_config import config
from src.decorators.app_module_decorator import AppModule

@AppModule(
    imports=[
        HealthModule
    ]
)
class Application:
    def __init__(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        print("Application initialized")
    
    def serve(self):
        self.server.add_insecure_port(config.grpc_url)
        self.server.start()
        self.server.wait_for_termination()

        print(f"Application started on ${config.grpc_url}")

app = Application()