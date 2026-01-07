# from rest_framework import serializers
# from rental_connects.models.booking import Advertisement, Comment, Booking
# from rental_connects.serializers.address import AddressSerializer
# from rental_connects.models.address import Address
#
#
#
# class AdvertisementSerializer(serializers.ModelSerializer):
#     address = AddressSerializer()
#     images = serializers.ImageField(required=False)
#
#     class Meta:
#         model = Advertisement
#         fields = ["id", "title", "type_of_property", "description", "price", "area", "number_of_rooms", "number_of_floors", "address", "images", "created_at", "updated_at"]
#         read_only_fields = ["id", "created_at", "updated_at", "deleted_at"]
#
#     def create(self, validated_data):
#         address_data = validated_data.pop('address')
#         address = Address.objects.create(**address_data)
#         advertisement = Advertisement.objects.create(address=address, **validated_data)
#         return advertisement
#
#
# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = [
#             "id",
#             "advertisement",
#             "start_date",
#             "end_date",
#         ]
#
#
# class BookingCreateSerializer(serializers.ModelSerializer):
#     advertisement = serializers.PrimaryKeyRelatedField(queryset=Advertisement.objects.all())
#
#     class Meta:
#         model = Booking
#         fields = ("id", "advertisement", "start_date", "end_date")
#
#     def validate(self, attrs):
#         if attrs["start_date"] >= attrs["end_date"]:
#             raise serializers.ValidationError({"end_date": "end_date must be after start_date"})
#         return attrs
#
#
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = "__all__"
#         read_only_fields = ["id", "created_at", "updated_at"]


from rest_framework import serializers
from rental_connects.models.booking import Advertisement, Comment, Booking
from rental_connects.serializers.address import AddressSerializer
from rental_connects.models.address import Address


class AdvertisementSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    images = serializers.ImageField(required=False)

    class Meta:
        model = Advertisement
        fields = [
            "id", "title", "type_of_property", "description", "price", "area",
            "number_of_rooms", "number_of_floors", "address", "images",
            "created_at", "updated_at"
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        advertisement = Advertisement.objects.create(address=address, **validated_data)
        return advertisement


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "advertisement", "start_date", "end_date", "created_at"]
        read_only_fields = ["id", "created_at"]


class BookingCreateSerializer(serializers.ModelSerializer):
    advertisement = serializers.PrimaryKeyRelatedField(queryset=Advertisement.objects.all())

    class Meta:
        model = Booking
        fields = ("id", "advertisement", "start_date", "end_date")

    def validate(self, attrs):
        if attrs["start_date"] >= attrs["end_date"]:
            raise serializers.ValidationError({"end_date": "end_date must be after start_date"})
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # безопасно: user не даём передавать из клиента
        fields = ["id", "advertisement", "text", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
