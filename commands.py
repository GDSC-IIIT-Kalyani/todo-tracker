import pickle

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
        self.commands["del"]=self.delete

    def load_data(self):
        try:
            self.dat = pickle.load(open(self.path+"/dat", "rb"))
        except:
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
        for i in range(len(self.dat)):
            print(str(len(self.dat)-i) + " -> " + self.dat[len(self.dat)-i-1])

    def delete(self):
        self.load_data()
        del self.dat[self.del_in-1]
        pickle.dump(self.dat, open(self.path+"/dat", "wb"))
        self.show()

    def get_dict(self):
        return self.commands

   
