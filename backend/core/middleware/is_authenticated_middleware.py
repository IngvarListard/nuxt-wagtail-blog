class IsUserAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.set_cookie(
            'isLoggedIn',
            request.user.is_authenticated,
            expires=request.session.get_expiry_date(),
            max_age=request.session.get_expiry_age(),
        )
        return response
