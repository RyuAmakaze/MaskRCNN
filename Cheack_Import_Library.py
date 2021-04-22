"""
TensorFlow1.14.0,python,keras,numpy,cv2をインポートし、versionチェック
Import_Requirement(CheckFlag):学習に必要なものをインポートする。

Args:
    checkFlag:Importしたものを確認するかどうか、1で確認する。

"""

def Version_Check(CheckFlag):
    import sys
    import tensorflow as tf
    import keras
    import numpy
    import cv2

    if CheckFlag==1:
        print('TensorFlow_version(1.14.0) ;  '+tf.__version__)
        print('python version(3.6.5) ; ' + sys.version)
        print('keras version(2.2.4) ; ' +keras.__version__)
        print('numpy version(1.16.4) ; ' +numpy.__version__)
        print('cv2 version(4.5.1) ; ' +cv2.__version__)
