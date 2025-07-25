from __future__ import absolute_import, print_function
import numpy as np
from lib.test.evaluation.data import Sequence, BaseDataset, SequenceList
from lib.test.utils.load_text import load_text
import glob
import json
import numpy as np
import os
import six


class VideoCube(BaseDataset):
    r"""`VideoCube <http://videocube.aitestunion.com>`_ Dataset.

    Publication:
        ``Global Instance Tracking: Locating Target More Like Humans.``,S. Hu, X. Zhao*, L. Huang and K. Huang (*corresponding author)
        IEEE Transactions on Pattern Analysis and Machine Intelligence, DOI:10.1109/TPAMI.2022.3153312

    Args:
        root_dir (string): Root directory of dataset where ``train``,
            ``val`` and ``test`` folders exist.
        subset (string, optional): Specify ``train``, ``val`` or ``test``
            subset of VideoCube.
    """

    def __init__(self):
        super().__init__()
        self.base_path = self.env_settings.git_path
        self.sequence_list = self._get_sequence_list()

    def get_sequence_list(self):
        return SequenceList([self._construct_sequence(s) for s in self.sequence_list])

    def _construct_sequence(self, sequence_name):

        anno_path = '{}/attribute/groundtruth/{}.txt'.format(self.base_path, sequence_name)

        ground_truth_rect = load_text(str(anno_path), delimiter=',', dtype=np.float64)


        # NOTE: pandas backed seems super super slow for loading occlusion/oov masks


        frames_path = '{}/{}/{}'.format(self.base_path, sequence_name, 'frame_'+ sequence_name)

        frames_list = ['{}/{:06d}.jpg'.format(frames_path, frame_number) for frame_number in
                       range(0, ground_truth_rect.shape[0])]

        return Sequence(sequence_name, frames_list, 'git', ground_truth_rect.reshape(-1, 4),
                        )

    def __len__(self):
        return len(self.sequence_list)

    def _get_sequence_list(self):
        sequence_list = ["001",
            "006",
            "007",
            "012",
            "022",
            "038",
            "045",
            "061",
            "074",
            "079",
            "087",
            "089",
            "093",
            "107",
            "111",
            "114",
            "117",
            "148",
            "181",
            "230",
            "255",
            "275",
            "277",
            "286",
            "311",
            "366",
            "418",
            "449",
            "469",
            "498"]

        return sequence_list
