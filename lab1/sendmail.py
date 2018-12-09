from gmail import GMail, Message
from random import randint
sickness_list = ["trĩ", "đau bụng", "tiêu chảy", "thương hàn"]
i = randint(0, len(sickness_list) - 1)


#1. Select a sickness randomly
sickness = sickness_list[i]


html_template = '''
<p>Ch&agrave;o sếp,</p>
<p style="padding-left: 30px;">Ng&agrave;y mai em bị <strong>{{sickness}}</strong>, xin sếp cho em nghỉ 1 h&ocirc;m ạ.</p>
<p>Em cảm ơn&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></p>
'''
#2. Sickness + html_template => html_content
#Hint: gg: string replace

html_content = html_template.replace("{{sickness}}", sickness)

gmail = GMail('Trung<trngle0409@gmail.com>','colenemmei')
msg = Message('Đơn xin nghỉ ốm',to='c4e.techkidsvn@gmail.com>',html=html_content)
gmail.send(msg)