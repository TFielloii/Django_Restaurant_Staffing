from django.shortcuts import redirect
from django.contrib import messages

def user_not_authenticated(function=None, redirect_url='login'):
    
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # If user is already authenticated, redirect to the specified url
            if request.user.is_authenticated:
                return redirect(redirect_url)
            # If user is not authenticated, proceed with the view
            return view_func(request, *args, **kwargs)
        return _wrapped_view

    # If the decorator is used with a function, returns the decorated function
    if function:
        return decorator(function)
    return decorator