"""
GoogleCloudStorage extension classes for MEDIA and STATIC uploads
"""

from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage

from storages.utils import setting
from urllib.parse import urljoin
import json, os
from dotenv import load_dotenv
load_dotenv()
GS_TYPE = os.getenv("GS_TYPE")
GS_PROJECT_ID = os.getenv("GS_PROJECT_ID")
GS_PRIVATE_KEY_ID = os.getenv("GS_PRIVATE_KEY_ID")

GS_PRIVATE_KEY = os.getenv("GS_PRIVATE_KEY")

GS_CLIENT_EMAIL = os.getenv("GS_CLIENT_EMAIL")
GS_CLIENT_ID = os.getenv("GS_CLIENT_ID")
GS_AUTH_URI = os.getenv("GS_AUTH_URI")
GS_TOKEN_URI = os.getenv("GS_TOKEN_UR")
GS_AUTH_PROVIDER_X509_CERT_URL = os.getenv("GS_AUTH_PROVIDER_X509_CERT_UR")
GS_CLIENT_X509_CERT_URL = os.getenv("CLIENT_X509_CERT_URL")

# GoogleCloudStorage = {
#     "credentials": {
#         {
#   "type": GS_TYPE,
#   "project_id": GS_PROJECT_ID,
#   "private_key_id": GS_PRIVATE_KEY_ID,
#   "private_key": GS_PRIVATE_KEY,
#   "client_email": GS_CLIENT_EMAIL,
#   "client_id": GS_CLIENT_ID,
#   "auth_uri": GS_AUTH_URI,
#   "token_uri": GS_TOKEN_URI,
#   "auth_provider_x509_cert_url": GS_AUTH_PROVIDER_X509_CERT_URL,
#   "client_x509_cert_url": GS_CLIENT_X509_CERT_URL
# }

#     }
# }
class GoogleCloudMediaFileStorage(GoogleCloudStorage):
    """
    Google file storage class which gives a media file path from MEDIA_URL not google generated one.
    """

    GS_MEDIA_BUCKET_NAME = os.getenv("GS_MEDIA_BUCKET_NAME")
    
    bucket_name = GS_MEDIA_BUCKET_NAME

    def url(self, name):
        """
        Gives correct MEDIA_URL and not google generated url.
        """
        return urljoin(settings.MEDIA_URL, name)


class GoogleCloudStaticFileStorage(GoogleCloudStorage):
    """
    Google file storage class which gives a media file path from MEDIA_URL not google generated one.
    """
    GS_STATIC_BUCKET_NAME = os.getenv(" GS_STATIC_BUCKET_NAME")
   
    bucket_name = GS_STATIC_BUCKET_NAME

    def url(self, name):
       # Gives correct STATIC_URL and not google generated url.
     
        return urljoin(settings.STATIC_URL, name)