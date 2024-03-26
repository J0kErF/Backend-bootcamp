from request_stream import RequestGenerator
from server import Server
class LoadBalancer:
    def __init__(self, event_generator, servers=[],servers_count=4):
        self.event_generator = event_generator

        self.servers = servers
        if servers is None or servers == []:
            for i in range(0,servers_count):
                self.servers.append(Server("tickets.json", max_requests_per_time=10, requests_threshold_delay=3, max_concurrent_requests=5))
        
        
        ##for round robin workes like lru
        self.current_server = 0
        
    def process_events(self):
        for event in self.event_generator.generate_events():
            self.handle_event(event)

    def handle_event(self, event):
        # Here you can implement any logic to process the event
        print("Received event:", event)
        self.round_robin(event)

    def round_robin(self, event):
        if self.servers is None or self.servers==[] or event is None:
            return
        if self.current_server >= len(self.servers):
            self.current_server = 0
        
        server = self.servers[self.current_server]

        self.current_server += 1
        print("Server: ",self.current_server)
        server.process_request(event)

# Example usage:
if __name__ == "__main__":
    request_generator = RequestGenerator()
    load_balancer = LoadBalancer(request_generator)

    load_balancer.process_events()
