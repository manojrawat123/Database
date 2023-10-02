from rest_framework import serializers
from myuser.models import MyUser

class MyUserSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"}, write_only = True)
    class Meta:
        model = MyUser
        fields = "__all__"
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("Password Didn't match")
        return attrs
    
    def create(self, validate_data):
        validate_data.pop('password2')
        return MyUser.objects.create_user(**validate_data)
    

class MyUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"  

    
class MyUserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 225)
    class Meta:
        model = MyUser
        fields = ["email", "password"]

    def validate(self, data):
        for field_name, value in data.items():
            if value == "":
                raise serializers.ValidationError(f"{field_name} field is required.")
        return data

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = MyUser
    fields = ["id","email","name", "phone"]
    