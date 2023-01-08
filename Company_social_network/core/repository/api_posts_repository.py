from Company_social_network.api_posts.models import Post, Like


def get_all_posts_not_deleted():
    return Post.objects.filter(deleted=False)


def find_post_by_pk(pk):
    return Post.objects.filter(id=pk)


def get_post(found_post):
    return found_post.get()


def find_is_current_user_has_liked_the_post(post, user):
    return Like.objects.filter(to_post_id=post, user_id=user).first()
