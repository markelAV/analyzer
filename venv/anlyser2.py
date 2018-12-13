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
        self.error_message = "Incomplete Line"
        self._str = str
        self._pos = 0
        self._count_iteration = 0
        self._step_isapsent = True

    def check_ident(self, str):
        if (len(str) <= 8) and not (str in self.key_words):
            self.inds.append(str)
            return True
        elif len(str) > 8:
            self.error_message = 'identifier name exceeds 8 characters'
        else:
            self.error_message = 'identifier name must not match the reserved word'
        return False
    def check_const(self, const):
        if (int(const) > -32768) and (int(const) < 32767):
            self.consts.append(int(const))
            return True
        self.error_message = 'the number should be between -32768 and 32767'
        return False
    def counting_iteration(self):
        if self._step_isapsent:
            if self.consts[1] > self.consts[0]:
                self._count_iteration = self.consts[1]-self.consts[0]
                if ((self.consts[0] < 0 and self.consts[1] >0)) or ((self.consts[0] > 0 and self.consts[1] <0)):
                    self._count_iteration +=1
            else:
                self._count_iteration = -1
        else:
            if self.consts[2] > 0:
                if self.consts[1] > self.consts[0]:
                    t = self.consts[1] - self.consts[0]
                    m = self.consts[2]
                    self._count_iteration = t//m
                    if ((self.consts[0] < 0 and self.consts[1] > 0)) or ((self.consts[0] > 0 and self.consts[1] < 0)):
                        self._count_iteration += 1
                else:
                    self._count_iteration = -1
            else:
                if self.consts[1] < self.consts[0]:
                    self._count_iteration = (self.consts[0] - self.consts[1])//abs(self.consts[2])
                    if ((self.consts[0] < 0 and self.consts[1] > 0)) or ((self.consts[0] > 0 and self.consts[1] < 0)):
                        self._count_iteration += 1
                else:
                    self._count_iteration = -1

    def control(self):
        idn = ""
        const = ""
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
                    elif _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.S
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'F\'"

                elif state == EnumStates.A1:
                    if _str[_pos] == 'o':
                        state = EnumStates.A2
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'O\'"

                elif state == EnumStates.A2:
                    if _str[_pos] == 'r':
                        state = EnumStates.A3
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'R\'"

                elif state == EnumStates.A3:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.B
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'space\' or \'Tab\'"

                elif state == EnumStates.B:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.B
                    elif _str[_pos].isalpha():
                        state = EnumStates.C
                        idn += _str[_pos]
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected letter"

                elif state == EnumStates.C:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        if self.check_ident(idn):
                            state = EnumStates.C1
                            idn = ''
                        else:
                            state = EnumStates.Error
                    elif _str[_pos].isalpha() or _str[_pos].isdigit(): #replaced by _str[_pos].isalpha() or _str[_pos].isdigit()
                        state = EnumStates.C
                        idn += _str[_pos]
                    elif _str[_pos] == '=':
                        if self.check_ident(idn):
                            state = EnumStates.D
                            idn = ''
                        else:
                            state = EnumStates.Error
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'=\' or letter"

                elif state == EnumStates.C1:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.C1
                    elif _str[_pos] == '=':
                        state = EnumStates.D
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'=\'"

                elif state == EnumStates.D:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.D
                    elif _str[_pos] == '-':
                        const += _str[_pos]
                        state = EnumStates.G3
                    elif _str[_pos] == '0':
                        self.check_const(_str[_pos])
                        const = ''
                        state = EnumStates.G2
                    elif _str[_pos].isdigit() and _str[_pos] != '0':
                        const += _str[_pos]
                        state = EnumStates.G
                    else:
                        state = EnumStates.Error
                        self.error_message = "Expect is number"

                elif state == EnumStates.G3:
                    if _str[_pos].isdigit() and _str[_pos] != '0':
                        const += _str[_pos]
                        state = EnumStates.G
                    else:
                        state = EnumStates.Error
                        self.error_message = 'expected number is unequal to zero'

                elif state == EnumStates.G2:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.H
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'space\'"

                elif state == EnumStates.G:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        if self.check_const(const):
                            state = EnumStates.H
                            const = ''
                        else:
                            state = EnumStates.Error
                    elif _str[_pos].isdigit():
                        const += _str[_pos]
                        state = EnumStates.G
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected number"

                elif state == EnumStates.H:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.H
                    elif _str[_pos] == 't':
                        state = EnumStates.I
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'T\'"

                elif state == EnumStates.I:
                    if _str[_pos] == 'o':
                        state = EnumStates.I2
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'O\'"

                elif state == EnumStates.I2:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.J
                    elif _str[_pos].isdigit():
                        state = EnumStates.G
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'space\' or \'Tab\'"

                elif state == EnumStates.J:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.J
                    elif _str[_pos].isdigit() and _str[_pos] != '0':
                        const += _str[_pos]
                        state = EnumStates.K
                    elif _str[_pos] == '-':
                        const += _str[_pos]
                        state = EnumStates.J2
                    elif _str[_pos] == '0':
                        self.check_const(_str[_pos])
                        state = EnumStates.J3
                    else:
                        state = EnumStates.Error
                        self.error_message = "expected character \'-\' or number"

                elif state == EnumStates.J2:
                    if _str[_pos].isdigit() and _str[_pos] != '0':
                        const += _str[_pos]
                        state = EnumStates.K
                    else:
                        self.error_message = "expected number"
                        state = EnumStates.Error

                elif state == EnumStates.J3:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.M
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.L
                    else:
                        self.error_message = "expected character \'space\' or \'end of line\'"
                        state = EnumStates.Error

                elif state == EnumStates.K:
                    if _str[_pos].isdigit():
                        const += _str[_pos]
                        state = EnumStates.K
                    elif _str[_pos] == ' ' or _str[_pos] == '\t':
                        if self.check_const(const):
                            state = EnumStates.M
                            const = ''
                        else:
                            state = EnumStates.Error
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        if self.check_const(const):
                            state = EnumStates.L
                            const = ''
                        else:
                            state = EnumStates.Error
                    else:
                        self.error_message = 'expected number or end of line'
                        state = EnumStates.Error

                elif state == EnumStates.M:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.M
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.L
                    elif _str[_pos] == 's':
                        state = EnumStates.M1
                    else:
                        self.error_message = "expected character \'S\' or \'end of line\'"
                        state = EnumStates.Error

                elif state == EnumStates.M1:
                    if _str[_pos] == 't':
                        state = EnumStates.M2
                    else:
                        self.error_message = "expected character \'T\'"
                        state = EnumStates.Error

                elif state == EnumStates.M2:
                    if _str[_pos] == 'e':
                        state = EnumStates.M3
                    else:
                        self.error_message = "expected character \'E\'"
                        state = EnumStates.Error

                elif state == EnumStates.M3:
                    if _str[_pos] == 'p':
                        state = EnumStates.M4
                    else:
                        self.error_message = "expected character \'P\'"
                        state = EnumStates.Error

                elif state == EnumStates.M4:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.N
                        self._step_isapsent = False
                    else:
                        self.error_message = "expected character \'space\' or \'Tab\'"
                        state = EnumStates.Error

                elif state == EnumStates.N:
                    if _str[_pos] == '-':
                        const += _str[_pos]
                        state = EnumStates.O2
                    elif _str[_pos].isdigit() and _str[_pos] != '0':
                        const += _str[_pos]
                        state = EnumStates.O
                    elif _str[_pos] == '0':
                        if self.check_const(_str[pos]):
                            state = EnumStates.O4
                            const = ''
                    else:
                        self.error_message = "expected character \'-\' or number"
                        state = EnumStates.Error

                elif state == EnumStates.O2:
                    if _str[_pos].isdigit() and _str[_pos] != '0':
                        const += _str[_pos]
                        state = EnumStates.O
                    else:
                        self.error_message = 'expected number is unequal to zero'
                        state = EnumStates.Error

                elif state == EnumStates.O4:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.O4
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.L
                    else:
                        self.error_message = 'expected end of line'
                        state = EnumStates.Error

                elif state == EnumStates.O:
                    if _str[_pos].isdigit():
                        const += _str[_pos]
                        state = EnumStates.O
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        if self.check_const(const):
                            state = EnumStates.L
                            const = ''
                        else:
                            state = EnumStates.Error
                    elif _str[_pos] == ' ' or _str[_pos] == '\t':
                        if self.check_const(const):
                            state = EnumStates.O4
                            const = ''
                        else:
                            state = EnumStates.Error
                    else:
                        self.error_message = 'expected number or end of line'
                        state = EnumStates.Error

                elif state == EnumStates.L:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.L
                    elif _str[_pos].isalpha():
                        idn += _str[_pos]
                        state = EnumStates.T
                    else:
                        self.error_message = 'expected letter'
                        state = EnumStates.Error

                elif state == EnumStates.T:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        if self.check_ident(idn):
                            idn = ''
                            state = EnumStates.U1
                        else:
                            state = EnumStates.Error
                    elif _str[_pos].isalnum():
                        idn += _str[_pos]
                        state = EnumStates.T
                    elif _str[_pos] == '=':
                        if self.check_ident(idn):
                            idn = ''
                            state = EnumStates.U
                        else:
                            state = EnumStates.Error
                    else:
                        self.error_message = 'expected letter or number or \'=\''
                        state = EnumStates.Error
                elif state == EnumStates.U1:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.U1
                    elif _str[_pos] == '=':
                        state = EnumStates.U
                    else:
                        self.error_message = 'expected character \'=\''
                        state = EnumStates.Error

                elif state == EnumStates.U:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.U
                    elif _str[_pos] == '-':
                        const += _str[_pos]
                        state = EnumStates.V3
                    elif _str[_pos].isdigit() and _str[_pos] != '0':
                        const += _str[_pos]
                        state = EnumStates.V2
                    elif _str[_pos] == '0':
                        if self.check_const(_str[_pos]):
                            const = ''
                            state = EnumStates.V4
                        else:
                            state = EnumStates.Error
                    elif _str[_pos].isalpha():
                        idn += _str[_pos]
                        state = EnumStates.V
                    else:
                        self.error_message = 'expected letter or number or character \'-\''
                        state = EnumStates.Error

                elif state == EnumStates.V3:
                    if _str[_pos].isdigit() and _str[_pos] != '0':
                        const += _str[_pos]
                        state = EnumStates.V2
                    else:
                        self.error_message = 'expected number'
                        state = EnumStates.Error

                elif state == EnumStates.V2:
                    if _str[_pos].isdigit():
                        const += _str[_pos]
                        state = EnumStates.V2
                    elif _str[_pos] == ' ' or _str[_pos] == '\t':
                        if self.check_const(const):
                            const = ''
                            state = EnumStates.V5
                        else:
                            state = EnumStates.Error
                    elif _str[_pos] in self.math_oper:
                        if self.check_const(const):
                            const = ''
                            state = EnumStates.U
                        else:
                            state = EnumStates.Error
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        if self.check_const(const):
                            const = ''
                            state = EnumStates.X
                        else:
                            state = EnumStates.Error
                    else:
                        self.error_message = 'expected  number or character \'math operation\' or end of line'
                        state = EnumStates.Error

                elif state == EnumStates.V4:
                    if _str[_pos] == ' ':
                        state = EnumStates.V5
                    elif _str[_pos] in self.math_oper:
                        state = EnumStates.U
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.X
                    else:
                        self.error_message = 'expected number or end of line'
                        state = EnumStates.Error

                elif state == EnumStates.V:
                    if _str[_pos].isalpha():
                        idn += _str[_pos]
                        state = EnumStates.V
                    elif _str[_pos] == ' ' or _str[_pos] == '\t':
                        if self.check_ident(idn):
                            idn = ''
                            state = EnumStates.V5
                        else:
                            state = EnumStates.Error
                    elif _str[_pos] in self.math_oper:
                        if self.check_ident(idn):
                            idn = ''
                            state = EnumStates.U
                        else:
                            state = EnumStates.Error
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        if self.check_ident(idn):
                            idn = ''
                            state = EnumStates.X
                        else:
                            state = EnumStates.Error
                    else:
                        self.error_message = 'expected number or letter or math operation or end of line'
                        state = EnumStates.Error

                elif state == EnumStates.V5:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.V5
                    elif _str[_pos] in self.math_oper:
                        state = EnumStates.U
                    elif _str[_pos] == '\n' or _str[_pos] == '\r':
                        state = EnumStates.X
                    else:
                        self.error_message = 'expected math operation or end of line'
                        state = EnumStates.Error

                elif state == EnumStates.X:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.X
                    elif _str[_pos] == 'n':
                        state = EnumStates.X1
                    elif _str[_pos] == 'e':
                        state = EnumStates.Y
                    else:
                        self.error_message = "expected character \'N\' or character \'E\'"
                        state = EnumStates.Error

                elif state == EnumStates.Y:
                    if _str[_pos] == 'x':
                        state = EnumStates.Y2
                    else:
                        self.error_message = "expected character \'X\'"
                        state = EnumStates.Error

                elif state == EnumStates.Y2:
                    if _str[_pos] == 'i':
                        state = EnumStates.Y3
                    else:
                        self.error_message = "expected character \'I\'"
                        state = EnumStates.Error

                elif state == EnumStates.Y3:
                    if _str[_pos] == 't':
                        state = EnumStates.Y4
                    else:
                        self.error_message = "expected character \'T\'"
                        state = EnumStates.Error

                elif state == EnumStates.Y4:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Y5
                    else:
                        self.error_message = "expected character \'space\'"
                        state = EnumStates.Error

                elif state == EnumStates.Y5:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Y5
                    elif _str[_pos] == 'f':
                        state = EnumStates.Y6
                    else:
                        self.error_message = "expected character \'F\'"
                        state = EnumStates.Error

                elif state == EnumStates.Y6:
                    if _str[_pos] == 'o':
                        state = EnumStates.Y7
                    else:
                        self.error_message = "expected character \'O\'"
                        state = EnumStates.Error

                elif state == EnumStates.Y7:
                    if _str[_pos] == 'r':
                        state = EnumStates.Y8
                    else:
                        self.error_message = "expected character \'R\'"
                        state = EnumStates.Error

                elif state == EnumStates.Y8:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Y8
                    elif _str[_pos] == '\r' or _str[_pos] == '\n':
                        state = EnumStates.Y9
                    else:
                        self.error_message = "expected character \'space\' or end of line"
                        state = EnumStates.Error

                elif state == EnumStates.Y9:
                    if _str[_pos] == 'n':
                        state = EnumStates.X1
                    elif _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Y9
                    else:
                        self.error_message = "expected character \'N\'"
                        state = EnumStates.Error

                elif state == EnumStates.X1:
                    if _str[_pos] == 'e':
                        state = EnumStates.X2
                    else:
                        self.error_message = "expected character \'E\'"
                        state = EnumStates.Error

                elif state == EnumStates.X2:
                    if _str[_pos] == 'x':
                        state = EnumStates.X3
                    else:
                        self.error_message = "expected character \'X\'"
                        state = EnumStates.Error

                elif state == EnumStates.X3:
                    if _str[_pos] == 't':
                        state = EnumStates.X4
                    else:
                        self.error_message = "expected character \'T\'"
                        state = EnumStates.Error

                elif state == EnumStates.X4:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Z
                    else:
                        self.error_message = "expected character \'space\' or \'Tab\'"
                        state = EnumStates.Error

                elif state == EnumStates.Z:
                    if _str[_pos] == ' ' or _str[_pos] == '\t':
                        state = EnumStates.Z
                    elif _str[_pos].isalpha():
                        idn += _str[_pos]
                        state = EnumStates.Z1
                    else:
                        self.error_message = "expected letter"
                        state = EnumStates.Error

                elif state == EnumStates.Z1:
                    if _str[_pos] == '\n' or _str[_pos] == ';':
                        if self.check_ident(idn):
                            idn =''
                            state = EnumStates.F
                        else:
                            state = EnumStates.Error
                    elif _str[_pos].isalnum():
                        idn += _str[_pos]
                        state = EnumStates.Z1
                    else:
                        self.error_message = "expected letter or number or end of line"
                        state = EnumStates.Error

                else:
                    state = EnumStates.Error

                _pos += 1
        if state == EnumStates.F:
            if self.inds[0] == self.inds[len(self.inds)-1]:
                flag = True
                self.counting_iteration()
            else:
                self.error_message = 'Names of identifiers following FOR and NEXT must match'
        return flag



