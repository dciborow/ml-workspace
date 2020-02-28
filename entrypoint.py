#!/usr/bin/env python3

from plumbum import local
import os

from azure_utils.machine_learning.utils import get_or_create_workspace_from_project

def debug(message: str):
    print(f'##[debug]{message}')


def run():
    projectyml = os.path.join(local.env.get('HOME', ''), 'project.yml')
    subscription_id = local.env.get('subscription_id')
    resource_group = local.env.get('resource_group')
    workspace_name = local.env.get('workspace_name')
    workspace_region = local.env.get('workspace_region')
   
    proj_config = ProjectConfiguration(projectyml)
    proj_config.add_setting("subscription_id", "Your Azure Subscription", subscription_id)
    proj_config.add_setting("resource_group", "Azure Resource Group Name", resource_group)
    proj_config.add_setting("workspace_name", "Azure ML Workspace Name", workspace_name)
    proj_config.add_setting("workspace_region", "Azure ML Workspace Region", workspace_region)

    debug(get_or_create_workspace_from_project(proj_config))

if __name__ == '__main__':
    run()
