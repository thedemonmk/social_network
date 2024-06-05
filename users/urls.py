from django.urls import path
from .views import SignupView, LoginView, UserSearchView, FriendRequestView, FriendListView, PendingFriendRequestsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserSearchView.as_view(), name='user_search'),
    path('friend-request/<int:user_id>/', FriendRequestView.as_view(), name='friend_request'),
    path('friend-request/<int:request_id>/action/', FriendRequestView.as_view(), name='friend_request_action'),
    path('friends/', FriendListView.as_view(), name='friends_list'),
    path('friend-requests/', PendingFriendRequestsView.as_view(), name='pending_friend_requests'),
]