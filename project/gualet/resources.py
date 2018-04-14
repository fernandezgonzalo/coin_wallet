from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.constants import ALL
from tastypie import fields
from tastypie.authorization import Authorization

from gualet.models import User
from gualet.models import Gualet
from gualet.models import Transaction


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        filtering = {
            'username': ALL,
        }
        authorization = Authorization()

    def obj_create(self, bundle, request=None, **kwargs):
        try:
            bundle = super(UserResource, self).obj_create(bundle)
            bundle.obj.set_password(bundle.data.get('password'))
            bundle.obj.save()
        except IntegrityError:
            raise BadRequest('Username already exists')

        return bundle


class GualetResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)

    class Meta:
        queryset = Gualet.objects.all()
        resource_name = 'gualets'
        filtering = {
            'user': ALL_WITH_RELATIONS,
        }
        authorization = Authorization()


class TransactionResource(ModelResource):
    address_from = fields.ForeignKey(GualetResource, 'address_from', full=True)
    address_to = fields.ForeignKey(GualetResource, 'address_to', full=True)

    class Meta:
        queryset = Transaction.objects.all()
        resource_name = 'transactions'
        authorization = Authorization()
        filtering = {
            'address_from': ALL_WITH_RELATIONS,
            'address_to': ALL_WITH_RELATIONS,
        }
