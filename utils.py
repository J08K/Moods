import datetime
import json
import os

ENVIRONMENT_DIR = "C:\\"


def check_last_session():
    directory_info = os.listdir("json")
    return directory_info[len(directory_info) - 1]


class MoodSession:
    session_id = int()
    session_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    """
    Message structure
    {
        "Session_id":1,
        "Session_start":date,
        "Moods":
        [
            {
            "time":time,
            "message":message
            "mood":mood
            }
        ]

    }
    """

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

        print("")

        self.session_id = int(check_last_session()[:-5]) + 1
        with open(str("json\\" + self.session_id) + ".json", "w+") as file:
            json.dump({"Session_id": self.session_id, "Session_start": self.session_start, "Moods": []}, file, indent=2)

    def add_message(self, text):
        with open("json\\" + str(self.session_id) + ".json", "r") as file:
            file_data = json.load(file)
            file_data["Moods"].append(
                {"time": datetime.datetime.now().strftime("%H:%M:%S"), "message": text, "mood": ""})
        with open("json\\" + str(self.session_id) + ".json", "w") as file:
            file.dump(file_data, file, indent=2)

    def add_mood(self, index, mood):
        with open("json\\" + str(self.session_id) + ".json", "r") as file:
            file_data = json.load(file)
            for mood_index in range(len(file_data["Moods"])):
                if mood_index == index:
                    file_data["Moods"][mood_index]["mood"] = mood
        with open("json\\" + str(self.session_id) + ".json", "w") as file:
            json.dump(file_data, file, indent=2)

    def list_messages(self, exclude=True):
        with open("json\\" + str(self.session_id) + ".json", "r") as file:
            file_data = json.load(file)
            temp_data = list()
            for mood, index in zip(file_data["Moods"], range(len(file_data["Moods"]))):
                if exclude:
                    if mood["mood"] != "":
                        temp_data.append(tuple(index, mood))
                else:
                    temp_data.append(tuple(index, mood))
            return temp_data


a = MoodSession()
