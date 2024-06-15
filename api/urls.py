from django.urls import path

from .views import PostView, ImageView, AttachmentView, CommentView, UserView, CustomizationView, TagView, ArticleView, ArticleCommentView, PortalView

urlpatterns = [
    #post
    path('posts-count', PostView.as_view({'get': 'count'})),
    path('posts/loadedItems=<int:loadedCount>/limit=<int:limit>', PostView.as_view({'get': 'list'})),
    path('post/<int:post_id>', PostView.as_view({'get': 'retrieve'})),
    path('get-post-supplements/<int:post_id>', PostView.as_view({'get': 'post_supplements_list'})),
    path('get-new-post', PostView.as_view({'get': 'get_new_post'})),
    path('set-new-post-text/<int:post_id>', PostView.as_view({'post': 'set_text'})),
    path('add-new-post', PostView.as_view({'post': 'create'})),
    path('delete-post', PostView.as_view({'post': 'delete'})),
    path('change-post-col/<int:post_id>', PostView.as_view({'post': 'edit_post_col'})),
    #image
    path('add-image', ImageView.as_view({'post': 'add_image'})),
    path('delete-image', ImageView.as_view({'post': 'delete'})),
    #attachment
    path('add-attachment', AttachmentView.as_view({'post': 'create'})),
    path('delete-attachment', AttachmentView.as_view({'post': 'delete'})),
    #comment
    path('comments/<int:post_id>/<int:loadedItemsCount>', CommentView.as_view({'get': 'list'})),
    path('add-comment', CommentView.as_view({'post': 'create'})),
    path('comments-count/<int:post_id>', CommentView.as_view({'get': 'count'})),
    path('delete-comment', CommentView.as_view({'post': 'delete'})),
    #user
    path('users-count', UserView.as_view({'get': 'count'})),
    path('login-or-registration', UserView.as_view({'post': 'login_or_registration'})),
    path('profile-registration', UserView.as_view({'post': 'profile_create'})),
    path('get-user', UserView.as_view({'get': 'retrieve'})),
    path('users', UserView.as_view({'post': 'search_list'})),
    path('users/<int:total_count>', UserView.as_view({'get': 'user_list'})),
    path('user-block', UserView.as_view({'post': 'block'})),
    #path('is-logged-in', UserView.as_view({'get': 'is_login'})),
    #path('is-admin', UserView.as_view({'get': 'is_admin'})),
    path('change-name', UserView.as_view({'post': 'change_name'})),
    path('change-email', UserView.as_view({'post': 'change_email'})),
    path('logout', UserView.as_view({'post': 'logout'})),
    #customization
    path('profile-info', CustomizationView.as_view({'get': 'profile_info'})),
    path('profile-about', CustomizationView.as_view({'get': 'profile_about'})),
    path('profile-contacts', CustomizationView.as_view({'get': 'profile_contacts'})),
    path('privacy-settings-data', CustomizationView.as_view({'get': 'privacy_settings_data'})),
    path('rules-settings-data', CustomizationView.as_view({'get': 'rules_settings_data'})),
    path('subscribe-permission-settings-data', CustomizationView.as_view({'get': 'sibscribe_permission_settings_data'})),
    path('styles', CustomizationView.as_view({'get': 'styles'})),
    path('edit-item', CustomizationView.as_view({'post': 'edit_item'})),
    path('edit-file-item', CustomizationView.as_view({'post': 'edit_file_item'})),
    path('get-need-to-enter-value', CustomizationView.as_view({'get': 'privacy_settings_data'})),
    #настройки для данных профиля
    path('edit-name', CustomizationView.as_view({'post': 'edit_name'})),
    path('edit-avatar', CustomizationView.as_view({'post': 'edit_avatar'})),
    path('edit-city', CustomizationView.as_view({'post': 'edit_city'})),
    path('edit-email', CustomizationView.as_view({'post': 'edit_email'})),
    path('edit-status', CustomizationView.as_view({'post': 'edit_status'})),
    #теги
    path('add-tag', TagView.as_view({'post': 'create'})),
    path('edit-tag', TagView.as_view({'post': 'edit'})),
    path('delete-tag', TagView.as_view({'post': 'delete'})),
    path('get-tags', TagView.as_view({'get': 'list'})),
    #статьи
    path('add-article', ArticleView.as_view({'post': 'create'})),
    path('get-article/<int:id>', ArticleView.as_view({'get': 'retrieve'})),
    path('get-articles', ArticleView.as_view({'post': 'list'})),
    path('articles-count', ArticleView.as_view({'post': 'count'})),
    path('edit-article/<int:id>', ArticleView.as_view({'post': 'edit'})),
    path('delete-article', ArticleView.as_view({'post': 'delete'})),
    #комментарии статей
    path('article-comments/<int:article_id>/<int:loadedItemsCount>', ArticleCommentView.as_view({'get': 'list'})),
    path('article-comments-count/<int:article_id>', ArticleCommentView.as_view({'get': 'count'})),
    path('add-article-comment', ArticleCommentView.as_view({'post': 'create'})),
    path('delete-article-comment', ArticleCommentView.as_view({'post': 'delete'})),
    #связь с другими ресурсами
    path('get-subscribes', PortalView.as_view({'get': 'base_data'})),
    path('add-subscribe', PortalView.as_view({'post': 'create'})),
    path('unsubscribe', PortalView.as_view({'post': 'delete'})),
]