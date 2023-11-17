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
        best_match = []
        best_keypoint = []
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k = 1500)
        for match in matches:
            for m in match:
                dist_value = m.distance
                if dist_value < threshold:
                    best_keypoint.append(m)
            best_match.append(best_keypoint)
            best_keypoint = []
        return best_match


    #TODO:Note that for >threshold, it is giving error
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
        best_match = []
        best_keypoint = []
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k = 100)
        for match in matches:
            f = 1.7976931348623157e+308
            a = None
            for m in match:
                dist_value = m.distance
                if dist_value < f:
                    f = dist_value
                    a = m
            if threshold == None or (threshold!= None and a.distance <= threshold):
                best_keypoint.append(a)
            best_match.append(best_keypoint)
            best_keypoint = []
        return best_match


    #Ambiguous
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
        best_match = []
        best_keypoint = []
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k = 2)
        for match in matches:
            feature_1 = match[0]
            feature_2 = match[1]
            if feature_1.distance <= feature_2.distance*threshold:
                best_keypoint.append(feature_1)
            best_match.append(best_keypoint)
            best_keypoint = []
        return best_match

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
        #print('Feature Matches looks like:')
        #print(feature_matches)
        #print('Length of feature_matches = '+ str(len(feature_matches)))
        if feature_matches == []:
            #print('No empty list allowed')
            return (0,0), [], []
        query_kp_index = feature_matches[0].queryIdx
        query_kp = kp1[query_kp_index]
        x_coord_query_kp = int(query_kp.pt[0])
        y_coord_query_kp = int(query_kp.pt[1])

        ref_coord_list = []
        ref_dist_list = []
        for feature in feature_matches:
            
            ref_dist_list.append(feature.distance)
            ref_kp_index = feature.trainIdx
            ref_kp = kp2[ref_kp_index]

            x_coord_ref_kp = int(ref_kp.pt[0])
            y_coord_ref_kp = int(ref_kp.pt[1])

            ref_coord_list.append((x_coord_ref_kp, y_coord_ref_kp))


        return (x_coord_query_kp,y_coord_query_kp), ref_coord_list, ref_dist_list

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    import run_odometry
    run_odometry.main(sys.argv[1:])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
