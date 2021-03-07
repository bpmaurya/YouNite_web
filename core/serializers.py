from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db.models import fields


from rest_framework import serializers
from rest_framework.fields import NOT_READ_ONLY_WRITE_ONLY




class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True,required=False)
    # username = serializers.CharField(read_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self,instance,validate_data):
        try:
            user = instance
            password= validate_data.pop('password')
            old_password = validate_data.pop('old_password')
            if user.check_password(old_password):
                user.set_password(password)
            else:
                raise Exception("Old password is Incorrect")
            user.save()

        except Exception as err:
            raise serializers.ValidationError(err)

        return super(UserSerializer,self).update(instance,validated_data)




    class Meta:
        model = User 
        fields=['url','id','username','email','first_name','last_name','password']
