###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2011, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

from Products.ZenRelations.RelSchema import ToManyCont, ToOne

from ZenPacks.zenoss.CloudStack.utils import BaseComponent


class Host(BaseComponent):
    meta_type = portal_type = "Host"

    host_type = None
    host_state = None
    host_events = None
    host_version = None
    hypervisor = None
    capabilities = None
    created = None
    hosttags = None
    ip_address = None
    local_storage_active = None
    management_server_id = None

    _properties = BaseComponent._properties + (
        {'id': 'host_type', 'type': 'string', 'mode': ''},
        {'id': 'host_state', 'type': 'string', 'mode': ''},
        {'id': 'host_events', 'type': 'string', 'mode': ''},
        {'id': 'host_version', 'type': 'string', 'mode': ''},
        {'id': 'hypervisor', 'type': 'string', 'mode': ''},
        {'id': 'capabilities', 'type': 'string', 'mode': ''},
        {'id': 'created', 'type': 'string', 'mode': ''},
        {'id': 'hosttags', 'type': 'string', 'mode': ''},
        {'id': 'ip_address', 'type': 'string', 'mode': ''},
        {'id': 'local_storage_active', 'type': 'boolean', 'mode': ''},
        {'id': 'management_server_id', 'type': 'int', 'mode': ''},
        )

    _relations = BaseComponent._relations + (
        ('cluster', ToOne(ToManyCont,
            'ZenPacks.zenoss.CloudStack.Cluster.Cluster',
            'hosts')
            ),
        )

    def device(self):
        return self.cluster().device()