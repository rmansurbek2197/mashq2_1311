class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.__status = "off"

    def turn_on(self):
        self.__status = "on"
        print(f"{self.name} yoqildi.")

    def turn_off(self):
        self.__status = "off"
        print(f"{self.name} o‘chirildi.")

    def get_status(self):
        return self.__status


class SmartHome:
    def __init__(self):
        self.devices = {}

    def add_device(self, device, restricted=False):
        self.devices[device.name] = {"device": device, "restricted": restricted}

    def control_device(self, user, device_name, action):
        if device_name not in self.devices:
            print("Bunday qurilma yo‘q.")
            return

        device_info = self.devices[device_name]
        if user.role == "guest" and device_info["restricted"]:
            print(f"{device_name} qurilmasiga siz kira olmaysiz.")
            return

        device = device_info["device"]
        if action == "on":
            device.turn_on()
        elif action == "off":
            device.turn_off()
        else:
            print("Noma’lum amal.")


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


home = SmartHome()
tv = SmartDevice("Televizor")
camera = SmartDevice("Xavfsizlik kamerasi")

home.add_device(tv)
home.add_device(camera, restricted=True)

admin = User("Ali", "admin")
guest = User("Vali", "guest")

home.control_device(admin, "Televizor", "on")
home.control_device(guest, "Xavfsizlik kamerasi", "on")


