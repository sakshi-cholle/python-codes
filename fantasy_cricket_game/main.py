#This is core file that connects the UI, points, and database.
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from team import Ui_FastasyCricketGame


class FantasyCricket(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FastasyCricketGame()
        self.ui.setupUi(self)
        
        # Init points and counts
        self.total_points = 1000
        self.used_points = 0
        self.selected_players = []

        # Connect signals
        self.ui.radioBat.toggled.connect(self.load_players)
        self.ui.radiobow.toggled.connect(self.load_players)
        self.ui.radioar.toggled.connect(self.load_players)
        self.ui.radiowk.toggled.connect(self.load_players)
        self.ui.availablePlayersList.itemDoubleClicked.connect(self.add_player)
        self.ui.selectedPlayersList.itemDoubleClicked.connect(self.remove_player)
        self.ui.btnevaluate.clicked.connect(self.evaluate_score)

        # Load initial list
        self.load_players()

    def get_selected_category(self):
        if self.ui.radioBat.isChecked():
            return "BAT"
        elif self.ui.radiobow.isChecked():
            return "BOW"
        elif self.ui.radioar.isChecked():
            return "AR"
        elif self.ui.radiowk.isChecked():
            return "WK"
        return ""

    def load_players(self):
        category = self.get_selected_category()
        self.ui.availablePlayersList.clear()
        if not category:
            return

        conn = sqlite3.connect("cricket.db")
        cursor = conn.cursor()
        cursor.execute("SELECT player FROM stats WHERE ctg = ?", (category,))
        players = cursor.fetchall()
        conn.close()

        for p in players:
            if p[0] not in self.selected_players:
                self.ui.availablePlayersList.addItem(p[0])

    def add_player(self, item):
        player = item.text()
        conn = sqlite3.connect("cricket.db")
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM stats WHERE player=?", (player,))
        result = cursor.fetchone()
        conn.close()

        if result:
            value = result[0]
            if self.used_points + value > self.total_points:
                QMessageBox.warning(self, "Points Exceeded", "Not enough points to add this player.")
                return

            self.ui.selectedPlayersList.addItem(player)
            self.selected_players.append(player)
            self.used_points += value

            # Update points display
            self.ui.label_6.setText(f"Points Available {self.total_points - self.used_points}")
            self.ui.label_7.setText(f"Points used {self.used_points}")

            self.load_players()

    def remove_player(self, item):
        player = item.text()
        conn = sqlite3.connect("cricket.db")
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM stats WHERE player=?", (player,))
        result = cursor.fetchone()
        conn.close()

        if result:
            value = result[0]
            self.used_points -= value
            self.selected_players.remove(player)
            self.ui.selectedPlayersList.takeItem(self.ui.selectedPlayersList.row(item))

            # Update points
            self.ui.label_6.setText(f"Points Available {self.total_points - self.used_points}")
            self.ui.label_7.setText(f"Points used {self.used_points}")

            self.load_players()

    def evaluate_score(self):
        if not self.selected_players:
            QMessageBox.information(self, "No Team", "Please select players first.")
            return

        total_score = 0
        conn = sqlite3.connect("cricket.db")
        cursor = conn.cursor()
        for player in self.selected_players:
            cursor.execute("SELECT runs, wickets, catches FROM match WHERE player=?", (player,))
            data = cursor.fetchone()
            if data:
                runs, wickets, catches = data
                score = runs // 2 + wickets * 10 + catches * 10
                total_score += score
        conn.close()

        QMessageBox.information(self, "Evaluation Result", f"Total Fantasy Score: {total_score}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FantasyCricket()
    window.show()
    sys.exit(app.exec_())
