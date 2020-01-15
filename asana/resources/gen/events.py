
class _Events:

    def __init__(self, client=None):
        self.client = client

    def get_events(self, params={}, **options):
        """Get events on a resource
        [params] : {Object} Parameters for the request
        :return: list[EventResponse]
        """
        path = "/events"
        return self.client.get(path, params, **options)

