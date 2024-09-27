class TO_DO:
    def __init__(self):
        self.lis=[]
        print('Welcome to Todo List')

    def add(self):
        Choice= input('What You Want To ADD : ').title()
        if Choice in self.lis:
            print('Task ALready in list ')
        else:
            self.lis.append(Choice)
            print('Your Task has been added in list')
    def Show(self):
        if not  self.lis:
            print('NO task in list to show')
        else:
            for idx,task in enumerate(self.lis,start =1):
                print(f'{idx}: {task}')
    def DELS(self):
        self.Show()
        if self.lis:
            try:
                task_num=int(input('Which Task you want to delete from Avobe: '))
                if 1<= task_num <= len(self.lis):
                    removed_task=self.lis.pop(task_num-1)
                    print(f'Task:- {removed_task} has been removed from list')
                else:
                    print('Please Enter valid Number ')
            except ValueError:
                print('Enter A Valid Number ')       
    def Exit(self):
        print('Thanks For Using Todo List ')
        return True
    
    def Choices(self):
        while True:
            print('\nMenu')
            print('1. Add Task')
            print('2. Show Task')
            print('3. Delete Task')
            print('4. Exit')
            
            try:                
                li=int(input('Enter Your Choices: '))
                if li ==1:
                    self.add()
                elif li==2:
                    self.Show()
                elif li == 3:
                    self.DELS()
                
                elif li==4:
                    if self.Exit():
                        break
                else:
                    print('Incorrect Number Try agian ')
            except ValueError:
                print('Enter A Valid Number')
if __name__ == '__main__':             
    todo=TO_DO()
    todo.Choices()
        
        
