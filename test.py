from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建Flask应用实例并配置数据库
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # 数据库文件位于项目根目录
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁用警告

# 初始化数据库对象
db = SQLAlchemy(app)


# 定义数据模型（以用户模型为例）
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)


# 创建数据库表（在应用上下文中执行）
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    # 示例：插入和查询数据
    new_user = User(username='john', email='john@example.com')
    db.session.add(new_user)
    db.session.commit()

    users = User.query.all()
    return f"总用户数：{len(users)}"


if __name__ == '__main__':
    app.run(debug=True)
