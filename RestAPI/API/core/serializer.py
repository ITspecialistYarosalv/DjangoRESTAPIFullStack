from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Advocate, Companies


class CompanySerializer(ModelSerializer):
    employe_count = SerializerMethodField(read_only=True)
    class Meta:
        model = Companies
        fields = '__all__'

    def get_employe_count(self,obj):
        count = obj.advocate_set.count()
        return count


class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Advocate
        fields = ("username","bio","company")
