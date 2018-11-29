from enum import Enum, auto


class Anlyser:
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
    def __init__(self, str):
        self.key_words = ["for", "to", "step", "exit", "next"]
        self.inds = []
        self.consts = []
        self.math_oper=['+', '-', '*', '/']
        self.errors = ["Error key word", "Error inedificator", "Error const"]
        self.error_message = "ERROR"
        self._str = str
        self._pos = 0


    def control(self):
        flag = False
        state = self.EnumStates.S
        EnumStates = self.EnumStates
        _str = self._str.lower()
        _pos = self._pos

        count_symbol = 0
        while (state != EnumStates.Error) and (state != EnumStates.F):

            if _pos >= len(_str):
                state = EnumStates.Error
            else:
                ch = _str[_pos]
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
                    elif _str[_pos].isalpha() or _str[_pos].isdigit():
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
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.L
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.L:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.L
                    elif _str[_pos].isalpha():
                        state = EnumStates.T
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.T:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.U1
                    elif _str[_pos].isalnum():
                        state = EnumStates.T
                    elif _str[_pos] == '=':
                        state = EnumStates.U
                    else:
                        state = EnumStates.Error
                elif state == EnumStates.U1:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.U1
                    elif _str[_pos] == '=':
                        state = EnumStates.U
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.U:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.U
                    elif _str[_pos] == '-':
                        state = EnumStates.V3
                    elif _str[_pos].isdigit() and _str[_pos] != '0':
                        state = EnumStates.V2
                    elif _str[_pos] == '0':
                        state = EnumStates.V4
                    elif _str[_pos].isalpha():
                        state = EnumStates.V
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.V3:
                    if _str[_pos].isdigit() and _str[_pos] != '0':
                        state = EnumStates.V2
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.V2:
                    if _str[_pos].isdigit():
                        state = EnumStates.V2
                    elif _str[_pos] == ' ':
                        state = EnumStates.V5
                    elif _str[_pos] in self.math_oper:
                        state = EnumStates.U
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.X
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.V4:
                    if _str[_pos] == ' ':
                        state = EnumStates.V5
                    elif _str[_pos] in self.math_oper:
                        state = EnumStates.U
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.X
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.V:
                    if _str[_pos].isalpha():
                        state = EnumStates.V
                    elif _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.V5
                    elif _str[_pos] in self.math_oper:
                        state = EnumStates.U
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.X
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.V5:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.V5
                    elif _str[_pos] in self.math_oper:
                        state = EnumStates.U
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.X
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.X:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.X
                    elif _str[_pos] == 'n':
                        state = EnumStates.X1
                    elif _str[_pos] == 'e':
                        state = EnumStates.Y

                elif state == EnumStates.Y:
                    if _str[_pos] == 'x':
                        state = EnumStates.Y2
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.Y2:
                    if _str[_pos] == 'i':
                        state = EnumStates.Y3
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.Y3:
                    if _str[_pos] == 't':
                        state = EnumStates.Y4
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.Y4:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Y5
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.Y5:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Y5
                    elif _str[_pos] == 'f':
                        state = EnumStates.Y6
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.Y6:
                    if _str[_pos] == 'o':
                        state = EnumStates.Y7
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.Y7:
                    if _str[_pos] == 'r':
                        state = EnumStates.Y8
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.Y8:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Y8
                    elif _str[_pos] == '\r' or _str[_pos] == '\n':
                        state = EnumStates.Y9
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.Y9:
                    if _str[_pos] == 'n':
                        state = EnumStates.X1
                    elif _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Y9
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.X1:
                    if _str[_pos] == 'e':
                        state = EnumStates.X2
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.X2:
                    if _str[_pos] == 'x':
                        state = EnumStates.X3
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.X3:
                    if _str[_pos] == 't':
                        state = EnumStates.X4
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.X4:
                    if _str[_pos] == ' ':
                        state = EnumStates.Z
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.Z:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Z
                    elif _str[_pos].isalpha():
                        state = EnumStates.Z1
                    else:
                        state = EnumStates.Error

                elif state == EnumStates.Z1:
                    if _str[_pos] == '\n' or _str[_pos] == ';':
                        state = EnumStates.F
                    elif _str[_pos].isalnum():
                        state = EnumStates.Z1
                    else:
                        state = EnumStates.Error

                else:
                    state = EnumStates.Error

                _pos += 1
        if state == EnumStates.F:
            flag = True
        return flag



