import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class SpidermanPortApp(App):
    def build(self):
        self.title = "Spider-Man Remastered Port"
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Status header
        status_label = Label(
            text="Status: Success! Engine initialized.",
            size_hint_y=None,
            height=50,
            bold=True
        )
        layout.add_widget(status_label)
        
        # Load JSON config
        config_path = "config/sequences/master_walkthrough.json"
        content_text = "Loading walkthrough data...\n"
        
        if os.path.exists(config_path):
            try:
                with open(config_path, "r") as f:
                    data = json.load(f)
                content_text += f"\nApp Title: {data.get('title', 'Walkthrough')}\n"
                content_text += f"Style: {data.get('style', 'Cinematic Flow')}\n\n"
                for cp in data.get("checkpoints", []):
                    content_text += f"[{cp.get('id')}] {cp.get('name')} ({cp.get('type', '').upper()})\n"
            except Exception as e:
                content_text += f"\nError parsing JSON: {e}"
        else:
            content_text += f"\nError: Config not found at {config_path}"
            
        # Scrollable text area for checkpoints
        scroll = ScrollView(size_hint=(1, 1))
        text_label = Label(
            text=content_text,
            size_hint_y=None,
            text_size=(self.root_window.width if self.root_window else 400, None)
        )
        text_label.bind(texture_size=lambda _, size: setattr(text_label, 'height', size[1]))
        scroll.add_widget(text_label)
        layout.add_widget(scroll)
        
        return layout

if __name__ == "__main__":
    SpidermanPortApp().run()
