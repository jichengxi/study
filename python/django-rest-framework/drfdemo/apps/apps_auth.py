from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from apps.models import UserToken


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 写认证逻辑，如果正常返回两个值 user, auth
        # 如果失败，抛出异常
        token = request.GET.get('token')
        if token:
            user_token = UserToken.objects.filter(token=token).first()
            # 认证通过
            if user_token:
                return user_token.user, token
            else:
                raise AuthenticationFailed('认证失败')
        else:
            raise AuthenticationFailed('请求地址中需要携带token')


