from datetime import datetime


class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("---------------------------------")
        print("Time :", datetime.now().strftime("%Y-%m-%d %I:%M %p"))
        print("Method :", request.method)
        print("Path :", request.path)
        print("---------------------------------")

        response = self.get_response(request)
        return response