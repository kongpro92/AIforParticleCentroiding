import cv2
import numpy as np
from particle import *

class Camera:
    def __init__(self, camera_matrix=None, distortion_coefficients=None,
        rotation_vector=None, translation_vector=None):
        self.camera_matrix = camera_matrix if camera_matrix is not None else np.eye(3, dtype=np.float32)
        self.distortion_coefficients = distortion_coefficients if distortion_coefficients is not None else np.zeros(5, dtype=np.float32)
        self.rotation_vector = rotation_vector if rotation_vector is not None else np.zeros(3, dtype=np.float32)
        self.translation_vector = translation_vector if translation_vector is not None else np.zeros(3, dtype=np.float32)

    def set_internal_parameters(self, camera_matrix, distortion_coefficients):
        self.camera_matrix = camera_matrix
        self.distortion_coefficients = distortion_coefficients

    def set_external_parameters(self, rotation_vector, translation_vector):
        self.rotation_vector = rotation_vector
        self.translation_vector = translation_vector

    def project_3d_to_2d(self, points_3d):
        points_2d, _ = cv2.projectPoints(
            points_3d, self.rotation_vector, self.translation_vector,
            self.camera_matrix, self.distortion_coefficients
        )
        return points_2d.squeeze().astype(float)


