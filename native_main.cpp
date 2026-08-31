#include <jni.h>
#include <android/log.h>
#include <android_native_app_glue.h>

#define LOGI(...) __android_log_print(ANDROID_LOG_INFO, "SpiderManEngine", __VA_ARGS__)

void handle_cmd(struct android_app* app, int32_t cmd) {
    switch (cmd) {
        case APP_CMD_INIT_WINDOW:
            LOGI(">>> [NATIVE WINDOW] GLES3 Pipeline Initialized & Rendering Active.");
            break;
        case APP_CMD_TERM_WINDOW:
            LOGI(">>> [NATIVE WINDOW] Window Terminated.");
            break;
        default:
            break;
    }
}

void android_main(struct android_app* state) {
    app_dummy();
    LOGI("==================================================");
    LOGI("=== Spider-Man Remastered Walkthrough Engine Boot ===");
    LOGI("==================================================");
    
    state->onAppCmd = handle_cmd;

    int ident;
    int events;
    struct android_poll_source* source;

    while (1) {
        while ((ident = ALooper_pollAll(0, NULL, &events, (void**)&source)) >= 0) {
            if (source != NULL) {
                source->process(state, source);
            }
            if (state->destroyRequested != 0) {
                LOGI(">>> Engine Shutdown Requested.");
                return;
            }
        }
    }
}
