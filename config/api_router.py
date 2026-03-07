from rest_framework.routers import DefaultRouter

from apps.api_keys.views import ApiKeyViewSet
from apps.recipients.views import RecipientViewSet
from apps.rules.views import NotificationRuleViewSet

router = DefaultRouter()

router.register("api-keys", ApiKeyViewSet, basename="api-keys")
router.register("recipients", RecipientViewSet, basename="recipients")
router.register("rules", NotificationRuleViewSet, basename="rules")

urlpatterns = router.urls
