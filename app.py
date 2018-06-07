from flask import Flask, render_template, request
from flask import redirect, url_for
from config.verify import RegistrationForm
from config.sql_manager import create_userinfo, found_userinfo
# from sql_manager import reset_userinfo, drop_userinfo
from flask_wtf import CSRFProtect
from config import csrf_config
app = Flask(__name__)

# 防止csrf攻击
app.config.from_object(csrf_config)
CSRFProtect(app)


# 简单的访问
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # csrf验证
    form = RegistrationForm(request.form)
    if request.method == "GET":
        return render_template("login.html", form=form)
    else:
        # 和数据库比对用户名密码
        print(form.username.data)
        userdata = found_userinfo(form.username.data)
        # print(userdata.username)
        if userdata:
            if userdata.password == form.password.data:
                return redirect(url_for("index"))
            else:
                form.password.errors = "密码错误!!!"
                return render_template("login.html", form=form)
        else:
            form.username.errors = "用户名不存在!!!"
            return render_template("login.html", form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    # csrf验证
    form = RegistrationForm(request.form)
    if request.method == "GET":
        return render_template("register.html", form=form)
    else:
        if form.validate():
            username = form.username.data
            password = form.password.data
            email = form.email.data
            result = create_userinfo(username=username, password=password, email=email)
            print("恭喜:%s,注册成功" % result)
            return redirect(url_for("login"))
        else:
            print(form.errors)
            return render_template("register.html", form=form)


@app.route('/index', methods=['GET', 'POST'])
def index():
    # if request.method == "POST":
    #     return render_template("index.html")
    # else:
    #     return None
    return render_template("index.html")


@app.route('/zoo/', methods=['GET'])
def zoo():
    if request.method == "GET":
        return render_template("zoo.html")
    else:
        return None


@app.route('/info/', methods=['GET'])
def info():
    if request.method == "GET":
        return render_template("info.html")
    else:
        return None


@app.route('/tickets/', methods=['GET'])
def tickets():
    if request.method == "GET":
        return render_template("tickets.html")
    else:
        return None


@app.route('/events/', methods=['GET'])
def events():
    if request.method == "GET":
        return render_template("events.html")
    else:
        return None


@app.route('/gallery/', methods=['GET'])
def gallery():
    if request.method == "GET":
        return render_template("gallery.html")
    else:
        return None


@app.route('/contact/', methods=['GET'])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        return None


@app.route('/live/', methods=['GET'])
def live():
    if request.method == "GET":
        return render_template("live.html")
    else:
        return None


@app.route('/blog/', methods=['GET'])
def blog():
    if request.method == "GET":
        return render_template("blog.html")
    else:
        return None


if __name__ == "__main__":
    app.debug = True
    app.run()
