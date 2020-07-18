from django import template
from django.contrib.auth.models import User
from django.db.models import Count, Q
from pytils.translit import slugify

from ..models import Profile, Post

register = template.Library()


# Вообще, это ласт-реги, но надо будет сделать куррент онлайн
@register.inclusion_tag('core/include/sidebar_for_users.html')
def show_users_online(count=5):
    users_online = User.objects.filter(is_active=True).order_by('-date_joined')[:count]
    return {'users_online': users_online}


@register.inclusion_tag('core/include/sidebar_for_likes.html')
def show_post_with_top_likes(count=5):
    posts = Post.objects.annotate(like_count=Count('votes', filter=Q(votes__vote__gt=0))).annotate(
        dislike_count=Count('votes', filter=Q(votes__vote__lt=0))).filter(created__year=2020).order_by('-like_count')[:count]
    # posts = LikeDislike.objects.filter(content_type=ContentType.objects.get_for_model(Post))
    # liked_posts = posts.likes()
    return {'liked_posts': posts}


@register.simple_tag()
def create_profile(user):
    profile = Profile(name=user, slug=slugify(user.username))
    profile.save()
    return ''
