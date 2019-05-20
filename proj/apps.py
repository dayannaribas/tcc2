from django.apps import AppConfig
from auditlog.apps import AuditlogConfig


class CoreConfig(AppConfig):
    name = 'proj'


class AuditlogCustomConfig(AuditlogConfig):
    verbose_name = 'Auditing'
