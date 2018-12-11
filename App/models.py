from App.ext import db


# 用户
class User(db.Model):
    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(128), unique=True)
    u_password = db.Column(db.String(256), unique=True)
    u_nikename = db.Column(db.String(128))
    u_sex = db.Column(db.String(32), default='男')
    phone = db.Column(db.String(32))
    funs = db.Column(db.Integer)
    focus = db.Column(db.Integer)
    dynamics = db.Column(db.Integer)
    u_hot = db.Column(db.Integer)
    u_walk = db.Column(db.String(32))
    u_icon = db.Column(db.String(128), default=None)
    u_com = db.relationship('Community', backref='user')
    u_col = db.relationship('Collection', backref='user')
    u_comment = db.relationship('Comment', backref='user')
    u_order = db.relationship('Order', backref='user')
    u_cou = db.relationship('Course', backref='user')



# 课程
class Course(db.Model):
    cou_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 课程名
    cou_name = db.Column(db.String(256), unique=True)
    # 课程图片
    cou_img = db.Column(db.String(128), default=None)
    # 几人正在训练
    cou_peple_num = db.Column(db.Integer)
    # 参加人数
    cou_join_pep = db.Column(db.String(32))
    # 0为全部，1为健身，2为跑步，3为瑜伽,4运动课程、5健身计划
    cou_group_id = db.Column(db.Integer)
    # 课程时长
    cou_time = db.Column(db.String(32))
    # 消耗卡路里
    cou_kli = db.Column(db.String(32))
    # 评级
    cou_rate = db.Column(db.String(32))
    cou_user=db.Column(db.ForeignKey('user.u_id'))

# 文章
class Article(db.Model):
    a_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 内容
    a_content = db.Column(db.String(1024))
    # 阅读数量
    a_read = db.Column(db.Integer)
    # 分享数量
    a_share = db.Column(db.Integer)
    # 上传时间
    a_puttime = db.Column(db.String(32))
    # 标签
    a_tag = db.Column(db.String(32))
    # 标题
    a_title = db.Column(db.String(128))
    # 图片
    a_img = db.Column(db.String(128))

class ArticleUser(db.Model):
    art_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    art_user = db.Column(db.Integer,db.ForeignKey('user.u_id'))
    art_article = db.Column(db.Integer, db.ForeignKey('article.a_id'))
# 食材
class Food(db.Model):
    foodid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    foodimg = db.Column(db.String(128))
    foodname = db.Column(db.String(32))
    # 食材分类，0为肉禽类，1为水产类，2为蔬菜类，3为果品类
    foodgroup = db.Column(db.Integer)


# 菜谱
class Menu(db.Model):
    menuid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menuname = db.Column(db.String(64))
    menuimg = db.Column(db.String(128))
    # 0为汤羹，1为小吃，2为主食
    menugroup = db.Column(db.Integer)


# 话题
class TopiClassify(db.Model):
    topicid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    topicname = db.Column(db.String(64))
    topicimg = db.Column(db.String(128))
    # 底部标注
    topicbottom = db.Column(db.String(128))
    # 参与评论的人数
    topic_com_num = db.Column(db.String(64))


# 评论
class Comment(db.Model):
    com_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    com_content = db.Column(db.String(256))
    comment_user = db.Column(db.Integer, db.ForeignKey('user.u_id'))


# 商品
class Goods(db.Model):
    g_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(256), unique=True)
    g_img = db.Column(db.String(128), default=None)
    # 0为跑步机，1为瑜伽，2为视频，3为助眠
    good_group_id = db.Column(db.Integer)
    g_price = db.Column(db.String(32))


# 收藏
class Collection(db.Model):
    col_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    col_name = db.Column(db.String(128))
    col_img = db.Column(db.String(128), default=None)
    # 判断是属于0运动，1食品，2视频的哪一类
    col_group_id = db.Column(db.Integer)
    col_user = db.Column(db.Integer, db.ForeignKey('user.u_id'))


# 社区
class Community(db.Model):
    com_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    com_title = db.Column(db.String(32))
    com_img = db.Column(db.String(128), default=None)
    com_bottom = db.Column(db.String(128))
    com_user = db.Column(db.Integer, db.ForeignKey('user.u_id'))


# 轮播图
class Swiper(db.Model):
    swi_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    swiper = db.Column(db.String(128), default=None)


# 图片
class Mainimg(db.Model):
    mid_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mid_img = db.Column(db.String(128), default=None)
    mid_type = db.Column(db.String(32), default=None)
    mid_title = db.Column(db.String(32), default=None)


# 动作训练
class ExerciseAct(db.Model):
    act_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    act_img = db.Column(db.String(128))
    act_title = db.Column(db.String(32), default=None)


# 动作库
class Act(db.Model):
    actid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actimg = db.Column(db.String(128))
    acttitle = db.Column(db.String(32))


# 购物车
class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_user = db.Column(db.Integer, db.ForeignKey('user.u_id'))
    cart_goods = db.Column(db.Integer, db.ForeignKey('goods.g_id'))
    is_choosed = db.Column(db.Boolean, default=True)


# 订单
class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 订单号
    order_num = db.Column(db.String(128))
    # 是否支付,0为待支付，1为代签收，2为已经支付
    is_pay = db.Column(db.Integer)
    u_id = db.Column(db.Integer, db.ForeignKey('user.u_id'))


# 支付与商品关系
class OrderGoods(db.Model):
    ordgood_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    good_id = db.Column(db.Integer, db.ForeignKey('goods.g_id'))
