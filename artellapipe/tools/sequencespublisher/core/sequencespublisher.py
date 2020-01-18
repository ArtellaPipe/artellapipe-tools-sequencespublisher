#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains sequences publisher implementation for Artella
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe


class SequencesPublisher(artellapipe.Tool, object):

    def __init__(self, project, config):
        super(SequencesPublisher, self).__init__(project=project, config=config)
