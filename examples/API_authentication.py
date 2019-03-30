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

import oci


def instance_principal():
    """Gets auth details from the Instance Principal.
    http://169.254.169.254/opc/v1/identity/
    """
    print("TODO")


def api_key():
    """Gets auth details from the default path, ~/.oci/config."""
    config = oci.config.from_file()


def auth_token():
    print("TODO")


def main():
    print("TODO")
