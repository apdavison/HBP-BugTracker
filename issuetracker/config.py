import os
import hbp_app_python_auth.settings as auth_settings

auth_settings.SOCIAL_AUTH_HBP_KEY = os.environ.get("HBP_OIDC_CLIENT_ID")
auth_settings.SOCIAL_AUTH_HBP_SECRET = os.environ.get("HBP_OIDC_CLIENT_SECRET")