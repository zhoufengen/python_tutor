#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
#2024-05-29 14:03:26.294 [ESC-IDM] [] [INFO] [main] [o.s.c.s.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [335] >>> Bean 'org.springframework.integration.config.IntegrationManagementConfiguration' of type [org.springframework.integration.config.IntegrationManagementConfiguration] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)
logRe = re.compile(r'^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}\.\d{3})(\s+\[\w*\])*$')
#读取日志文件
with open('reg-test-log.txt', 'r') as f:
    for line in f.readlines():
        logReMatch = logRe.match(line)
        logReMatch.groups()






