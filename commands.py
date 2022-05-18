import pickle
import os

class Commands:

    def __init__(self, path, task):
        self.task = {}
        self.path = path
        self.dat = []
        try:
            self.del_in = int(task[0])
        except:
            pass
       
        self.task = task
        self.commands = {}

        self.commands["store"] = self.store
        self.commands["purge"] = self.purge
        self.commands["show"] = self.show
        self.commands["delete"]=self.delete
        self.commands["search"] = self.search
        self.commands["exit"] = self.exit
        self.commands["cd"] = self.cd
        self.commands["ls"] = self.ls

    def exit(self):
        exit()


    def load_data(self):
        try:
            if os.path.isfile(self.path+"/dat"):
                self.dat = pickle.load(open(self.path+"/dat", "rb"))
            else:
                self.dat = []
                pickle.dump(self.dat,open(self.path+"/dat", "wb"))
        except Exception as e:
            print(e)
            self.dat = []
            pickle.dump(self.dat,open(self.path+"/dat", "wb"))


    def store(self):
        
        self.load_data()

        coods = self.dat
        path = self.path
        task = " ".join(self.task)
        tasks = pickle.load(open(path+"/dat", "rb"))

        try:
            tasks.append(task)
        except KeyError:
            tasks = [task]
       
        pickle.dump(tasks, open(path+"/dat", "wb"))
        return 1

    def purge(self):       
        pickle.dump([], open( self.path+"/dat", "wb"))
        return 1

    def show(self):
        self.load_data()
        if len(self.dat) == 0:
            print("Empty!")
        else:
            for i in range(len(self.dat)):
                print(str(len(self.dat)-i) + " -> " + self.dat[len(self.dat)-i-1])

    def delete(self):
        self.load_data()
        del self.dat[self.del_in-1]
        pickle.dump(self.dat, open(self.path+"/dat", "wb"))
        self.show()

    def search(self):
        self.load_data()

        que =  " ".join(self.task)
        j = 0

        for i in range(len(self.dat)):
            word = self.dat[len(self.dat)-i-1]
            if word.find(que) != -1:
                j += 1
                print(str(len(self.dat) - i) + " -> " + word, end = "\n")
            
        if j == 0:
            print("No matches found !!")

    def get_dict(self):
        return self.commands

    def cd(self):
        self.load_data()
        os.system("echo -n %s > curr_dir"%self.task[0])

    def ls(self):
        self.load_data()
        dirs = os.listdir(self.path+"/../")
        curr_dir = self.path.split('/')[-1]
        if 'debug' in dirs:
            dirs.remove('debug')
        if 'dummy' in dirs:
            dirs.remove('dummy')
        for dir in dirs:
            if dir == curr_dir:
                print(dir+" <---- curr")
            else:
                print(dir)
