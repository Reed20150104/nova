# Copyright 2011 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Disk Config extension."""

from webob import exc

from nova.api.openstack import extensions
from nova.i18n import _

ALIAS = 'os-disk-config'
API_DISK_CONFIG = "OS-DCF:diskConfig"
INTERNAL_DISK_CONFIG = "auto_disk_config"
authorize = extensions.os_compute_soft_authorizer(ALIAS)


def disk_config_to_api(value):
    return 'AUTO' if value else 'MANUAL'


def disk_config_from_api(value):
    if value == 'AUTO':
        return True
    elif value == 'MANUAL':
        return False
    else:
        msg = _("%s must be either 'MANUAL' or 'AUTO'.") % API_DISK_CONFIG
        raise exc.HTTPBadRequest(explanation=msg)


class DiskConfig(extensions.V21APIExtensionBase):
    """Disk Management Extension."""

    name = "DiskConfig"
    alias = ALIAS
    version = 1

    def get_controller_extensions(self):
        return []

    def get_resources(self):
        return []
