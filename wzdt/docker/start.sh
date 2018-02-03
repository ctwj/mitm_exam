if [ ! -f "/kerwin/startservice.sh" ];then
echo '启动脚本不存在,请手动启动'
else
chmod +x /kerwin/startservice.sh
/kerwin/startservice.sh
fi