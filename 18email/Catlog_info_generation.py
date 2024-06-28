#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess

basePath = '/Users/mac_user/codes/kce-portal-catalog-infos'


def exec_command(tenantName, command):
    #进入目录/Users/mac_user/codes/kce-portal-catalog-infos/apps
    # 执行命令cd /Users/mac_user/codes/kce-portal-catalog-infos/apps
    #os.system(f'cd {basePath}/apps')
    #在目录下创建文件夹
    check_idr = f'{basePath}/apps/{tenantName}'
    if not os.path.exists(check_idr):
        result = subprocess.run(f'mkdir {check_idr}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = result.stdout, result.stderr
        print('1---', stdout, stderr)
    # 执行命令 command
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = result.stdout, result.stderr
    print('2--', stdout, stderr)
    print(f'{command} is executed!!!')


def generation_for_env(tenantName, appName, gitlabProjectId, **kwargs):
    envArray = ['dev', 'qa', 'prod']

    for env in envArray:
        command_print(appName, env, tenantName, gitlabProjectId, **kwargs)



def command_print(appName, env, tenantName, gitlabProjectId, **kwargs):
    clusterEnv = env
    appNameReal = appName
    codeProjectPath = appName
    projectName = appName
    clusterName = f'{clusterEnv}-kce-v2'
    if env == 'prod' and 'clusterName' in kwargs:
        clusterName = kwargs.get('clusterName')

    if '/' in appName:
        appNameArray = appName.split('/')
        projectName = appNameArray[0]
        appNameReal = appNameArray[1]
        if len(appNameArray) == 3:
            projectModule = appNameArray[1]
            appNameReal = appNameArray[2]
            newAppName = ''
            #appNameReal 插入 'modules'
            # 分割appName字符串
            parts = appNameReal.split('-')
            # 检查分割后的列表长度，确保至少有两个元素
            if len(parts) >= 2:
                # 拼接新的appName
                newAppName = parts[0] + '-modules-' + parts[1]

            codeProjectPath = f"{projectName}/-/tree/develop/{projectModule}/{newAppName}"
        else:
            #https://gitlab.kmcloud.kingmed.idc/llmteam/xiaoyu-cloud/-/tree/develop/xiaoyu-modules/xiaoyu-modules-file
            codeProjectPath = f"{projectName}/-/tree/develop/{appNameReal}"

    if env == 'qa':
        clusterEnv = 'test'
    command = f"sh ../../scripts/create-app.sh {appNameReal} {env} {tenantName} https://gitlab.kmcloud.kingmed.idc/{tenantName}/{codeProjectPath} {gitlabProjectId} {tenantName}/{projectName} {clusterName}"
    print(command)
    return command


if __name__ == "__main__":

    #对源码地址支持不是很友好

    #generation_for_env("llmteam", "chat-h5", "781")
    #generation_for_env("llmteam", "chat-pc", "780")
    #generation_for_env("llmteam", "km-llm-service", "728")
    #generation_for_env("llmteam", "xiaoyu-cloud/xiaoyu-auth", "798")
    #generation_for_env("llmteam", "xiaoyu-cloud/xiaoyu-file", "798")
    #generation_for_env("llmteam", "xiaoyu-cloud/xiaoyu-gateway", "798")
    #generation_for_env("llmteam", "xiaoyu-cloud/xiaoyu-modules/xiaoyu-job", "798")
    #generation_for_env("llmteam", "xiaoyu-mgr", "808")
    #generation_for_env("llmteam", "xiaoyu-cloud/xiaoyu-modules/xiaoyu-preprocess", "798")
    #generation_for_env("llmteam", "xiaoyu-cloud/xiaoyu-modules/xiaoyu-qiwei", "798")
    generation_for_env("llmteam", "xiaoyu-cloud/xiaoyu-modules/xiaoyu-system", "798", clusterName='prod-pf-v2')




