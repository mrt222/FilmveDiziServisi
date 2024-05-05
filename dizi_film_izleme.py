import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QAction, QMenuBar, QMenu, QMessageBox
)
from PyQt5.QtGui import QFont

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 120)
        self.setWindowTitle('Giriş')
        self.setStyleSheet("background-color: #003366; color: white;")

        layout = QVBoxLayout()

        self.user_label = QLabel("Kullanıcı Adı:")
        self.user_input = QLineEdit()
        self.pass_label = QLabel("Şifre:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Giriş Yap")
        self.login_button.setStyleSheet("background-color: #FFA500; color: white;")
        self.login_button.clicked.connect(self.check_credentials)

        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_credentials(self):
        username = self.user_input.text()
        password = self.pass_input.text()

        if username == "maruf" and password == "korkutata":
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            self.user_label.setText("Hatalı kullanıcı adı veya şifre!")
            self.user_label.setStyleSheet("color: red;")

class SeriesWidget(QWidget):
    def __init__(self, series_list, parent=None):
        super().__init__(parent)
        self.series_list = series_list
        self.initializeUI()

    def initializeUI(self):
        layout = QVBoxLayout()

        for series in self.series_list:
            series_label = QLabel(f"<b>{series['title']}</b><br>"
                                  f"Yönetmen: {series['director']}<br>"
                                  f"Çıkış Yılı: {series['release_year']}<br>"
                                  f"Sezon Sayısı: {series['seasons']}<br>")
            watch_button = QPushButton("İzle", self)
            watch_button.setStyleSheet("background-color: #FFA500; color: white;")
            watch_button.clicked.connect(lambda _, s=series: self.parent().watch_series(s))
            layout.addWidget(series_label)
            layout.addWidget(watch_button)

        self.setLayout(layout)

class MovieWidget(QWidget):
    def __init__(self, movie_list, parent=None):
        super().__init__(parent)
        self.movie_list = movie_list
        self.initializeUI()

    def initializeUI(self):
        layout = QVBoxLayout()

        for movie in self.movie_list:
            movie_label = QLabel(f"<b>{movie['title']}</b><br>"
                                  f"Yönetmen: {movie['director']}<br>"
                                  f"Konu: {movie['plot']}<br>"
                                  f"Yayın Yılı: {movie['release_year']}<br>")
            watch_button = QPushButton("İzle", self)
            watch_button.setStyleSheet("background-color: #FFA500; color: white;")
            watch_button.clicked.connect(lambda _, m=movie: self.parent().watch_movie(m))
            layout.addWidget(movie_label)
            layout.addWidget(watch_button)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.series_widget = None  
        self.movie_widget = None   
        self.initializeUI()
        self.watched_series = []  
        self.watched_movies = []  

    def initializeUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Kültür Üniversitesi Dizi&Film İzleme Platformu')
        self.setStyleSheet("background-color: #003366; color: white;")

        # Setup menu
        self.menu_bar = self.menuBar()
        user_menu = self.menu_bar.addMenu("User : Maruf Korkutata")

        user_info_action = QAction("Kullanıcı Bilgileri", self)
        user_info_action.triggered.connect(self.display_user_info)
        user_menu.addAction(user_info_action)

        watched_series_action = QAction("İzlediğim Diziler", self)
        watched_series_action.triggered.connect(self.display_watched_series)
        user_menu.addAction(watched_series_action)

        watched_movies_action = QAction("İzlediğim Filmler", self)
        watched_movies_action.triggered.connect(self.display_watched_movies)
        user_menu.addAction(watched_movies_action)

        self.anasayfa_don_action = QAction("Anasayfa Dön", self)
        self.anasayfa_don_action.triggered.connect(self.back_to_main_window)
        user_menu.addAction(self.anasayfa_don_action)

        
        self.home_button = QPushButton("Anasayfa Dön", self)
        self.home_button.clicked.connect(self.back_to_main_window)
        self.home_button.setGeometry(650, 530, 100, 30)
        self.home_button.setStyleSheet("background-color: #FFA500; color: white;")

        
        self.movies_button = QPushButton("Film İzle", self)
        self.movies_button.clicked.connect(self.display_movies)
        self.movies_button.setGeometry(600, 300, 150, 50)
        self.movies_button.setStyleSheet("background-color: #FFA500; color: white;")

        self.series_button = QPushButton("Dizi İzle", self)
        self.series_button.clicked.connect(self.display_series)
        self.series_button.setGeometry(50, 300, 150, 50)
        self.series_button.setStyleSheet("background-color: #FFA500; color: white;")

        self.display_home()  

    def display_home(self):
        self.movies_button.show()
        self.series_button.show()
        self.home_button.hide()

        if self.series_widget:
            self.series_widget.deleteLater()
            self.series_widget = None

        if self.movie_widget:
            self.movie_widget.deleteLater()
            self.movie_widget = None

        title_label = QLabel("KÜLTÜR ÜNİVERSİTESİ DİZİ&FİLM İZLEME PLATFORMU", self)
        title_font = QFont("Arial", 15, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setGeometry(0, 50, 800, 50)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #FFA500;")
        title_label.show()

    def display_user_info(self):
        self.hide_home_buttons()
        QMessageBox.information(self, "Kullanıcı Bilgileri", 
                                "Kullanıcı: Maruf Korkutata\n"
                                "Telefon Numarası: 0536 *** ****\n"
                                "Mail Adresi: marufkorkutata@gmail.com\n"
                                "Hesap Oluşturma Tarihi: 03.07.2023\n"
                                "Son İzleme Tarihi: 13.05.2024")

    def display_watched_series(self):
        self.hide_home_buttons()
        if self.watched_series:
            watched_series_text = "\n".join(set([f"{series['title']} - {series['director']} ({series['release_year']})" for series in self.watched_series]))
            QMessageBox.information(self, "İzlediğim Diziler", watched_series_text)
        else:
            QMessageBox.information(self, "İzlediğim Diziler", "Henüz hiç dizi izlenmedi.")

    def display_watched_movies(self):
        self.hide_home_buttons()
        if self.watched_movies:
            watched_movies_text = "\n".join(set([f"{movie['title']} - {movie['director']} ({movie['release_year']})" for movie in self.watched_movies]))
            QMessageBox.information(self, "İzlediğim Filmler", watched_movies_text)
        else:
            QMessageBox.information(self, "İzlediğim Filmler", "Henüz hiç film izlenmedi.")

    def display_movies(self):
        self.hide_home_buttons()
        movie_list = [
            {"title": "Inception", "director": "Christopher Nolan", "plot": "Bilinçaltına girip hırsızlık yapma konsepti", "release_year": 2010},
            {"title": "The Shawshank Redemption", "director": "Frank Darabont", "plot": "Hapishanede hayatta kalma mücadelesi", "release_year": 1994},
            {"title": "The Godfather", "director": "Francis Ford Coppola", "plot": "Mafya babasının hikayesi", "release_year": 1972},
            {"title": "Pulp Fiction", "director": "Quentin Tarantino", "plot": "Karmaşık hikayelerin kesiştiği bir gün", "release_year": 1994},
            {"title": "Forrest Gump", "director": "Robert Zemeckis", "plot": "Zeki ama saf bir adamın hayatı", "release_year": 1994}
        ]

        self.movie_widget = MovieWidget(movie_list, self)
        self.setCentralWidget(self.movie_widget)

    def display_series(self):
        self.hide_home_buttons()
        series_list = [
            {"title": "Breaking Bad", "director": "Vince Gilligan", "release_year": 2008, "seasons": 5},
            {"title": "Game of Thrones", "director": "David Benioff, D. B. Weiss", "release_year": 2011, "seasons": 8},
            {"title": "Friends", "director": "David Crane, Marta Kauffman", "release_year": 1994, "seasons": 10},
            {"title": "Stranger Things", "director": "The Duffer Brothers", "release_year": 2016, "seasons": 4},
            {"title": "The Office", "director": "Greg Daniels", "release_year": 2005, "seasons": 9}
        ]

        self.series_widget = SeriesWidget(series_list, self)
        self.setCentralWidget(self.series_widget)

    def watch_series(self, series):
        if series not in self.watched_series:
            self.watched_series.append(series)
            QMessageBox.information(self, "Dizi İzlendi", f"{series['title']} dizisi izlendi!")
            self.update_watched_series_widget()

    def watch_movie(self, movie):
        if movie not in self.watched_movies:
            self.watched_movies.append(movie)
            QMessageBox.information(self, "Film İzlendi", f"{movie['title']} filmi izlendi!")
            self.update_watched_movies_widget()

    def update_watched_series_widget(self):
        pass

    def update_watched_movies_widget(self):
        pass

    def hide_home_buttons(self):
        self.movies_button.hide()
        self.series_button.hide()
        self.home_button.show()

    def back_to_main_window(self):
        self.hide_home_buttons()
        self.display_home()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())
