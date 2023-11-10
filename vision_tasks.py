#!/usr/bin/env python3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Sample code for Comp24011 SLAM lab solution

NB: The default code in non-functional; it simply avoids type errors
"""

__author__ = "USERNAME"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import cv2
import sys

from vision_tasks_base import VisionTasksBase

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class VisionTasks(VisionTasksBase):
    def __init__(self, *params):
        """Initialise instance by passing arguments to super class"""
        super().__init__(*params)

    def dt(self, des1, des2, threshold):
        """Implements feature matching based on distance thresholding

        :param des1: descriptors for the previous image (query)
        :type des1:  list
        :param des2: descriptors for the current image (train)
        :type des2:  list
        :param threshold: threshold value
        :type threshold:  float

        :return: matches for descriptors
        :rtype:  list
        """
        return []

    def nn(self, des1, des2, threshold=None):
        """Implements feature matching based on nearest neighbour

        :param des1: descriptors for the previous image (query)
        :type des1:  list
        :param des2: descriptors for the current image (train)
        :type des2:  list
        :param threshold: threshold value
        :type threshold:  float or None

        :return: matches for descriptors
        :rtype:  list
        """
        return []

    def nndr(self, des1, des2, threshold):
        """Implements feature matching based on nearest neighbour distance ratio

        :param des1: descriptors for the previous image (query)
        :type des1:  list
        :param des2: descriptors for the current image (train)
        :type des2:  list
        :param threshold: threshold value
        :type threshold:  float

        :return: matches for descriptors
        :rtype:  list
        """
        return []

    def matching_info(self, kp1, kp2, feature_matches):
        """Collects information about the matches of some feature

        :param kp1: keypoints for the previous image (query)
        :type kp1:  list
        :param kp2: keypoints for the current image (train)
        :type kp2:  list
        :param feature_matches: matches for the feature
        :type feature_matches:  list

        :return: coordinate of feature in previous image,
                 coordinates for feature matches in current image,
                 distances for feature matches in current image
        :rtype:  tuple, list, list
        """
        return (0,0), [], []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    import run_odometry
    run_odometry.main(sys.argv[1:])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
