from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from brain import HelpyNeuralBrain
from guardian import HelpyGuardian
import threading

# Настройки окна для ПК (на Android они подстроятся сами)
Window.size = (400, 600)

class HelpyInterface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.brain = HelpyNeuralBrain()
        self.guardian = HelpyGuardian(self.brain)
        
        # Активируем права администратора (для Android)
        self.guardian.activate_admin_rights()

    def check_password(self, text):
        if self.brain.process_query(text) == "ДОСТУП 201321 ПОДТВЕРЖДЕН. Я — твой персональный ИИ.":
            self.ids.status_label.text = "Авторизация успешна!"
            self.ids.status_label.color = [0, 1, 0, 1] # Зеленый
        else:
            self.ids.status_label.text = "Неверный код! Доступ ограничен."
            self.ids.status_label.color = [1, 0, 0, 1] # Красный
            self.guardian.anti_theft_lock()

class HelpyAssistantApp(App):
    def build(self):
        return HelpyInterface()

if __name__ == "__main__":
    HelpyAssistantApp().run()
