# from rest_framework import viewsets, filters
# import django_filters.rest_framework
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rental_connects.models.booking import Advertisement, Comment
# from rental_connects.serializers.booking import AdvertisementSerializer, CommentSerializer
# from rental_connects.filters import AdvertisementFilter
#
# class AdvertisementViewSet(viewsets.ModelViewSet):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
#     filterset_class = AdvertisementFilter
#     search_fields = ["title", "description", "address__city"]
#     ordering_fields = ["price", "created_at"]
#
#     def perform_create(self, serializer):
#         serializer.save(landlord=self.request.user)
#
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
#
# from rental_connects.models.booking import RentRequest, Advertisement
# from rental_connects.models.accounts import Tenant
#
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status
#
#
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])  # Это проверит JWT токен
# def create_rent_request(request, advertisement_id):
#     print(f"Request received for advertisement_id: {advertisement_id}")
#     try:
#         advertisement = Advertisement.objects.get(id=advertisement_id)
#         tenant = Tenant.objects.get(user=request.user)
#
#         if RentRequest.objects.filter(tenant=tenant, advertisement=advertisement).exists():
#             return Response(
#                 {'status': 'error', 'message': 'Mietanfrage bereits gestellt'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         rent_request = RentRequest(tenant=tenant, advertisement=advertisement, status='pending')
#         rent_request.save()
#
#         return Response(
#             {'status': 'success', 'message': 'Mietanfrage erfolgreich gestellt'},
#             status=status.HTTP_201_CREATED
#         )
#
#     except Advertisement.DoesNotExist:
#         print(f"Advertisement {advertisement_id} not found")
#         return Response(
#             {'status': 'error', 'message': 'Anzeige nicht gefunden'},
#             status=status.HTTP_404_NOT_FOUND
#         )
#     except Tenant.DoesNotExist:
#         print(f"Tenant for user {request.user} not found")
#         return Response(
#             {'status': 'error', 'message': 'Mieter nicht gefunden'},
#             status=status.HTTP_404_NOT_FOUND
#         )
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
#
# from rental_connects.models.booking import Booking
# from rental_connects.serializers.booking import BookingSerializer
#
#
# class CreateBookingView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         serializer = BookingSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         advertisement = serializer.validated_data["advertisement"]
#         start_date = serializer.validated_data["start_date"]
#         end_date = serializer.validated_data["end_date"]
#
#
#         exists = Booking.objects.filter(
#             advertisement=advertisement,
#             start_date__lte=end_date,
#             end_date__gte=start_date,
#         ).exists()
#
#         if exists:
#             return Response(
#                 {"detail": "Apartment already booked for selected dates"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         booking = Booking.objects.create(
#             tenant=request.user,
#             advertisement=advertisement,
#             start_date=start_date,
#             end_date=end_date
#         )
#
#         return Response(
#             {"message": "Booking created successfully", "booking_id": booking.id},
#             status=status.HTTP_201_CREATED       )

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from django.shortcuts import get_object_or_404
#
# from rental_connects.models.booking import Booking, Advertisement  # поправь импорт
# from rental_connects.serializers.booking import BookingCreateSerializer
#
#
# class CreateBookingView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         serializer = BookingCreateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         booking = Booking(
#             tenant=request.user,
#             advertisement=serializer.validated_data["advertisement"],
#             start_date=serializer.validated_data["start_date"],
#             end_date=serializer.validated_data["end_date"],
#         )
#
#         try:
#             booking.save()
#         except Exception as e:
#
#             return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#
#         return Response(
#             {"message": "Booking created successfully", "booking_id": booking.id},
#             status=status.HTTP_201_CREATED
#         )
#
#
# class MyBookingsView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         qs = Booking.objects.filter(tenant=request.user).select_related("advertisement").order_by("-created_at")
#         data = [
#             {
#                 "id": b.id,
#                 "advertisement_id": b.advertisement_id,
#                 "advertisement_title": getattr(b.advertisement, "title", ""),
#                 "start_date": b.start_date,
#                 "end_date": b.end_date,
#                 "created_at": b.created_at,
#             }
#             for b in qs
#         ]
#         return Response(data, status=status.HTTP_200_OK)
#
#
# class AdvertisementBusyDatesView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, advertisement_id):
#         ad = get_object_or_404(Advertisement, pk=advertisement_id)
#         qs = Booking.objects.filter(advertisement=ad).order_by("start_date")
#
#         return Response(
#             {
#                 "advertisement_id": ad.id,
#                 "busy": [{"start_date": b.start_date, "end_date": b.end_date} for b in qs]
#             },
#             status=status.HTTP_200_OK
#         )
from rest_framework import viewsets, filters
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from rental_connects.models.booking import Advertisement, Comment, RentRequest, Booking
from rental_connects.models.accounts import Tenant, Landlord
from rental_connects.serializers.booking import AdvertisementSerializer, CommentSerializer, BookingCreateSerializer
from rental_connects.filters import AdvertisementFilter
from rest_framework.exceptions import ValidationError
from django.db.models import Avg



# class AdvertisementViewSet(viewsets.ModelViewSet):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
#     filterset_class = AdvertisementFilter
#     search_fields = ["title", "description", "address__city"]
#     ordering_fields = ["price", "created_at"]
#
#     def perform_create(self, serializer):
#         # ВАЖНО: в модели landlord = ForeignKey(Landlord)
#         landlord = Landlord.objects.get(user=self.request.user)
#         serializer.save(landlord=landlord)


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all().order_by("-created_at")
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    search_fields = ["title", "description", "address__city"]
    ordering_fields = ["price", "created_at"]

    def perform_create(self, serializer):
        try:
            landlord = Landlord.objects.get(user=self.request.user)
        except Landlord.DoesNotExist:
            raise ValidationError({
                "detail": "You are not a landlord. Call /api/accounts/become_landlord/ first."
            })

        serializer.save(landlord=landlord)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(user=self.request.user)
        avg_rating = comment.advertisement.comments.exclude(rating__isnull=True).aggregate(avg=Avg("rating"))["avg"]

        comment.advertisement.rating = avg_rating
        comment.advertisement.save(update_fields=["rating"])


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_rent_request(request, advertisement_id):
    try:
        advertisement = Advertisement.objects.get(id=advertisement_id)
        tenant = Tenant.objects.get(user=request.user)

        if RentRequest.objects.filter(tenant=tenant, advertisement=advertisement).exists():
            return Response(
                {'status': 'error', 'message': 'Mietanfrage bereits gestellt'},
                status=status.HTTP_400_BAD_REQUEST
            )

        rent_request = RentRequest(tenant=tenant, advertisement=advertisement, status='pending')
        rent_request.save()

        return Response(
            {'status': 'success', 'message': 'Mietanfrage erfolgreich gestellt'},
            status=status.HTTP_201_CREATED
        )

    except Advertisement.DoesNotExist:
        return Response(
            {'status': 'error', 'message': 'Anzeige nicht gefunden'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Tenant.DoesNotExist:
        return Response(
            {'status': 'error', 'message': 'Mieter nicht gefunden'},
            status=status.HTTP_404_NOT_FOUND
        )


class CreateBookingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BookingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        advertisement = serializer.validated_data["advertisement"]
        start_date = serializer.validated_data["start_date"]
        end_date = serializer.validated_data["end_date"]

        # overlap: existing.start < new.end AND existing.end > new.start
        exists = Booking.objects.filter(
            advertisement=advertisement,
            start_date__lt=end_date,
            end_date__gt=start_date,
        ).exists()

        if exists:
            return Response(
                {"detail": "Apartment already booked for selected dates"},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking = Booking.objects.create(
            tenant=request.user,
            advertisement=advertisement,
            start_date=start_date,
            end_date=end_date
        )

        return Response(
            {"message": "Booking created successfully", "booking_id": booking.id},
            status=status.HTTP_201_CREATED
        )


class MyBookingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Booking.objects.filter(tenant=request.user).select_related("advertisement").order_by("-created_at")
        data = [
            {
                "id": b.id,
                "advertisement_id": b.advertisement_id,
                "advertisement_title": getattr(b.advertisement, "title", ""),
                "start_date": b.start_date,
                "end_date": b.end_date,
                "created_at": b.created_at,
            }
            for b in qs
        ]
        return Response(data, status=status.HTTP_200_OK)


class AdvertisementBusyDatesView(APIView):
    permission_classes = [IsAuthenticated]  # можно IsAuthenticatedOrReadOnly

    def get(self, request, advertisement_id):
        ad = get_object_or_404(Advertisement, pk=advertisement_id)
        qs = Booking.objects.filter(advertisement=ad).order_by("start_date")

        return Response(
            {
                "advertisement_id": ad.id,
                "busy": [{"start_date": b.start_date, "end_date": b.end_date} for b in qs]
            },
            status=status.HTTP_200_OK
        )
