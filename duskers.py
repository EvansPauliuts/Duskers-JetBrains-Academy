# Write your code here
from art_text import text_art_dusk


class DuskCommander:
    def __init__(self):
        pass

    @staticmethod
    def play_command():
        name_input = input('\nEnter your name:\n')

        print(f'\nGreetings, commander {name_input}!')
        print('Are you ready to begin?')
        print('    [Yes] [No]')

    @staticmethod
    def no_command():
        print('\nHow about now.')
        print('Are you ready to begin?')
        print('    [Yes] [No]')

    @staticmethod
    def exit():
        print('\nThanks for playing, bye!')
        exit()

    def run(self):
        text_art_dusk()
        print('\n[Play]')
        print('[exit]')

        while True:
            user_input = input('\nYour command:\n')

            if user_input in ('play', 'Play', 'pLAY', 'PLAY'):
                self.play_command()
                continue
            elif user_input in ('no', 'No', 'NO', 'nO'):
                self.no_command()
                continue
            elif user_input in ('yes', 'Yes', 'yES', 'YES'):
                print('\nGreat, now let\'s go code some more ;)')
                exit()
            elif user_input == 'exit':
                self.exit()


def main():
    dusk_commander = DuskCommander()
    dusk_commander.run()


if __name__ == '__main__':
    main()
