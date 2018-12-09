from gmail import GMail, Message
import datetime

html_content = '''
<p>Ch&agrave;o sếp Huy,</p>
<p>Em l&agrave; <strong>L&ecirc; Th&agrave;nh Trung</strong> học lớp <strong>C4E24</strong>. H&ocirc;m nay em vừa đi kh&aacute;m, b&aacute;c sĩ bảo em sẽ bị <strong>đau bụng</strong> v&agrave;o mai. Mặc d&ugrave; rất muốn đi học nhưng em n&ecirc;n nghe theo lời b&aacute;c sĩ.</p>
<p>Em l&agrave;m đơn n&agrave;y xin ph&eacute;p sếp cho em được nghỉ ng&agrave;y mai ạ.&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></p>
<p>Em cảm ơn.</p>
'''

gmail = GMail('Trung<trngle0409@gmail.com>','colenemmei')
msg = Message('Lê Thành Trung - Đơn xin nghỉ ốm',to='c4e.techkidsvn@gmail.com>',html=html_content)

now = datetime.datetime.now()
if now.hour >= 7:
    gmail.send(msg)
else:
    print("Wait until 7AM!")