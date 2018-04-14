from tastypie.api import Api
from .resources import UserResource
from .resources import GualetResource
from .resources import TransactionResource


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(GualetResource())
v1_api.register(TransactionResource())
