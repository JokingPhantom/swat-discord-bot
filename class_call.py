#!/usr/bin/python

# Class responsible for keeping track of a class call's information.
# A class call contains information related to a game's setup, such as
# players' classes, mode, leader, etc.
import tabulate

ACCEPTABLE_FORMATS = ['default', 'grid']
GRID_HEADERS = ['position', 'name', 'class']

class ClassCall:
    def __init__(self):
        self.format = 'default'
        self.leader = None
        self.mode = None
        self.lock = False
        self.data = []
        self.lock_timer = 900
        self.time_since_last_call = 0
        self.class_call_used = False
        print("Class Call initialized")

    def receive_call(self, name, match):
        if self.lock is True:
            return
        position = match.group('position')
        matched_name = match.group('name')
        call = next(filter(lambda x: x['position'] == position, self.data), None)
        if not call:
            call = {}
        else:
            self.data.remove(call)
        call['position'] = position
        call['name'] = name
        call['class'] = matched_name.replace('/', '')[0:50].strip()
        if matched_name and not matched_name.isspace():
            self.data.append(call)
        self.class_call_used = True
        self.time_since_last_call = 0
        self.data.sort(key=lambda x: x['position'])

    def swap(self, pos1, pos2):
        call1 = next(filter(lambda x: x['position'] == pos1, self.data), None)
        call2 = next(filter(lambda x: x['position'] == pos2, self.data), None)
        if call1 and call2:
            call1['position'] = pos2
            call2['position'] = pos1
        elif call1:
            call1['position'] = pos2
        elif call2:
            call2['position'] = pos1
        self.data.sort(key=lambda x: x['position'])

    def import_cc(self, cc):
        self.data = []
        calls = cc.split('/')

        try:
            for index, call in enumerate(calls, start=1):
                if call == '/':
                    break
                self.data.append({'position': index, 'name': '', 'class': call})
        except:
            return False
        self.time_since_last_call = 0
        self.class_call_used = True
        return True

    def set_format(self, input):
        if input not in ACCEPTABLE_FORMATS:
            return 'Unsupported format. Accepted formats are: {}'.format(ACCEPTABLE_FORMATS)
        else:
            self.format = input
            return None

    def export(self, format=None):
        print('{}'.format(format))
        format = self.format if not format else format
        if format == 'default':
            result = []
            calls = []
            if self.mode:
                result.append('Mode: {},'.format(self.mode))
            if self.leader:
                result.append('Leader: {},'.format(self.leader))
            for i in range(1, 10):
                call = next(filter(lambda x: int(x['position']) == i, self.data), None)
                if call:
                    calls.append(call['class'] or call['position'])
                else:
                    calls.append(str(i))
            call_seperator = '/'
            result_seperator = ' '
            if result:
                result.append('Calls: {}'.format(call_seperator.join(calls)))
            else:
                result.append(call_seperator.join(calls))
            return result_seperator.join(result)
        if format == 'grid':
            rows = [x.values() for x in self.data]
            return "```" + tabulate.tabulate(rows, GRID_HEADERS, tablefmt='grid') + "```"

    def __str__(self):
        return self.export()
    