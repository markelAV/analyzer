from kivy.app import App
from kivy.uix.label import Label
from venv import analyzer
from venv import anlyser2
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


class Root(BoxLayout):

    input = ObjectProperty()
    output = ObjectProperty()
    out_list = ObjectProperty()
    anlyz = analyzer.Analyzer()

    def out(self):
        self.output.text = ''
        self.out_list.text = ''
        self.anlyz.error_message = 'ERROR'
        print(self.input.text)
        s = self.input.text
        lines = s.split('\n')
        kod = []
        i = 0
        while i < len(lines) and len(lines) > 1:
            if len(lines[i]) != 0:
                kod.append(lines[i])
            i += 1
        b = self.anlyz.main_analyzer_method(kod)
        if not b:
            str_buf = ', '.join(self.anlyz.inds)
            output_list = "Список индедификаторов: [" + str_buf + '].\nСписок констант: ['
            str_buf = ''
            for i in self.anlyz.consts:
                str_buf += ' ' + str(i)
            output_list += str_buf + '].'
            self.output.text = "Good"
            self.out_list.text = output_list
        else:
            self.output.text = self.anlyz.error_message



class CustomLayout(FloatLayout):
    def out(self):

        self.output_Error.text = str("Error")


class AnalyserApp(App):
    def build(self):
        root = Root()
        return root

    def testing(self):
        print("Hello world")
        anlyz = analyzer.Analyzer()
        # anlyz.analyze_code()
        numbers = {"-32768", "-32767", "32767", "32766", "-123", "123", "38213", "23h21", "7", "123456432"}
        identifier = {"i", "J", "Tsdf", "dLKJs", "2df", "d3", "df.a"}
        line1 = "FOR J12 = 85 TO 100 "
        line2 = "FOR I =1 TO 10 STEP 2"
        line3 = "FOR BL = 1 TO 10 STEP -2"
        line1e = "FOR I =1 TO 10 STEP "
        _2line1 = "A = 18 * A"
        _2lline2 = "h = -386  + AX * 5 + ty"
        _2line3 = "Z8 = 0"
        lines = {line1, line2, line3, line1e}  # bag with line3!!!!!
        _2lines = {_2line1, _2lline2, _2line3}
        for i_line in _2lines:
            if not anlyz.parse_second_line(i_line):
                print(i_line, "  is ok")
            else:
                print(i_line, "  is not ok")
        exit = "EXIT FOR "
        nextq = " NEXT   R1"
        t = len(exit)
        if not anlyz.parse_fourth_line(nextq):
            print(nextq, " - is ok")
        else:
            print(nextq, " - is not ok")
        mline = [line2, _2line1, exit, nextq]
        if not anlyz.main_analyzer_method(mline):
            print("good")
        else:
            print("bad")

if __name__ == '__main__':
    #AnalyserApp().run()
    '''anlyz = analyzer.Analyzer()

    numbers = {"-32768", "-32767", "32767", "32766", "-123", "123", "38213", "23h21", "7", "123456432"}
    identifier = {"i", "J", "Tsdf", "dLKJs", "2df", "d3", "df.a"}
    line1 = "FOR J12 = 85 TO 100 "
    line2 = "FOR I =1 TO 10 STEP 2"
    line3 = "FOR BL = 1 TO 10 STEP -2"
    line1e = "FOR I =1 TO 10 STEP "
    _2line1 = "A = 18 * A"
    _2lline2 = "h = -386  + AX * 5 + ty"
    _2line3 = "Z8 = 0"
    lines = {line1, line2, line3, line1e}  # bag with line3!!!!!
    _2lines = {_2line1, _2lline2, _2line3}
    exit = "EXIT FOR "
    nextq = " NEXT   I"
    mline = [line2, _2line1, exit, nextq]
    if not anlyz.main_analyzer_method(mline):
        print("good")
        s = "Indedificators: "
        s += str(anlyz.inds)
        print(s)
    else:
        print("bad")
'''
    line1 = "FOR J1 = 1 TO 10 STEP 1 \n q=n+1 \n EXIT FOR \n NEXT J1;  "
    an = anlyser2.Anlyser(line1)
    flag = an.control()
    if flag:
        print("good")
        print(an.error_message)
        print(an.inds)
        print(an.consts)
    else:
        print("bad")
        print(an.error_message)


