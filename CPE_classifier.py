import os           
import numpy                      as np  
import tensorflow                 as tf
from tensorflow.keras.models      import Sequential, load_model

#  BATCH_SIZE 변수
BATCH_SIZE = 32

#  이미지 사이즈 변수
IMAGE_SIZE = [256, 256]

#  데이터 로드할 때 빠르게 로드할 수 있도록하는 설정 변수
AUTOTUNE = tf.data.experimental.AUTOTUNE

#  라벨링 함수
def get_label(file_path):
    parts = tf.strings.split(file_path, os.path.sep)
    return parts[-2] == 'cpe'

#  이미지 해석 함수
def decode_img(img):
    img = tf.image.decode_jpeg(img, channels = 3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    return tf.image.resize(img, IMAGE_SIZE)

#  이미지 처리 함수
def process_path(file_path):
    label = get_label(file_path)
    img = tf.io.read_file(file_path)
    img = decode_img(img)
    return img, label

#  모델 만드는 함수
def model_build():
    vgg_layer = tf.keras.applications.VGG19(include_top = False,
                                            weights = None,
                                            input_shape = (256, 256, 3),
                                            classes = 1,
                                            classifier_activation = "sigmoid")

    fc_layer = [
        tf.keras.layers.Flatten(),

        tf.keras.layers.Dense(4096),
        tf.keras.layers.Activation('relu'),
        tf.keras.layers.Dropout(0.5),

        tf.keras.layers.Dense(4096),
        tf.keras.layers.Activation('relu'),
        tf.keras.layers.Dropout(0.5),

        tf.keras.layers.Dense(1),
        tf.keras.layers.Activation('sigmoid')
    ]
    model = tf.keras.models.Sequential([vgg_layer] + fc_layer)
    model.load_weights('models/VGG19_with_aug_weight0604.h5')
    return model

#  이미지 예측 함수
def prediction_base(model, image):    
    #  들어오는 이미지 처리
    test_list_ds = tf.data.Dataset.list_files(image)
    test_ds = test_list_ds.map(process_path, num_parallel_calls=AUTOTUNE)
    test_ds = test_ds.batch(BATCH_SIZE)

    #  모델로 예측    
    predicted_image = model.predict(test_ds)

    if predicted_image >= 0.5:
        return str('CPE.')
    elif predicted_image < 0.5:
        return str('No CPE.')


# if __name__== '__main__':
#     #  테스트용 코드
#     ROOT_PATH = os.path.join(os.getenv('HOME') + '/CellPin_Trial')
#     cellpin_file = ROOT_PATH + '/CellPin/test/normal/419_9.png'
#     model = model_build()
#     prediction_base(model, cellpin_file)
