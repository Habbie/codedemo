import sys, random, unittest

def findCoincident(a, b):
    ret=[]
    for x in xrange(0, min(len(a), len(b))):
        if(a[x]==b[x]):
            ret.append(x)

    return ret

def populateLists(a,b):
    for x in range(0, 100000):
        a.append(random.randrange(65536))
        b.append(random.randrange(65536))

class TestCoincident(unittest.TestCase):
    def test_empty(self):
        res = findCoincident([], [])
        self.assertTrue(len(res)==0)

    def test_noMatches(self):
        res = findCoincident([1,2,3], [4,5,6])
        self.assertTrue(len(res)==0)

    def test_allMatches(self):
        res = findCoincident([1,2,3], [1,2,3])
        self.assertTrue(res==[0,1,2])

    def test_diffLength(self):
        res = findCoincident([1,2], [1,2,3,4])
        self.assertTrue(res==[0,1])

    def test_large(self):
        r = range(0,1000000)
        res = findCoincident(r,r)
        self.assertTrue(r==res)

    def test_diffLength2(self):
        res = findCoincident([1,2,3,4], [1,2])
        self.assertTrue(res==[0,1])

if __name__ == '__main__':
    unittest.main()