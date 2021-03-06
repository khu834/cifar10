import keras
from keras.models import load_model
import matplotlib
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
from utils.plotting import plot_confusion_matrix, plot_multi_auc
import numpy as np


def evaluate_model(model_artifact, x_test, y_true, classes, batch_size=128):
    model = load_model(model_artifact)
    y_pred = model.predict(x=x_test, batch_size=batch_size)
    y_pred_argmax = np.argmax(y_pred, axis=-1)
    y_true_argmax = np.argmax(y_true, axis=-1)
    _, cm = plot_confusion_matrix(
        y_true_argmax, y_pred_argmax, classes, normalize=False, title=None, cmap=plt.cm.Blues
    )

    fpr, tpr, roc_auc = plot_multi_auc(y_true, y_pred, classes)
    print("Accuracy: {}".format(accuracy_score(y_true_argmax, y_pred_argmax)))
    return fpr, tpr, roc_auc, cm

