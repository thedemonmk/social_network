from django.db import models

class SocialUser(models.Model):
    email = models.EmailField(unique=True)
    user = models.ForeignKey('auth.User', related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)



class FriendRequest(models.Model):
    from_user = models.ForeignKey(SocialUser, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(SocialUser, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')