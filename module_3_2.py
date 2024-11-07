def send_email(message, recipient, *,
               sender="university.help@gmail.com"):  # определяем функцию с двумя позиционными аргументами и одним именованным с значением по умолчанию
    # Проверка корректности e-mail адресов
    valid_domains = (".com", ".ru", ".net")  # допустимые домены
    if "@" not in recipient or not recipient.endswith(valid_domains):  # проверяем корректность адреса получателя
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")  # выводим сообщение об ошибке
        return  # завершаем выполнение функции
    if "@" not in sender or not sender.endswith(valid_domains):  # проверяем корректность адреса отправителя
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")  # выводим сообщение об ошибке
        return  # завершаем выполнение функции

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")  # выводим сообщение, если отправитель и получатель совпадают
        return  # завершаем выполнение функции

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(
            f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")  # выводим сообщение об успешной отправке
    else:
        print(
            f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")  # выводим сообщение о нестандартном отправителе