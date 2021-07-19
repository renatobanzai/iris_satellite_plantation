import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

plt.rcParams['figure.figsize'] = [10, 10]

def get_8bits(img_source, show=False):
    img_8bits = cv2.convertScaleAbs(img_source, alpha=0.03)
    if show:
        plt.imshow(img_8bits, cmap='gray')
        plt.show()
    return img_8bits


def get_edges(img_source, show=False):
    img_edges = cv2.Canny(img_source, 10, 50, None)
    if show:
        plt.imshow(img_edges, cmap='gray')
        plt.show()
    return img_edges

def get_NDVI(img_b04_path, img_b08_path):
    img_b04 = cv2.imread(img_b04_path, -1)
    img_b08 = cv2.imread(img_b08_path, -1)
    NDVI = np.uint8(((img_b08 - img_b04) / (img_b08 + img_b04)) * 256)
    return NDVI


def view_kmeans(img_b04_path, img_b08_path, show=False):
    img_1 = get_NDVI(img_b04_path, img_b08_path)
    print("img_1.shape", img_1.shape)
    img_k = img_1.reshape((-1, 2))
    print("img_k.shape", img_k.shape)
    img_k = np.float32(img_k)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 1.0)
    attempts = 30
    k = 5
    ret, label, center = cv2.kmeans(img_k, k, None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    result = res.reshape((img_1.shape))
    if show:
        plt.imshow(result, cmap='gray')
        plt.show()
        plt.imshow(cv2.cvtColor(cv2.imread("./data/machine_learning/interest_tci_pivot.tif"), cv2.COLOR_BGR2RGB))
        plt.show()
    print("center", center)
    print("result", result)
    return result