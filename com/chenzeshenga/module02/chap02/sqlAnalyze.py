def loadData():
    employeeData = {"staff_id": [], "name": [], "age": [], "phone": [], "dept": [], "enroll_date": []}
    file = open("employee.txt", "r", encoding="utf-8")
    for line in file:
        strArray = line.strip().split(",")
        employeeData["staff_id"].append(strArray[0])
        employeeData["name"].append(strArray[1])
        employeeData["age"].append(strArray[2])
        employeeData["phone"].append(strArray[3])
        employeeData["dept"].append(strArray[4])
        employeeData["enroll_date"].append(strArray[5])
    # print(employeeData)
    file.close()
    return employeeData


def addData(sql, employeeData):
    if "staff_table" in sql:
        data = sql.replace("add staff_table ", "")
        staffData = data.split(",")
        if staffData[2] in employeeData["phone"]:
            print("phone %s 已存在，插入数据失败，请重新输入" % staffData[2])
        else:
            addedData = str(int(employeeData["staff_id"][-1]) + 1) + "," + data
            # print(addedData)
            file = open("employee.txt", "a", encoding="utf-8")
            file.write(addedData + "\n")
            file.close()
            print("插入了一条数据 %s" % addedData)
    else:
        print("数据表%s不存在" % sql.split(" ")[1])


def delData(sql, employeeData):
    id = sql.split("where")[1].split("=")[1].strip()
    # print(id)
    if id in employeeData["staff_id"]:
        file = open("employee.txt", "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        file = open("employee.txt", "w", encoding="utf-8")
        for line in lines:
            if id == line.split(",")[0]:
                continue
            else:
                file.write(line)
        file.close()
        print("已成功删除一条记录, id 为 %s" % id)
    else:
        print("当前id %s 不存在，请重新输入" % id)


def updateData(sql, employeeData):
    lines = analyzeWhere(sql.split("where")[1].strip())
    # print(lines)
    setData = sql.split(" ")[3].split("=")
    # print(setData)
    for index in lines:
        employeeData[setData[0]][index] = setData[1].replace("\"", "")
    file = open("employee.txt", "w", encoding="utf-8")
    file.truncate()
    i=0
    for id in employeeData["staff_id"]:
        str = employeeData["staff_id"][i] + ","+employeeData["name"][i] + ","+employeeData["age"][i] + ","+employeeData["phone"][i] + ","+employeeData["dept"][i] + ","+employeeData["enroll_date"][i] + "\n"
        file.write(str)
        i+=1
    file.close()
    print("更新结果如下，总共更新%s条记录：" % len(lines))


def findData(sql, employeeData):
    lines = analyzeWhere(sql.split("where")[1].strip())
    # print(lines)
    columns = sql.split(" ")[1]
    print("查询结果如下，总共查询到%s条记录：" % len(lines))
    if columns == "*":
        for k in lines:
            print(lines[k], end="")
    else:
        print(columns)
        columnArray = columns.split(",")
        for index in lines:
            for column in columnArray:
                print(employeeData[column][index], end="\t")
            print("\n", end="")


def analyzeWhere(sentence):
    id = []
    if ">" in sentence:
        condition = sentence.split(">")
        condition[0] = condition[0].strip()
        condition[1] = condition[1].strip()
        # print(condition)
        i = 0
        for data in employeeData[condition[0]]:
            if int(data) > int(condition[1]):
                # print(privateID)
                id.append(i)
            i += 1
        # print(id)
    elif "<" in sentence:
        condition = sentence.split("<")
        condition[0] = condition[0].strip()
        condition[1] = condition[1].strip()
        # print(condition)
        i = 0
        for data in employeeData[condition[0]]:
            if int(data) < int(condition[1]):
                id.append(i)
            i += 1
        # print(id)
    elif "=" in sentence:
        condition = sentence.split("=")
        condition[0] = condition[0].strip()
        condition[1] = condition[1].strip().replace("\"", "")
        # print(condition)
        i = 0
        for data in employeeData[condition[0]]:
            if data == condition[1]:
                id.append(i)
            i += 1
        # print(id)
    elif "like" in sentence:
        condition = sentence.split("like")
        condition[0] = condition[0].strip()
        condition[1] = condition[1].strip().replace("\"", "")
        # print(condition)
        i = 0
        for data in employeeData[condition[0]]:
            if condition[1] in data:
                id.append(i)
            i += 1
        # print(id)
    else:
        print("语句语法错误，请重新输入")
    lines = findDataById(id)
    return lines


def findDataById(id):
    result = {}
    if not id:
        print("未找到记录，请重新尝试")
    else:
        file = open("employee.txt", "r", encoding="utf-8")
        i = 0
        for line in file:
            if i in id:
                result[i] = line
            i += 1
        file.close()
    return result


def findFunction(sql, employeeData):
    if "add" in sql:
        addData(sql, employeeData)
    elif "where" in sql:
        if "del from staff " in sql:
            delData(sql, employeeData)
        elif "UPDATE staff_table SET " in sql:
            updateData(sql, employeeData)
        elif "find" == sql.split(" ")[0]:
            findData(sql, employeeData)
        else:
            print("查询语句语法错误，请重新输入")
    else:
        print("查询语句语法错误，请重新输入")


employeeData = loadData()
while True:
    sql = input("请输入查询语句：").strip()
    findFunction(sql, employeeData)
