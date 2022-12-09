import os
import sys
import functools

curr_dir = os.path.dirname(os.path.realpath(__file__))
input_file = f"{curr_dir}/07input.txt"

class File:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
    def __str__(self):
        return f"- {self.name} (file, size={self.size})"
    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return hash(self.name)

class Dir:
    def __init__(self, name):
        self.name = name
        self.dirs = set()
        self.files = set()

    def __str__(self):
        s=f"- {self.name} (dir)"
        for r in self.dirs.union(self.files):
            for line in r.__str__().split("\n"):
                s += f"\n  {line}"
        return s

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def insert(self, record):
        if isinstance(record, Dir):
            self.dirs.add(record)
        else:
            self.files.add(record)
        record.parent = self

    def total_size(self):
        return sum([0] + [d.total_size() for d in self.dirs] + [f.size for f in self.files])
    
    def get_sum(self, max):
        s = 0
        ts = self.total_size()
        if ts <= max:
            s += ts
        for d in self.dirs:
            s += d.get_sum(max)
        return s

    def get_size_to_delete(self, min_size):
        sts = self.total_size()
        if sts < min_size:
            return -1
        if len(self.dirs) == 0:
            return sts
        dir = self
        min_ts = sts
        for d in self.dirs:
            dts = d.get_size_to_delete(min_size)
            if dts > 0 and dts >= min_size and dts < min_ts:
                dir = d
                min_ts = dts
        return min_ts



def get_tree(file):
    with open(file, "r") as f:
        content = "".join(f).split("$ ")
        cur_dir = Dir("/")
        for section in content[1:]:
            # print(cur_dir.name)
            lines = section.split("\n")
            command = lines[0].split(" ")
            # print(command)
            if command[0] == "cd":
                dir_name = command[1]
                if dir_name != "..":
                    child_dir = Dir(dir_name)
                    cur_dir.insert(child_dir)
                    cur_dir = child_dir
                else:
                    cur_dir = cur_dir.parent
            else:
                for line in lines[1:]:
                    line_content = line.split(" ")
                    if len(line_content) == 2:
                        dir_or_size = line_content[0]
                        name = line_content[1]
                        if dir_or_size != "dir":
                            cur_dir.insert(File(name, int(dir_or_size)))                       
        while cur_dir.name != "/":
            cur_dir = cur_dir.parent
        return cur_dir

root_dir = get_tree(input_file)
print(root_dir.get_sum(100000))
total_fs_size = 70000000
space_needed = 30000000
print(root_dir.get_size_to_delete(space_needed - (total_fs_size - root_dir.total_size())))
