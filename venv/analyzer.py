

# str[i].isdigit() - проверка строки на цифры
# str[i].isalnum() - проверка строки на буквы и цифры
# str[i].isalnum() - проверка строки на буквы
'''         Описаниеи ошибок:
    1. Ошибки в написании ключевых слов
        1) Наличие недопустимых символов
    2. Ошибки индентификатора:
        1) Не начинается с буквы
        2) Имеет длину более 8 символов
        3) Является зарезервированным словом : FOR, TO, STEP , EXIT , NEXT.
        4) Наличие недопусттимых символов
    3. Ошибки констант:
        1) Выход числа из диапозона -32768 - 32767
        2) Наличие недопустимых символов
    4. Наличие лишних символов в строке
'''

''' написать массив шаблонных ошибок "Название(тип) ошибки(+ можно дописать рекомендацию
(ожидался for или индедификатор не может начинаться с цифры и т.п.))). Строка(где возникла оштбка" '''

class Analyzer:

    def __init__(self):
        self.key_words = {"for", "to", "step", "exit", "next"}
        self.inds = []
        self.consts = []
        self.error_message = []

     # TESTING and Make and screw the TABLE

    def control_const(self, _str, index):
        if len(_str) == 0:
            return -1
        i = 0
        min_side = -32768
        max_side = 32767
        flag_error = True
        str_number = ""
        minus = False
        count_symbol = 0
        max_symbol = 5
        number = 0
        if _str[i] == '-':
            minus = True
            i += 1

        while (i < len(_str)) and (count_symbol <= max_symbol+1) and _str[i].isdigit():
            str_number += _str[i]
            count_symbol += 1
            i += 1
        if i == len(_str)or((count_symbol <= 5) and (_str[i] == ' ' or _str[i] == '\t' or _str[i] == '+'
                                                     or _str[i] == '-' or _str[i] == '*' or _str[i] == '/')):
            number = int(str_number)
            if minus:
                number = -number

            if (number > min_side) and (number < max_side):
                flag_error = False
        if not flag_error:
            #занесение константы в таблицу
            #return number
            self.consts.append(number) # deleate
            index += i
            return index
        else:
            return -1

    # Testing, to redo last "if" and screw thr Table
    def control_indentifier(self, _str, index):
        i = 0
        flag_error = True
        max_symbol = 8
        count_symbol = 0
        indentifier = ""
        # S.isalnum()	Состоит ли строка из цифр или букв проверить
        if _str[i].isalpha():
            indentifier += _str[i]
            i += 1
            count_symbol += 1
            while i < len(_str) and count_symbol <= max_symbol+1 and _str[i].isalnum():
                indentifier += _str[i]
                i += 1
                count_symbol += 1
            if i == len(_str) or (count_symbol <= max_symbol):
                if(indentifier.lower() != "for") and (indentifier.lower() != "to") and\
                        (indentifier.lower() != "exit") and (indentifier.lower() != "step") and\
                        (indentifier.lower() != "next"):
                    # уменьшить строку
                    #действия по занесению в таблицу ( массив)
                    flag_error = False
        if not flag_error:
            index += i
            self.inds.append(indentifier)
            return index
        else:
            return -1

    #Tesing
    #rename parse/ parsing

    def parse_first_line(self, _str):
        flags_error = True
        _str = _str.lower()
        i = 0
        while (_str[i] == ' ' or _str[i] == '\t') and (len(_str) - i) >= 12:
            i += 1
        if (len(_str) - i) >= 12 and _str.find("for ", i, i+2):
            i += 4
            while i < len(_str) and (_str[i] == ' ' or _str[i] == '\t') and (len(_str) - i) >= 8: # maybe not 8
                i += 1
            i = self.control_indentifier(_str[i:len(_str)], i)
            if (len(_str) - i) >= 7 and i > 0:
                while (_str[i] == ' ' or _str[i] == '\t') and (len(_str) - i) >= 7: # maybe not 7
                    i += 1
                if (len(_str) - i) >= 7 and _str[i] == '=':
                    i += 1
                    while (_str[i] == ' ' or _str[i] == '\t') and (len(_str) - i) >= 6:
                        i += 1
                    i = self.control_const(_str[i:len(_str)], i)
                    if(len(_str) - i) >= 6 and i > 0:
                        while i < len(_str) and (_str[i] == ' ' or _str[i] == '\t') and (len(_str) - i) >= 4:
                            i += 1
                        if (len(_str) - i) >= 4 and _str.find("to", i, i+1):
                            i += 2
                            while (_str[i] == ' ' or _str[i] == '\t') and (len(_str) - i) >= 1:
                                i += 1
                            i = self.control_const(_str[i:len(_str)], i)
                            if i > 0:
                                while i < len(_str) and (_str[i] == ' ' or _str[i] == '\t'):
                                    i += 1
                                if i == len(_str):
                                    flags_error = False
                                else:
                                    if (len(_str) - i) >= 6 and _str.find("step ", i, i + 3):
                                        i += 5
                                        while (len(_str) - i) >= 1 and (_str[i] == ' ' or _str[i] == '\t'):
                                            i += 1
                                        i = self.control_const(_str[i:len(_str)], i)
                                        if i > 0:
                                            if i == len(_str):
                                                flags_error = False
                                            while i < len(_str) and (_str[i] == ' ' or _str[i] == '\t'):
                                                i += 1
                                            if i == len(_str):
                                                flags_error = False
        return flags_error

    def parse_second_line(self, _str):
        flag_error = True
        _str = _str.lower()
        i = 0
        while i < len(_str) and (_str[i] == ' ' or _str[i] == '\t') and (len(_str) - i) >= 3:
            i += 1
        i = self.control_indentifier(_str[i:len(_str)], i)
        if (len(_str) - i) >= 2 and i > 0:
            while (_str[i] == ' ' or _str[i] == '\t') and (len(_str) - i) >= 2:
                i += 1
            if (len(_str) - i) >= 2 and _str[i] == '=':
                i += 1
                if (len(_str) - i) >= 1:
                    while i < len(_str):
                        while i < len(_str) and (_str[i] == ' ' or _str[i] == '\t') and (len(_str) - i) >= 1:
                            i += 1
                        i = self.parse_term(_str[i:len(_str)], i)
                        if i > 0:
                            while i < len(_str) and (_str[i] == ' ' or _str[i] == '\t'):
                                i += 1
                            # if i == len(str):
                            #    flag_error = False
                            if (len(_str)-i) > 1 and (_str[i] == '-' or _str[i] == '+' or _str[i] == '*' or _str[i] == '/'):
                                i += 1
                        else:
                            break
                        if (i > 0) and (i == len(_str)):
                            flag_error = False
        return flag_error

    def parse_term(self, _str, index):
        i = 0
        flag_error = True
        while i < len(_str) and (_str[i] == ' ' or _str[i] == '\t'):
            i += 1
        if i < len(_str) and (_str[i].isalnum() or _str[i] == '-'):
            if _str[i].isdigit() or _str[i] == '-':
                i = self.control_const(_str[i:len(_str)], i)

            else:
                i = self.control_indentifier(_str[i:len(_str)], i)
            if (i > 0) and (i <= len(_str)):
                flag_error = False
        if not flag_error:
            index += i
            return index
        else:
            return -1

    def parse_third_line(self, _str):
        flag_error = True
        _str = _str.lower()
        i = 0
        while (i < len(_str)) and (_str[i] == ' ' or _str[i] == '\t'):
            i += 1
        if (len(_str) - i) >= 8 and ("exit " in _str):
            i += 4
            while (len(_str) - i) >= 3 and (_str[i] == ' ' or _str[i] == '\t'):
                i += 1
            if ((len(_str) - i) == 3 and ("for" in _str)) or ((len(_str) - i) > 3 and ("for " in _str)):
                i += 3
                while (i < len(_str)) and (_str[i] == ' ' or _str[i] == '\t'):
                    i += 1
                if i == len(_str):
                    flag_error = False
        return flag_error

    def parse_fourth_line(self, _str):
        _str = _str.lower()
        flag_error = True
        i = 0
        while (i < len(_str)) and (_str[i] == ' ' or _str[i] == '\t'):
            i += 1
        if (len(_str) - i) >= 6 and ("next " in _str):
            i += 4
            while (i < len(_str)) and (_str[i] == ' ' or _str[i] == '\t'):
                i += 1
            if i < len(_str):
                i = self.control_indentifier(_str[i:len(_str)], i)
                if i > 0:
                    while (i < len(_str)) and (_str[i] == ' ' or _str[i] == '\t'):
                        i += 1
                    if i == len(_str):
                        flag_error = False
        return flag_error

    def main_analyzer_method(self, lines):
        flag_error = True
        self.inds = []
        if len(lines) == 4 or len(lines) == 3:
            if not self.parse_first_line(lines[0]) and not self.parse_second_line(lines[1]):
                if len(lines) == 3 and not self.parse_fourth_line(lines[2]):
                    flag_error = False
                else:
                    if len(lines) == 4 and not self.parse_third_line(lines[2]) and not self.parse_fourth_line(lines[3]):
                        flag_error = False
            if self.inds == [] or self.inds[0] != self.inds[len(self.inds)-1]:
                flag_error = True
        return flag_error

