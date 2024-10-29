import numpy as np
from lib.test.evaluation.data import Sequence, BaseDataset, SequenceList
from lib.test.utils.load_text import load_text


class TLPDataset(BaseDataset):

    def __init__(self):
        super().__init__()
        self.base_path = self.env_settings.tlp_path
        self.sequence_list = self._get_sequence_list()
        self.clean_list = self.clean_seq_list()

    def clean_seq_list(self):
        clean_lst = []
        for i in range(len(self.sequence_list)):
            cls= self.sequence_list[i].split('-')
            clean_lst.append(cls)
        return  clean_lst

    def get_sequence_list(self):
        return SequenceList([self._construct_sequence(s) for s in self.sequence_list])

    def _construct_sequence(self, sequence_name):
        class_name = sequence_name.split('-')[0]
        anno_path = '{}/{}/groundtruth_rect.txt'.format(self.base_path,  sequence_name)

        ground_truth_rect = load_text(str(anno_path), delimiter=',', dtype=np.float64)[:, 1:5]

        target_visible = (load_text(str(anno_path), delimiter=',', dtype=np.float64)[:, -1]==0)

        frames_path = '{}/{}/img'.format(self.base_path, sequence_name)

        frames_list = ['{}/{:05d}.jpg'.format(frames_path, frame_number) for frame_number in range(1, ground_truth_rect.shape[0] + 1)]

        target_class = class_name
        return Sequence(sequence_name, frames_list, 'tlp', ground_truth_rect.reshape(-1, 4),
                        object_class=target_class, target_visible=target_visible)

    def __len__(self):
        return len(self.sequence_list)

    def _get_sequence_list(self):
        sequence_list = ['Hideaway', 'KinBall2', 'PolarBear2', 'CarChase1', 'Bike', 'DriftCar2', 'Lion', 'Badminton1', 'Puppies1', 'Basketball', 'Rope', 'Drone3', 'Jet1', 'Bharatanatyam', 'Alladin', 'Badminton2', 'Boxing2', 'Drone2', 'BreakfastClub', 'CarChase3', 'Jet2', 'Jet4', 'Elephants', 'Helicopter', 'Billiards1', 'MotorcycleChase', 'Dashcam', 'PolarBear3', 'IceSkating', 'DriftCar1', 'Jet5', 'Parakeet', 'KinBall3', 'Drone1', 'KinBall1', 'Boxing1', 'Boat', 'Boxing3', 'PolarBear1', 'Mohiniyattam', 'ZebraFish', 'Sam', 'Aquarium1', 'Puppies2', 'Violinist', 'ISS', 'Billiards2', 'CarChase2', 'Jet3', 'Aquarium2']

        return sequence_list