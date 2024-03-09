import sys
from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class WelcomeScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setGeometry(100, 100, 800, 600) # Posição (100, 100) e tamanho (800x600 pixels)
        self.setWindowTitle("Tela Grande")
        self.show()

        self.login_button = QPushButton("Login", self)
        self.create_button = QPushButton("Create Account", self)
        layout.addWidget(self.login_button)
        layout.addWidget(self.create_button)

        self.login_button.clicked.connect(self.go_to_login)
        self.create_button.clicked.connect(self.go_to_create)

    def go_to_login(self):
        self.login_screen = LoginScreen()
        self.login_screen.show()

    def go_to_create(self):
        self.create_screen = CreateAccScreen()
        self.create_screen.show()

class LoginScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setGeometry(100, 100, 800, 600) # Posição (100, 100) e tamanho (800x600 pixels)
        self.setWindowTitle("Login")
        self.show()

        self.username_field = QLineEdit(self)
        self.password_field = QLineEdit(self)
        self.password_field.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login", self)
        layout.addWidget(self.username_field)
        layout.addWidget(self.password_field)
        layout.addWidget(self.login_button)

        self.login_button.clicked.connect(self.login)

    def login(self):
        # Aqui você pode adicionar a lógica de autenticação
        # Por exemplo, verificar o banco de dados para o usuário e senha
        print("Usuário logado:", self.username_field.text())
        self.main_screen = MainScreen()
        self.main_screen.show()

class CreateAccScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setGeometry(100, 100, 800, 600) # Posição (100, 100) e tamanho (800x600 pixels)
        self.setWindowTitle("Create Account")
        self.show()

        self.username_field = QLineEdit(self)
        self.password_field = QLineEdit(self)
        self.confirm_password_field = QLineEdit(self)
        self.create_button = QPushButton("Create Account", self)
        layout.addWidget(self.username_field)
        layout.addWidget(self.password_field)
        layout.addWidget(self.confirm_password_field)
        layout.addWidget(self.create_button)

        self.create_button.clicked.connect(self.create_account)

    def create_account(self):
        # Aqui você pode adicionar a lógica para criar uma nova conta
        print("Conta criada para:", self.username_field.text())

class MainScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.welcome_label = QLabel("Bem-vindo ao sistema!", self)
        layout.addWidget(self.welcome_label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome_screen = WelcomeScreen()
    welcome_screen.show()
    sys.exit(app.exec_())
