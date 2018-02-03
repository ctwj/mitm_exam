echo 'start web'
python /kerwin/test.py  &
echo 'start proxy'
mitmdump -s /kerwin/wzdt.py