import tensorflow as tf
import cv2
import numpy as np


def _float_feature(value):
    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

class Feeder:

    @staticmethod
    def convert_to(imagesPath:str, files,labels, name, directory='',tqdm = False):
        filename = directory + name + '.tfrecord'
        print('Writing', filename)
        loop = tqdm_notebook(range(len(files))) if tqdm else range(len(file))
        with tf.io.TFRecordWriter(filename) as writer:
            for i in loop:
                image = cv2.imread(imagesPath+files[i])
                _,image = cv2.imencode('.png',image)
                image = image.tobytes()
                name = files[i][:len(files[i])-4]
                label = df[df['id']==files[i][:len(files[i])-4]]['corr'].iloc[0]
                example = tf.train.Example(
                  features=tf.train.Features(
                      feature={
                          'images': _bytes_feature(image),
                          'labels': _float_feature(label),

                      }))
                writer.write(example.SerializeToString())


    @staticmethod
    def extract_fn(tfrecord):
        # Extract features using the keys set during creation
        features = {
            'images': tf.io.FixedLenFeature([], tf.string),
            'labels': tf.io.FixedLenFeature([], tf.float32)

        }

        # Extract the data record
        sample = tf.io.parse_single_example(tfrecord, features)
        image = tf.image.decode_image(sample['images'],channels = 1)
        image = image/255
        image = image[2:129,21:148]
        label = sample['labels']
        label = tf.cast([label],tf.float32)
        return [image, label]

    def createDataset(filename):
        dataset = tf.data.TFRecordDataset(filename)
        dataset = dataset.map(_extract_fn)
        dataset = dataset.repeat(1000)
        dataset = dataset.batch(64,drop_remainder=True)
        iterator = iter(dataset)
        return iterator
