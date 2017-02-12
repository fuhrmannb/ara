#   Copyright 2017 Red Hat, Inc. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

from ara import models


def configure_context_processors(app):

    @app.context_processor
    def ctx_add_nav_data():
        '''Makes some standard data from the database available in the
        template context.'''

        playbook_item_limit = app.config.get('NAV_MENU_MAX_PLAYBOOKS', 10)
        host_item_limit = app.config.get('NAV_MENU_MAX_HOSTS', 10)

        return dict(hosts=models.Host.query
                    .order_by(models.Host.name)
                    .limit(host_item_limit),
                    playbooks=models.Playbook.query
                    .order_by(models.Playbook.time_start.desc())
                    .limit(playbook_item_limit))
