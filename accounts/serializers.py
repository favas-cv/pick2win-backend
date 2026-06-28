from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from accounts.models import User
from clubs.models import Club,ClubInvite,Club_member
from django.db import transaction

class RegisterSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    token = serializers.CharField()
    class Meta:
        model = User
        fields = (
            "name",
            "phone",
            "password1",
            "password2",
            "token"
        )

    def validate(self, attrs):

        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError(
                "Passwords do not match"
            )

        # validate_password(attrs["password1"])
        
        token = attrs.get("token")
        
        invite = ClubInvite.objects.filter(
            token = token, 
            is_active = True
        ).first()
        
        if not invite:
            raise serializers.ValidationError(
                {"token":"invlaid or expired invite link"}
            )
            
        attrs['invite'] =invite

        return attrs


    def create(self, validated_data):
        with transaction.atomic():
            invite = validated_data.pop("invite")
            validated_data.pop("token")
            validated_data.pop("password2")

            password = validated_data.pop("password1")
            phone = validated_data["phone"]

            user = User.objects.create_user(
                username=phone,
                password=password,
                **validated_data
            )

            Club_member.objects.create(
                user=user,
                club=invite.club,
                role="member"
            )

            return user
        
        
from django.db import transaction
from rest_framework import serializers

from accounts.models import User
from clubs.models import Club, Club_member


class ClubRegisterSerializer(serializers.Serializer):

    # User Details
    name = serializers.CharField(max_length=60)
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    # Club Details
    club_name = serializers.CharField(max_length=50)
    slug = serializers.SlugField()
    place = serializers.CharField(max_length=50)
    description = serializers.CharField()

    def validate(self, attrs):

        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Passwords do not match."}
            )

        if User.objects.filter(phone=attrs["phone"]).exists():
            raise serializers.ValidationError(
                {"phone": "Phone number already exists."}
            )

        if Club.objects.filter(slug=attrs["slug"]).exists():
            raise serializers.ValidationError(
                {"slug": "Slug already exists."}
            )

        return attrs

    @transaction.atomic
    def create(self, validated_data):

        validated_data.pop("password2")

        password = validated_data.pop("password")

        club_name = validated_data.pop("club_name")
        slug = validated_data.pop("slug")
        place = validated_data.pop("place")
        description = validated_data.pop("description")

        phone = validated_data.pop("phone")

        user = User.objects.create_user(
            username=phone,
            phone=phone,
            password=password,
            role="club_admin",
            **validated_data
        )

        club = Club.objects.create(
            owner=user,
            name=club_name,
            slug=slug,
            place=place,
            description=description,
        )

        Club_member.objects.create(
            club=club,
            user=user,
            role="club_admin"
        )

        return club
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "slug": instance.slug,
            "place": instance.place,
            "description": instance.description,
        }
    
    
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    club = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "phone",
            "role",
            "total_points",
            "club",
        ]

    def get_club(self, obj):
        membership = (
            Club_member.objects
            .select_related("club")
            .filter(user=obj)
            .first()
        )

        if not membership:
            return None

        return {
            "id": membership.club.id,
            "name": membership.club.name,
            "place": membership.club.place,
            "description": membership.club.description,
            "slug": membership.club.slug,
            "member_role": membership.role,
            "joined_at": membership.joined_at,
        }