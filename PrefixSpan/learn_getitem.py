"""
将老人基本信息，先测试写入文本，再写入数据库！
"""
import pymongo


class GetItem:

    # 全局变量
    varString = "admin你好！"

    # 构造函数
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.name = 'admin'
        # 连接指定IP地址的数据库
        self.client = pymongo.MongoClient("127.0.0.1", 27017)

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")
        self.client.close()

    @classmethod
    def test2(cls):
        print(cls)
        print('test2')
        print('----------------')

    # 查询所有collections
    def find_all(self):
        # 选择数据库
        db = self.client.yanglao
        # 使用集合(表)
        collection = db.fp_trans_p1
        # 查询所有
        for data in collection.find():
            print(data)
        print("总记录数为：", collection.find().count())

    def find_one(self):
        # 选择数据库
        db = self.client.get_database("yanglao")
        collection = db.get_collection("fp_trans_p1")
        # var_cursor = collection.find({"pPer_id": self.uid}).limit(100)  # 查找一个人的所有记录
        var_cursor = collection.find().limit(300)  # 查找一个人的所有记录
        cursor_count = var_cursor.count()
        var_list = list(range(0, cursor_count, 1))
        print("var_list:", var_list, ", \nvar_cursor_count:", var_cursor.count())
        myslice = slice(5, 20)  # 切片函数
        print(myslice)
        print(var_list[myslice])
        var_doc = var_cursor.__getitem__(myslice)
        print("var_doc:", var_doc)
        for var_doc_slice in var_doc:
            print("var_doc_slice_id:", var_doc_slice.get("_id"))

    def find_one_scan_fp(self):
        db = self.client.get_database("yanglao")
        collection = db.get_collection("fp_trans_p1")
        # var_cursor = collection.find({"pPer_id": self.uid}).limit(100)  # 查找一个人的所有记录
        trans_no = 9
        start_index = 20
        var_cursor = collection.find({"trans_no": trans_no, "_id": {"$gte": start_index}})
        for var_doc in var_cursor:
            print("_id:", var_doc.get("_id"))


if __name__ == '__main__':
    gt = GetItem()
    # gt.find_one()
    gt.find_one_scan_fp()
