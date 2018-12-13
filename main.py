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


    def out(self):
        self.output.text = ''
        self.out_list.text = ''
        s = self.input.text+';'
        anlyz = anlyser2.Anlyser(s)

        b = anlyz.control()
        if b:
            str_buf = ', '.join(anlyz.inds)
            output_list = "Список индедификаторов: [" + str_buf + '].\nСписок констант: ['
            str_buf = ''
            for i in anlyz.consts:
                str_buf += ' ' + str(i)
            output_list += str_buf + '].\n'
            output_list += 'Колчество проходов цикла = '
            if anlyz._count_iteration >=0:
                output_list += str(anlyz._count_iteration)
            else:
                output_list += 'Бесконечно'
            self.output.text = "Good"
            self.out_list.text = output_list
        else:
            self.output.text = anlyz.error_message



class CustomLayout(FloatLayout):
    def out(self):

        self.output_Error.text = str("Error")


class AnalyserApp(App):
    def build(self):
        root = Root()
        return root



if __name__ == '__main__':
    AnalyserApp().run()
