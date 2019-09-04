import re
import math
class Tbl(object):
    def __init__(self):
        self.oid = 1
        self.cols = []
        self.rows = []
        self.index = 1
        self.skipCol = []

    def compiler(self, x):
        "return something that can compile strings of type x"
        try:
            int(x); return int
        except:
            try:
                float(x); return float
            except ValueError:
                return str

    def string(self, s):
        "read lines from a string"
        for line in s.splitlines():
            yield line

    def row(self, src, sep=",", doomed=r'([\n\t\r ]|#.*)'):
        "convert lines into lists, killing whitespace and comments"
        for line in src:
            line = line.strip()
            line = re.sub(doomed, '', line)
            if line:
                yield line.split(sep)

    def cells(self, src):
        "convert strings into their right types"
        oks = None
        for n, cells in enumerate(src):
            if n == 0:
                yield cells
            else:
                oks = [self.compiler(cell) for cell in cells]
                yield [f(cell) for f, cell in zip(oks, cells)]

    def fromString(self, s):
        "putting it all together"
        for lst in self.cells(self.row(self.string(s))):
            yield lst

    def createCols(self, lst):
        for index, col in enumerate(lst):
            if "?" in col:
                self.skipCol.append(index)
            else:
                self.index += 1
                self.cols.append(Col(self.index, index, col))

    def createRows(self, lst):
        self.index += 1
        cells = []
        i = 0
        for index, row in enumerate(lst):
            if index not in self.skipCol:
                cells.append(row)
                if row != "?":
                    self.cols[index-i].num.__add_num__(row)
            else:
                i+=1
        if len(self.cols) != len(cells):
           # print("!!! ***Row doesnt have enough cells*** !!!")
            self.rows.append(Row(self.index, None,True))
            for index, row in enumerate(lst):
                if row != "?":
                    self.cols[index].num.__remove_num__(row)
        else:
            self.rows.append(Row(self.index, cells,False))


    def print (self):
        print("PART 3:")
        print()
        print("t.cols")
        for index, col in enumerate(self.cols):
            print("| %d" %(index+1))
            print("|  | col: %d" % (index+1))
            print("|  | hi: %d" % self.cols[index].num.high)
            print("|  | low: %d" % self.cols[index].num.low)
            print("|  | m2: %f" % self.cols[index].num.m2)
            print("|  | mu: %f" % self.cols[index].num.mu)
            print("|  | sd: %f" % self.cols[index].num.sd)
            print("|  | oid: %d" % self.cols[index].oid)
            print("|  | text: " + self.cols[index].text)
        print("t.oids: %d"% self.oid)
        print("t.rows")
        for index, row in enumerate(self.rows):
            if(not row.skipped):
                print("| %d" %(index+1))
                print("|  | cells")
                for index,cell in enumerate(row.cells):
                    print("|  | |  %d : %s" % ((index + 1),str(cell)))
                print("|  | oid: %d" % row.oid)

    def readAndCreate(self):
        s = """
    $cloudCover, $temp, ?$humid, <wind,  $playHours
    100,        68,    80,    0,    3   # comments
      0,          85,    85,    0,    0

     0,          80,    90,    10,   0
     60,         83,    86,    0,    4
      100,        70,    96,    0,    3
      100,        65,    70,    20,   0
      70,         64,    65,    15,   5
      0,          72,    95,    0,    0
      0,          69,    70,    0,    4
    ?,          75,    80,    0,    ? 
    0,          75,    70,    18,   4
    60,         72   
     40,         81,    75,    0,    2
  100,        71,    91,    15,   0
    """
        print("PART 1:")
        for lst in self.fromString(s):
            print(lst)

        print()
        print("PART 2:")
        for index, lst in enumerate(self.fromString(s)):
            if index == 0:
                self.createCols(lst)
            else:
                self.createRows(lst)

        for col in self.cols:
            print(col.text+",", end =" "),
        print()
        for index , row in enumerate(self.rows):
            if row.skipped:
                print ("E> skipping line %d" %(index+1))
            else:
                print(row.cells)
        print()

        return self




class Num(object):
    def __init__(self):
        self.low = 10 ** 32
        self.high = -1 * (self.low)
        self.sd = 0
        self.m2 = 0
        self.mu = 0
        self.col_count = 0

    def __add_num__(self, n):
        self.col_count += 1
        self.low = min(n, self.low)
        self.high = max(n, self.high)
        delta = n - self.mu;
        self.mu += delta / self.col_count
        delta2 = n - self.mu
        self.m2 += delta * delta2
        self.get_standard_deviation()

    def get_standard_deviation(self):
        if self.m2 < 0 or self.col_count < 2:
            self.sd = 0;
        else:
            self.sd = math.sqrt((self.m2 / (self.col_count - 1)));

    def __remove_num__(self, n):
        self.col_count -= 1
        if self.col_count < 2:
            self.sd = 0
        else:
            delta = n - self.mu;
            self.mu -= delta / self.col_count
            delta2 = n - self.mu
            self.m2 -= delta * delta2
            self.get_standard_deviation()

class Row(object):
  def __init__(self,oid,cells,skip):
    self.oid = oid
    self.cells = cells
    self.cooked = []
    self.dom = 0
    self.skipped = skip

class Col(object):
  def __init__(self, oid,col,text):
    self.oid = oid
    self.col = col
    self.text = text
    self.num = Num()

if __name__=="__main__":
    Tbl().readAndCreate().print()



