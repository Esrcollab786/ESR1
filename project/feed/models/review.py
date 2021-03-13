from django.utils import timezone
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from project.feed.models import Restaurant
from project.feed.models.offer import Offer


class Review(models.Model):

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    offer =  models.ForeignKey(Offer, on_delete=models.CASCADE,)
    comment = models.TextField(null=True, blank=True)
    rating_taste = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    rating_ambiance = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    rating_service = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    rating_overall = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']
        unique_together = [(
             'user_id', 'restaurant_id'
        )]
