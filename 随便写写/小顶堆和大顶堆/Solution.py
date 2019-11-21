class MaxHeap(object):
    def __init__(self):
        self._data = []#堆
        self._count = 0#索引
    def size(self):
        return self._count
    def isEmpty(self):
        return self._count == 0
    def add(self,x):
        '''
        1.先把数据当作最后一个节点添加到堆的最后
        2.判断当前节点和其父节点的大小，如果当前结点比父节点大，就交换两个节点的位置，继续往上比较，直到小于父节点或者是根结点（_shiftup中实现逻辑）
        3.x:需要加入大顶堆中的元素，return：调整后的大顶堆
        '''
        self._data.append(x)
        self._shiftup(self._count)#传入的是新加入节点的索引
        self._count += 1
    def pop(self):
        """
        从最大堆中弹出根节点，该元素肯定是这个堆中最大的元素；调整堆的结构使得新的堆仍是一个最大堆：
        1. 首先弹出根节点（也就是索引为0的元素），然后把最后一个叶子节点放到根节点位置
        2. 从根节点开始，比较其与两个子节点的大小：当当前节点小于其子节点时，则将当前节点与较大的一个子节点交换位置，然后继续往下比较，直到当前节点是叶子节点或者当前节点大于子节点
        :return: 返回调整后的最大堆
        """
        if self._count:
            ret = self._data[0]
            self._data[0] = self._data[-1]
            self._count -= 1
            self._shiftdown(0)#传入弹出的索引
            return ret
    def _shiftup(self,index):
        parent = (index - 1) >> 1#因为根结点的索引是0
        while index > 0 and self._data[index] < self._data[parent]:
            self._data[index],self._data[parent] = self._data[parent],self._data[index]
            index = parent
            parent = (index - 1) >> 1
    def _shiftdown(self,index):
        max_child = (index << 1) + 1
        if max_child + 1 and max_child < max_child + 1:
            max_child = max_child + 1
        if self._data[index] < self._data[max_child]:
            self._data[index] ,self._data[max_child] = self._data[max_child],self._data[index]
            index = max_child
            max_child = (index << 1) + 1
        else:
            break
