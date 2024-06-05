from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FriendRequest, SocialUser
from .serializers import UserSerializer, FriendRequestSerializer
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

class SignupView(generics.CreateAPIView):
    queryset = SocialUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['email'] = data['email'].lower()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email').lower()
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            return Response(UserSerializer(user).data)
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class UserSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = request.GET.get('q', '')
        users = SocialUser.objects.filter(Q(email__iexact=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
        paginator = Paginator(users, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        serializer = UserSerializer(page, many=True)
        return Response(serializer.data)

class FriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        to_user = SocialUser.objects.get(id=user_id)
        friend_request, created = FriendRequest.objects.get_or_create(from_user=request.user, to_user=to_user)
        if not created:
            return Response({"message": "Friend request already sent."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(FriendRequestSerializer(friend_request).data, status=status.HTTP_201_CREATED)

    def put(self, request, request_id):
        friend_request = FriendRequest.objects.get(id=request_id)
        action = request.data.get('action')
        if action == 'accept':
            friend_request.status = 'accepted'
        elif action == 'reject':
            friend_request.status = 'rejected'
        friend_request.save()
        return Response(FriendRequestSerializer(friend_request).data)

class FriendListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        friends = SocialUser.objects.filter(Q(sent_requests__to_user=request.user, sent_requests__status='accepted') |
                                      Q(received_requests__from_user=request.user, received_requests__status='accepted'))
        serializer = UserSerializer(friends, many=True)
        return Response(serializer.data)

class PendingFriendRequestsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pending_requests = FriendRequest.objects.filter(to_user=request.user, status='pending')
        serializer = FriendRequestSerializer(pending_requests, many=True)
        return Response(serializer.data)

def homepage(request):
    api_endpoints = {
        'Signup': reverse('signup'),
        'Login': reverse('login'),
        'User Search': reverse('user_search'),
        'Send Friend Request': reverse('friend_request', kwargs={'user_id': 1}),
        'Friend Request Action': reverse('friend_request_action', kwargs={'request_id': 1}),
        'Friends List': reverse('friends_list'),
        'Pending Friend Requests': reverse('pending_friend_requests'),
    }
    return render(request, 'homepage.html', {'api_endpoints': api_endpoints})