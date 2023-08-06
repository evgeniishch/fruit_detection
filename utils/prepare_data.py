import os
import numpy as np
from tqdm import tqdm
import warnings
import shutil

IMGS_PATH = "acfr-fruit-dataset/apples/images/"
LABELS_PATH = "acfr-fruit-dataset/apples/annotations/"
SPLITS_PATH = "acfr-fruit-dataset/apples/sets"

IMG_WIDTH, IMG_HEIGTH = 308, 202
SPLITS = ["train", "val", "test"]

def reformat_data():
	labels_files = os.listdir(LABELS_PATH)

	for file in tqdm(labels_files, desc="Reformatting data to YOLO"):
		labels_file = np.loadtxt(os.path.join(LABELS_PATH, file), delimiter=",", ndmin=2)

		if not len(labels_file):
			continue

		# Each row is class x_center y_center width height format
		labels_file[:, 0] = 0
		labels_file[:, -1] = labels_file[:, -2]
		labels_file[:, -2:] *= 2

		# Normalize box coordinates - divide x_center and width by image width, and y_center and height by image height.
		labels_file[:, 1] /= IMG_WIDTH
		labels_file[:, 3] /= IMG_WIDTH
		labels_file[:, 2] /= IMG_HEIGTH
		labels_file[:, 4] /= IMG_HEIGTH

		fmt = '%d', '%1.2f', '%1.2f', '%1.2f', '%1.2f'
		np.savetxt(os.path.join(LABELS_PATH, os.path.splitext(file)[0] + ".txt"), labels_file, fmt=fmt)
		# os.remove(os.path.join(LABELS_PATH, file))


def organize_directories():
	for folder in ["images", "labels"]:
		os.mkdir(os.path.join("data", folder))
		for split in SPLITS:
			os.mkdir(os.path.join("data", folder, split))

	for split in SPLITS:
		split_path = os.path.join(SPLITS_PATH, split + ".txt")
		
		with open(split_path, "r") as f:
			sample_ids = f.readlines()
		
		for sample_id in tqdm(sample_ids, desc="Arranging {} split".format(split)):
			sample_id = sample_id.strip()
			shutil.copy(os.path.join(IMGS_PATH, sample_id + ".png"), os.path.join("data", "images", split, sample_id + ".png"))
			if os.path.isfile(os.path.join(LABELS_PATH, sample_id + ".txt")):
				shutil.copy(os.path.join(LABELS_PATH, sample_id + ".txt"), os.path.join("data", "labels", split, sample_id + ".txt"))


def main():
	with warnings.catch_warnings():
		warnings.filterwarnings('ignore', r'loadtxt')
		reformat_data()

	organize_directories()


if __name__ == "__main__":
    main()




