import os


class Dataset:
    MSD_DIR = os.path.join('.', 'MillionSongDataset')
    MSD_DATA_DIR = os.path.join(MSD_DIR, 'data')
    MSD_ADD_DIR = os.path.join(MSD_DIR, 'AdditionalFiles')

    MSD_UNIQ_TRACKS_PATH = os.path.join(MSD_ADD_DIR, 'unique_tracks.txt')


class SubsetDataset:
    MSD_DIR = os.path.join('.', 'MillionSongSubset')
    MSD_DATA_DIR = os.path.join(MSD_DIR, 'data')
    MSD_ADD_DIR = os.path.join(MSD_DIR, 'AdditionalFiles')

    MSD_UNIQ_TRACKS_PATH = os.path.join(MSD_ADD_DIR, 'subset_unique_tracks.txt')


class MSDChallengeDataset:
    MSDC_DIR = os.path.join('.', 'EvalDataYear1MSDWebsite')
    MSDC_EVAL_VISIBLE_PATH = os.path.join(MSDC_DIR, 'year1_valid_triplets_visible.txt')
    MSDC_EVAL_HIDDEN_PATH = os.path.join(MSDC_DIR, 'year1_valid_triplets_hidden.txt')
    MSDC_TEST_VISIBLE_PATH = os.path.join(MSDC_DIR, 'year1_test_triplets_visible.txt')
    MSDC_TEST_HIDDEN_PATH = os.path.join(MSDC_DIR, 'year1_test_triplets_hidden.txt')


class TasteProfileDataset:
    TPD_DIR = os.path.join('.', 'TasteProfile')
    TPD_TRAIN_PATH = os.path.join(TPD_DIR, 'train_triplets.txt')
