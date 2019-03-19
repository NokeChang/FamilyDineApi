from django.utils.deprecation import MiddlewareMixin


class TestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print("process_request of middleware")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("process_view of middleware")

    def process_response(self, request, response):
        print("process_response of middleware")
        return response
