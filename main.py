
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('CalculatorApp.kv')
# Builder.load_string(''' copy builder file text here ''')

class CalculatorApp(Widget):
    def clear(self):
        self.ids.calc_input.text ="0"

    def button_press(self, button):
        # create a variable that contains whatever in the text box
        prior = self.ids.calc_input.text
        # Test for Error first
        if "Error" in prior:
            prior = ''

        # if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
    # create function remove last character in text box
    def remove(self):
        prior = self.ids.calc_input.text
        # Remove the last item in the text box
        prior = prior[:-1]
        # Output back to the text box
        self.ids.calc_input.text = prior

    # Create function to make text box positive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Test to see if there is a - sign
        if "-" in prior:
            self.ids.calc_input.text=f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior.replace("-", "")}'







    # character in text box

    # create decimal number
    def dot(self):
        prior = self.ids.calc_input.text
        # Split out the text box by +
        num_list = prior.split("+")
        num_list[-1]
        if "+" in prior and "." not in num_list[-1] :
            # add a decimal to the end fo the test
            prior = f'{prior}.'
            # outbox back to the text
            self.ids.calc_input.text = prior

        elif "." in prior:
            pass
        else:
            # add a decimal to the end fo the test
            prior = f'{prior}.'
            # outbox back to the text
            self.ids.calc_input.text = prior



    def math_sign(self,sign):
        # create a variable that contains whatever in the text box
        prior = self.ids.calc_input.text
        # slap a + sign
        self.ids.calc_input.text =f'{prior}{sign}'



    # creat equals
    def equals(self):
        prior = self.ids.calc_input.text
        # Error Handling
        try:
            # Evaluate the math from the text box
            answer = eval(prior)
            # Output the answer
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"







        # if "+" in prior:
        #     num_list= prior.split("+")
        #     answer = 0.0
        #     # loop through the list
        #     for number in num_list:
        #         answer= answer + float(number)
        #     # print answer in text box
        #     self.ids.calc_input.text = str(answer)




class Calculator(App):
    def build(self):
        return CalculatorApp()

if __name__ == '__main__':
    Calculator().run()

