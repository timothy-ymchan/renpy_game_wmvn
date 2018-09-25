init python:
    #This statement format title string
    import re
    def TITLE(str):
        return "{size=80}{color=#ffffff}"+ str+"{/color}{/size}"

    def load_nl(self,name_list):
        self.name_list = name_list
        self.name_count = 0
        self.name = name_list[0]
    def next_name(self):
        if(self.name_count<len(self.name_list)-1):
            self.name_count += 1
            self.name = self.name_list[self.name_count]

    ADVCharacter.next_name = next_name
    ADVCharacter.load_names = load_nl

    class ScriptLoader:
        script_dir = 'scripts/'
        def __init__(self):
            self.dates = self.get_dates()
            self.load_date(self.dates[0])

        def get_dates(self):
            file_list = [file for file in renpy.list_files() if ScriptLoader.script_dir in file]
            dates = [dir.split('/')[1] for dir in file_list if '.' not in dir.split('/')[1]]
            dates = list(set(dates))
            return sorted(dates)

        def get_current_day(self):
            return self.dates[self.current_day]

        def get_next_day(self):
            next_day = self.current_day
            if(self.current_day < len(self.dates)-1):
                next_day += 1
                return self.dates[next_day]
            return ''

        def load_date(self,date):
            if(date in self.dates):
                self.current_day = self.dates.index(date)
                log_path = '/'.join([ScriptLoader.script_dir,date,"run_order.txt"])
                run_order = [map(lambda i:re.sub('\r\n','',i),line.split(':')) for line in renpy.file(log_path)]
                self.event_list = [e[1] for e in sorted(run_order)]
            else:
                raise IndexError('The date passed is not in dates list!')

        def get_next_event(self):
            if(len(self.event_list) != 0):
                return self.event_list.pop(0)
            return ''
