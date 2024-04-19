import copy
from .gfl_headv2 import GFLHeadV2
from .txydet_head import txydetHead


def build_head(cfg):
    head_cfg = copy.deepcopy(cfg)
    name = head_cfg.pop('name')
    if name == 'GFLHeadV2':
        return GFLHeadV2(**head_cfg)
    elif name == 'txydetHead':
        return txydetHead(**head_cfg)
    else:
        raise NotImplementedError