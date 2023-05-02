import hashlib
import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_login.settings'

if __name__ == '__main__':

    # subject, from_email, to = '来自www.liujiangblog.com的测试邮件', 'a357965604@sina.com', '357965604@qq.com'
    # text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    # html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
    # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()

    def hash_code(s, salt='mysite'):
        h = hashlib.sha256()
        s += salt
        h.update(s.encode())
        return h.hexdigest()

    def md5_code(s):
        h = hashlib.md5()
        h.update(s.encode())
        return h.hexdigest()
    print(md5_code('123456'))