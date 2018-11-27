#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Copyright (C) Software Competence Center Hagenberg GmbH (SCCH)
# All rights reserved.
# -----------------------------------------------------------------------------
# This document contains proprietary information belonging to SCCH.
# Passing on and copying of this document, use and communication of its
# contents is not permitted without prior written authorization.
# -----------------------------------------------------------------------------
# Created on : 17.09.2018 $
# by : fischer $

# --- imports -----------------------------------------------------------------
from configs.config import ConfigFlags


def load_config():
    config = ConfigFlags().return_flags()

    # Directories
    config.data_dir = ''

    # Model to train
    config.model_name = 'DeepSNP_V1'

    # Data generation parameters
    config.jitter = True

    # Training parameters
    # all default

    # Architecture specific parameters
    config.use_input_attention = True
    config.use_output_attention = True

    # Evaluation parameters
    # only used for evaluation

    return config