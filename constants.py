import os

class Dataset:
    MSD_DIR = os.path.join(".", "MillionSongDataset")
    MSD_DATA_DIR = os.path.join(MSD_DIR, "data")
    MSD_ADD_DIR = os.path.join(MSD_DIR, "AdditionalFiles")

    MSD_UNIQ_TRACKS_PATH = os.path.join(MSD_ADD_DIR, "unique_tracks.txt")


class SubsetDataset:
    MSD_DIR = os.path.join(".", "MillionSongSubset")
    MSD_DATA_DIR = os.path.join(MSD_DIR, "data")
    MSD_ADD_DIR = os.path.join(MSD_DIR, "AdditionalFiles")

    MSD_UNIQ_TRACKS_PATH = os.path.join(MSD_ADD_DIR, "subset_unique_tracks.txt")


class TasteProfileDataset:
    TPD_DIR = os.path.join(".", "TasteProfile")
    TPD_TRAIN_PATH = os.path.join(TPD_DIR, "train_triplets.txt")
