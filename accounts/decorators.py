from django.shortcuts import redirect


def allowed_roles(roles=[]):

    def decorator(view_func):

        def wrapper(
            request,
            *args,
            **kwargs
        ):

            role = (
                request.user
                .userprofile
                .role
            )

            if role in roles:

                return view_func(
                    request,
                    *args,
                    **kwargs
                )

            return redirect(
                'login'
            )

        return wrapper

    return decorator
