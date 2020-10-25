import json, datetime, os

ENVIRONMENT_DIR = "C:\\"


def check_last_session():
    directory_info = os.listdir("json")
    return directory_info[len(directory_info) - 1]


class MoodUtils:
    session_id = int()
    session_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __init__(self):
        os.chdir(ENVIRONMENT_DIR)
        if not os.path.exists("Moods"):
            os.mkdir("Moods")
            print("Created directory: Moods")
        os.chdir("Moods")

        if not os.path.exists("json"):
            os.mkdir("json")
            print("Created directory: json")

        if not os.path.exists("printable"):
            os.mkdir("printable")
            print("Created directory: printable")

        self.session_id = int(check_last_session()[:-5]) + 1
        with open(str(self.session_id) + ".json", "w+") as file:
            json.dump({"Session_id": self.session_id, "Session_start": self.session_start}, file, indent=2)
        with open(str(self.session_id) + ".txt", "w+") as file:
            file.write(f"Date: {self.session_start}\nSession number {self.session_id}\n"+"-"*20)

    def add_message(self, text):
        pass

    def add_mood(self, index, mood):
        pass

    def list_messages(self, exclude=True):
        pass


a = MoodUtils()
