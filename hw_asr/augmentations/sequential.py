from typing import List, Callable

from torch import Tensor

from hw_asr.augmentations.base import AugmentationBase
import random


class SequentialAugmentation(AugmentationBase):
    def __init__(self, augmentation_list: List[Callable]):
        self.augmentation_list = augmentation_list

    def __call__(self, data: Tensor) -> Tensor:
        x = data
        for augmentation in self.augmentation_list:
            x = augmentation(x)
        return x
    
# my own
class SequentialRandomApplyAugmentation(AugmentationBase):
    def __init__(self, augmentation_list: List[Callable], augmentation_apply_probability: float=1):
        self.augmentation_list = augmentation_list
        self.augmentation_apply_probability = augmentation_apply_probability

    def __call__(self, data: Tensor) -> Tensor:
        x = data
        for augmentation in self.augmentation_list:
            if random.random() > self.augmentation_apply_probability:
                x = augmentation(x)
        return x
