LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE    := spiderman
LOCAL_SRC_FILES := GameFlowController.cpp main.cpp
LOCAL_LDLIBS    := -llog -landroid -lGLESv3
include $(BUILD_SHARED_LIBRARY)
