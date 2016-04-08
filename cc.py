#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from cookiecutter.main import cookiecutter

cookiecutter(
    template,
    extra_context={'timestamp': datetime.utcnow().isoformat()}
)
