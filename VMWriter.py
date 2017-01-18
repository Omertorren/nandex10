class VMWriter:
    def __init__(self, path):
        self.path = path
        self.lines = list()

    def write_push(self, segment, index):
        pass

    def write_pop(self, segment, index):
        pass

    def write_arithmetic(self, command):
        pass

    def generate_label(self, name):
        pass

    def write_label(self, label):
        self.lines.append('label %s\n' % label)

    def write_go_to(self, label):
        pass

    def write_if(self, label):
        pass

    def write_call(self, name, n_args):
        pass

    def write_function(self, name, n_locals):

        pass

    def write_return(self):
        pass

    def close(self):
        vm_file = open(self.path, 'w')
        for line in self.lines:
            vm_file.write(line)
        vm_file.close()