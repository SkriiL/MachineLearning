import os

class LoadingBar:
    def show_body(self, label, percentage):
        progress = [" " for x in range(0, 100)]
        for i in range(0, int(percentage)):
            progress[i] = "|"

        print(label)
        print("[", end="")
        for p in progress:
            print(p, end="")
        print("] ", percentage, "%")

    def show(self, label, percentage):
        os.system("cls")
        self.show_body(label=label, percentage=percentage)