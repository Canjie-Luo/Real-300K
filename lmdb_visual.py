import lmdb
import random
from PIL import Image
import six
import os
import sys
import numpy as np
import argparse
import cv2

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--root', type=str, default='Real-300K-DataBase', help='path to the lmdb database')
	parser.add_argument('--num', type=int, default=10, help='number of the images to save')
	opt = parser.parse_args()

	env_src = lmdb.open(
	    opt.root,
	    max_readers=1,
	    readonly=True,
	    lock=False,
	    readahead=False,
	    meminit=False)

	if not env_src:
	    print('\nCannot open LMDB from %s.\n' % (root_src))
	    sys.exit(0)

	if os.path.isdir('./demo'):
		print('\nTrying to create a folder \"demo\" to save images, but this folder exists.\n')
		sys.exit(0)
	else:
		os.mkdir('./demo')
		print('\nCreate a folder \"demo\" to save images.\n')

	with env_src.begin(write=False) as txn:

		num_samples = int(txn.get('num-samples'.encode()))
		print('\nTotally %d samples in the source LMDB database.\n' % num_samples)

		for i in range(opt.num):

			idx_sample = random.randint(1, num_samples)

			img_key = 'image-%09d' % idx_sample
			imgbuf = txn.get(img_key.encode())

			buf = six.BytesIO()
			buf.write(imgbuf)
			buf.seek(0)

			try:
				img = Image.open(buf).convert('RGB')
			except IOError:
				print('\nCorrupted image (id: %d).\n.' % idx_sample)
				continue

			label_key = 'label-%09d' % idx_sample
			label = str(txn.get(label_key.encode()).decode('utf-8'))

			img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
			cv2.imwrite('demo/%d_%s.jpg' % (i, label), img)

	print('\nTotally %d images are saved in the folder \"demo\".\n' % opt.num)
				