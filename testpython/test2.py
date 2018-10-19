#最短路径问题
def mathSortRoad(twoDimensionList):
    siz = len(twoDimensionList)
    list1 = []
    list1.append({'x':0,'y':0,'value':twoDimensionList[0][0]})
    for i in range(0,siz*2-2,1):
        list2 = []
        for obj in list1:
            if obj.get('x') < siz-1:
                obj1={}
                obj1['x'] = obj.get('x')+1
                obj1['y'] = obj.get('y')
                obj1['value'] = obj.get('value')+twoDimensionList[obj1.get('x')][obj1.get('y')]
                list2.append(obj1)
            if obj.get('y') < siz-1:
                obj2={}
                obj2['x'] = obj.get('x')
                obj2['y'] = obj.get('y')+1
                obj2['value'] = obj.get('value')+twoDimensionList[obj2.get('x')][obj2.get('y')]
                list2.append(obj2)
        list1 = list2
    print('一共有'+str(len(list1))+'条路径')
    result =  list1[0].get('value')
    for obj in list1:
        if result > obj.get('value'):
            result = obj.get('value')
    return result

print(mathSortRoad([[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]))

