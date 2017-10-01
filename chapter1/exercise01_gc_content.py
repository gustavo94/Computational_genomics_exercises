import matplotlib.pyplot as plt
import numpy as np

class GcContent(object):
    GC = 'GC'
    """docstring for GcContent."""
    def __init__(self, window_size):
        super(GcContent, self).__init__()
        self.window_size = window_size
        self.base_count = 0
        self.gc_count = 0
        self.gc_frequency_list = []
        self.curr_window = []
        self.curr_window_gc_count = 0
        self.pivot = 0

    def add_base(self, base):
        if self.base_count < self.window_size:
            self.curr_window.append(base)
            if base in self.GC:
                self.curr_window_gc_count += 1
                self.gc_count += 1
        else:
            self.gc_frequency_list.append(self.curr_window_gc_count / self.window_size)
            if base in self.GC:
                self.curr_window_gc_count += 1
                self.gc_count += 1
            if self.curr_window[self.pivot] in self.GC:
                self.curr_window_gc_count -= 1
            self.curr_window[self.pivot] = base
            self.gc_frequency_list.append(self.curr_window_gc_count / self.window_size)
            self.pivot = (self.pivot + 1) % self.window_size
        self.base_count += 1

    def plot_frequency_list(self):
        plt.plot(np.array(self.gc_frequency_list))
        plt.ylabel('GC Frequency for window size %d' % self.window_size)
        plt.show()

    def print_frequency(self):
        print(self.gc_count / self.base_count)

def main():
    filename = 'data/NC_001416.fasta'
    window_size = 10
    gc_content = GcContent(window_size)
    GCAT = 'GCAT'
    with open(filename) as f:
        next(f)
        for line in f:
            for base in line:
                if base in GCAT:
                    gc_content.add_base(base)
            break

    gc_content.print_frequency()
    gc_content.plot_frequency_list()

if __name__ == '__main__':
    main()
