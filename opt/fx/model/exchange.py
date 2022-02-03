# -*- coding: utf-8 -*-
import os, shutil

class proc:
    def __init__(self):
        current = str(os.getcwd())
        #in
        self.__input_path = current + "/in"
        #out
        self.__output_path = current + "/out"

    def checkPath(self):
        #in
        if not os.path.exists(self.__input_path):
            return True
        #out
        output = self.__output_path
        if os.path.exists(output):
            shutil.rmtree(output)
        os.mkdir(output)
        return False
