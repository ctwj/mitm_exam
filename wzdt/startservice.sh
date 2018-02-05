echo 'start web'
python /kerwin/webserver.py  &
echo 'start proxy'
mitmdump -s /kerwin/wzdt.py