# coding: utf-8

"""
Task2. Mediator. Meeting in a company
"""


class Participant(object):
    def invite(self):
        raise NotImplementedError()

    def not_invite(self):
        raise NotImplementedError()


class AllWorkers(Participant):
    def invite(self):
        print('All workers will be on the meeting')

    def not_invite(self):
        print('All workers won`t be on the meeting')


class HeadsOfDepartments(Participant):
    def invite(self):
        print('Heads of departments will be on the meeting')

    def not_invite(self):
        print('Heads of departments won`t be on the meeting')


class CTO(Participant):
    def invite(self):
        print('CTO will be on the meeting')

    def not_invite(self):
        print('CTO won`t be on the meeting')


class MeetingMediator(object):
    def __init__(self):
        self.commands = dict.fromkeys(['all', 'head', 'cto'])

    def invite(self, win):
        for window in self.commands.values():
            if window not in win:
                window.not_invite()
            else:
                window.invite()

    def set_all(self, win):
        self.commands['all'] = win

    def set_heads(self, win):
        self.commands['head'] = win

    def set_cto(self, win):
        self.commands['cto'] = win


def main():
    all_workers = AllWorkers()
    heads = HeadsOfDepartments()
    cto = CTO()

    med = MeetingMediator()
    med.set_all(all_workers)
    med.set_heads(heads)
    med.set_cto(cto)

    med.invite([all_workers, heads])
    print()
    med.invite([heads, cto])
    print()
    med.invite([all_workers, heads, cto])


if __name__ == '__main__':
    main()
