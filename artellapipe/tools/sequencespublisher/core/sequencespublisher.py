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

from tpQtLib.widgets import stack

import artellapipe


class SequencesPublisher(artellapipe.PyblishTool, object):

    def __init__(self, project, config):
        super(SequencesPublisher, self).__init__(project=project, config=config)

    def ui(self):
        super(SequencesPublisher, self).ui()

        self._stack = stack.SlidingStackedWidget()
        self.main_layout.addWidget(self._stack)

        self._sequences_viewer = artellapipe.SequencesViewer(project=self._project)
        self._stack.addWidget(self._sequences_viewer)

    def post_attacher_set(self):
        super(SequencesPublisher, self).post_attacher_set()

        self._stack.addWidget(self._pyblish_window)
