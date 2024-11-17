import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # имя пользователя
        self.password = self.hash_password(password)  # хэшированный пароль
        self.age = age  # возраст пользователя

    @staticmethod
    def hash_password(password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)  # хэширование пароля

    def __str__(self):
        return f"User(nickname={self.nickname}, age={self.age})"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname and self.password == other.password
        return False


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # заголовок видео
        self.duration = duration  # продолжительность видео
        self.time_now = 0  # секунда остановки
        self.adult_mode = adult_mode  # ограничение по возрасту

    def __str__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        return False


class UrTube:
    def __init__(self):
        self.users = []  # список пользователей
        self.videos = []  # список видео
        self.current_user = None  # текущий пользователь

    def log_in(self, nickname, password):
        password_hash = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                print(f"User {nickname} logged in successfully.")
                return
        print("Invalid username or password!")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"User {nickname} registered and logged in successfully.")

    def log_out(self):
        self.current_user = None
        print("User logged out successfully.")

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Video '{video.title}' added to UrTube.")

    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                return
        print("Видео не найдено")

    def __str__(self):
        return f"UrTube(current_user={self.current_user}, total_users={len(self.users)}, total_videos={len(self.videos)})"


# Код для проверки
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
