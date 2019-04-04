import examples_auth_and_logging


# For a full list of clients -
# https://github.com/oracle/oci-python-sdk/blob/master/docs/api/landing.rst

def create_clients(config, **kwargs):
    announcement_client = oci.announcements_service.AnnouncementClient(config)
    audit_client = oci.audit.AuditClient(config)
    auto_scaling_client = oci.autoscaling.AutoScalingClient(config)
    block_storage_client = oci.core.BlockstorageClient(config)
    budget_client = oci.budget.BudgetClient(config)
    compute_client = oci.core.ComputeClient(config)
    compute_management_client = oci.core.ComputeManagementClient(config)
    container_engine_client = oci.container_engine.ContainerEngineClient(config)
    database_client = oci.database.DatabaseClient(config)
    dns_client = oci.dns.DnsClient(config)
    email_client = oci.email.EmailClient(config)
    file_storage_client = oci.file_storage.FileStorageClient(config)
    health_checks_client = oci.healthchecks.HealthChecksClient(config)
    identity_client = oci.identity.IdentityClient(config)
    kms_crypto_client = oci.key_management.KmsCryptoClient(config)
    kms_management_client = oci.key_management.KmsManagementClient(config)
    kms_vault_client = oci.key_management.KmsVaultClient(config)
    load_balancer_client = oci.load_balancer.LoadBalancerClient(config)
    monitoring_client = oci.monitoring.MonitoringClient(config)
    notification_control_plane_client = oci.ons.NotificationControlPlaneClient(config)
    notification_data_plane_client = oci.ons.NotificationDataPlaneClient(config)
    object_storage_client = oci.object_storage.ObjectStorageClient(config)
    resource_search_client = oci.resource_search.ResourceSearchClient(config)
    stream_admin_client = oci.streaming.StreamAdminClient(config)
    stream_client = oci.streaming.StreamClient(config)
    virtual_network_client = oci.core.VirtualNetworkClient(config)
    waas_client = oci.waas.WaasClient(config)
