init python:
    #This statement format title string
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
