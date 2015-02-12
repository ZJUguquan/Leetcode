class Automaton(object):

    def __init__(self):
        self.states = []

    def read_commands(self, commands):
        _state = 'q1'
        for idx, c in enumerate(commands):
            if _state == 'q1' and c == '1':
                _state = 'q2'
            elif _state == 'q1' and c == '0':
                continue
            elif _state == 'q2' and c == '0':
                _state = 'q3'
            elif _state == 'q2' and c == '1':
                continue
            else:
                _state = 'q2'
            print(_state, '-', idx)
        return True if _state == 'q2' else False

my_automaton = Automaton()

a = Automaton()
cs = ['1', '0', '0' ,'1']
print(a.read_commands(cs))