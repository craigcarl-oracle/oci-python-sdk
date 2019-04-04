# OCI supports multiple methods for programmatic authentication.
# These SDK examples default to an Instance Principal and fallback to an API key.
#
# API keys - https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm
# API keys and related details are generally stored in ~/.oci/config.
#
# Instance Principals - https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm
# If your tool will be executed on an OCI instance you should use an Instance Principal.
#
# Auth Token - https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/clitoken.htm
# Tokens are primarily used when the user account is federated with OCI.
#
# Customer Secret Keys - https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#s3
# Used for authenticating against the OCI Object Storage S3 compatible API. See the Object Storage examples.

import sys
import logging
import requests

import oci

logger = logging.getLogger(__name__)


def configure_logging(loglevel):
    """Configures the logger."""

    loglevel = getattr(logging, loglevel.upper(), None)
    if not isinstance(loglevel, int):
        raise ValueError('Invalid log level: {}.').format(loglevel)
    logging.getLogger('__name__')
    logging.basicConfig(level=loglevel, style='{')  # , format=form)
    return logging


def get_instance_principal():
    """Gets authentication details from the Instance Principal."""
    config = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
    return config


def get_api_key():
    """Gets authentication details from the default path, ~/.oci/config."""
    config = oci.config.from_file()
    return config


def auth_token():
    print("TODO")
    config = False
    return config


def test_auth():
    """Tests for valid authorization details.

    Any authenticated user has permissions to get the Object Storage Namespace name.
    We can use this to test Instance Principals and API keys.
    """
    print(object_storage_client.get_namespace().data)


def main():
    assert sys.version_info >= (3, 5)
    # The SDK will use this loglevel.
    configure_logging('INFO')

    try:
        # Test to see if we're running on an OCI instance.
        r = requests.get("http://169.254.169.254/opc/v1/identity/")
        r.raise_for_status()
    except (requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError):
        logger.info("Can't access the OCI metadata service. Trying API "
                    "key auth.")
        auth = get_api_key()
