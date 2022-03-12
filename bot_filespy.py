from botoy import GroupMsg, Action, decorators, jconfig
from botoy.contrib import plugin_receiver
from botoy.parser import group as gp

__doc__ = "监听群消息并转发到指定qq"

master = jconfig.master


@plugin_receiver.group
@decorators.ignore_botself
def file_spy(ctx: GroupMsg):
    action = Action(ctx.CurrentQQ)
    file_data = gp.file(ctx)
    if file_data is not None:
        file_id = action.getGroupFileURL(
            group=ctx.FromGroupId, fileID=file_data.FileID)
        file_name = file_data.FileName
        file_size = file_data.FileSize
        address = f"文件名:\n{file_name}\n文件大小{round(file_size/1024/1024, 2)}MB\n来自群:{ctx.FromGroupName}({ctx.FromGroupId})\n来自用户:{ctx.FromNickName}({ctx.FromUserId})\n下载地址:\n{file_id['Url']}"
        action.sendFriendText(user=master, content=address)
