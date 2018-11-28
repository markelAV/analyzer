from enum import Enum, auto


class Anlyser:
    def __init__(self, str):
        self.key_words = ["for", "to", "step", "exit", "next"]
        self.inds = []
        self.consts = []
        self.math_oper=['+', '-', '*', '/']
        self.errors = ["Error key word", "Error inedificator", "Error const"]
        self.error_message = "ERROR"
        _str = str
        _pos = 0


    def control(self):
        flag = False
        state = EnumStates.S
        count_symbol = 0
        while (state != EnumStates.Error) and (state != EnumStates.F):
            if _s >= len(_str):
                state = EnumStates.Error
            else:
                if state == EnumStates.S:
                    if _str[_pos] == 'f':
                        state = EnumStates.A1
                        #_pos += 1
                    elif _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.S#_pos += 1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.A1:
                    if _str[_pos] == 'o':
                        state = EnumStates.A2
                        #_pos += 1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.A2:
                    if _str[_pos] == 'r':
                        state = EnumStates.A3
                       # _pos += 1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.A3:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.B
                        #_pos += 1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.B:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.B#_pos += 1
                    elif _str[_pos].isalpha():
                        state = EnumStates.C
                        #_pos += 1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.C:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.C1
                       # _pos += 1
                    elif _str[_pos].isalpha():
                        state = EnumStates.C
                    elif _str[_pos] == '=':
                        state = EnumStates.D
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.C1:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.C1#_pos += 1
                    elif _str[_pos] == '=':
                        state = EnumStates.D
                        #_pos += 1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.D:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.D
                    elif _str[_pos] == '-':
                        state = EnumStates.G3
                    elif _str[_pos] == '0':
                        state = EnumStates.G2
                    elif _str[_pos].isdigit() and _str[_pos] != '0':
                        state = EnumStates.G
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.G3:
                    if _str[_pos].isdigit() and _str[_pos] != '0':
                        state = EnumStates.G #_pos += 1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.G2:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.H #_pos += 1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.G:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.H #_pos += 1
                    elif _str[_pos].isdigit():
                        state = EnumStates.G
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.H:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.H #_pos += 1
                    elif _str[_pos] == 't':
                        state = EnumStates.I
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.I:
                    if _str[_pos] == 'o':
                        state = EnumStates.I2 #_pos += 1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.I2:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.J #_pos += 1
                    elif _str[_pos].isdigit():
                        state = EnumStates.G
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.J:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.J #_pos += 1
                    elif _str[_pos].isdigit() and _str[_pos] != '0':
                        state = EnumStates.K
                    elif _str[_pos] != '-':
                        state = EnumStates.J2
                    elif _str[_pos] == '0':
                        state = EnumStates.J3
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.J2:
                    if _str[_pos].isdigit() and _str[_pos] != '0':
                        state = EnumStates.K
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.J3:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.M
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.L
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.K:
                    if _str[_pos].isdigit():
                        state = EnumStates.K
                    elif _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.M
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.L
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.M:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.M
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.L
                    elif _str[_pos] == 's':
                        state = EnumStates.M1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.M1:
                    if _str[_pos] == 't':
                        state = EnumStates.M2
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.M2:
                    if _str[_pos] == 'e':
                        state = EnumStates.M3
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.M3:
                    if _str[_pos] == 'p':
                        state = EnumStates.M4
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.M4:
                    if _str[_pos] == ' ':
                        state = EnumStates.N
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.N:
                    if _str[_pos] == '-':
                        state = EnumStates.O2
                    elif _str[_pos].isdigit() and _str[_pos] != '0':
                        state = EnumStates.O
                    elif _str[_pos] == '0':
                        state = EnumStates.O4
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.O2:
                    if _str[_pos].isdigit() and _str[_pos] != '0':
                        state = EnumStates.O
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.O4:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.O4
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.L
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.O:
                    if _str[_pos].isdigit():
                        state = EnumStates.O
                    elif _str[_pos] == ' ' or _str[_pos] == '\t' or _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.L
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.L:
                    state = EnumStates.F
                else:
                    state = EnumStates.Error
                _pos += 1
        if state == EnumStates.F:
            flag = True
        return flag

    class EnumStates(Enum):
        S = auto()
        A1 = auto()
        A2 = auto()
        A3 = auto()
        B = auto()
        C = auto()
        C1 = auto()
        D = auto()
        G = auto()
        G2 = auto()
        G3 = auto()
        H = auto()
        I = auto()
        I2 = auto()
        J = auto()
        J2 = auto()
        J3 = auto()
        K = auto()
        K2 = auto()
        M = auto()
        M1 = auto()
        M2 = auto()
        M3 = auto()
        M4 = auto()
        N = auto()
        O = auto()
        O2 = auto()
        O4 = auto()
        L = auto()
        T = auto()
        U = auto()
        U1 = auto()
        V = auto()
        V2 = auto()
        V3 = auto()
        V4 = auto()
        V5 = auto()
        X = auto()
        X1 = auto()
        X2 = auto()
        X3 = auto()
        X4 = auto()
        Z = auto()
        Z1 = auto()
        Y = auto()
        Y2 = auto()
        Y3 = auto()
        Y4 = auto()
        Y5 = auto()
        Y6 = auto()
        Y7 = auto()
        Y8 = auto()
        Y9 = auto()
        F = auto()
        Error = auto()

