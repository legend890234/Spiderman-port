package com.engine.spiderman;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import java.io.File;

public class MainActivity extends Activity {
    private TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        tv = new TextView(this);
        tv.setText("Spider-Man Remastered Port\n\nStatus: Loading native libraries...");
        setContentView(tv);

        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    String nativeDir = getApplicationInfo().nativeLibraryDir;
                    
                    // Explicitly load dependencies in order using absolute paths to satisfy namespaces
                    System.load(nativeDir + "/libc++_shared.so");
                    
                    try {
                        System.load(nativeDir + "/libEGL.so.1");
                    } catch (Throwable t) {
                        Log.w("SpidermanEngine", "Could not pre-load libEGL.so.1, trying system fallback", t);
                    }

                    System.load(nativeDir + "/libspiderman.so");

                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            tv.setText("Spider-Man Remastered Port\n\nStatus: Success! Engine initialized.");
                        }
                    });
                } catch (final Throwable e) {
                    Log.e("SpidermanEngine", "Load failed", e);
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            tv.setText("Spider-Man Remastered Port\n\nStatus: Error -> " + e.getClass().getSimpleName() + ": " + e.getMessage());
                        }
                    });
                }
            }
        }).start();
    }
}
