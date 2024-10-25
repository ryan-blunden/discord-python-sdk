from .types import BeforeRequestHook


class AuthHeaderHook(BeforeRequestHook):
    def before_request(self, hook_ctx, request):
        # Assuming hook_ctx.oAuth2Scopes and request.headers follow the same interface pattern
        if (
            hasattr(hook_ctx, "oAuth2Scopes")
            and hook_ctx.oauth2_scopes
            and len(hook_ctx.oauth2_scopes) > 0
        ):
            return request

        auth_token = request.headers.get("Authorization")
        if auth_token and "Bot" not in auth_token:
            request.headers["Authorization"] = f"Bot {auth_token}"

        return request
