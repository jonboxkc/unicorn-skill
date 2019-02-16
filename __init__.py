from mycroft import MycroftSkill, intent_file_handler


class Unicorn(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('unicorn.intent')
    def handle_unicorn(self, message):
        self.speak_dialog('unicorn')


def create_skill():
    return Unicorn()

