#/usr/bin/sh
testlist="1 10 100 1000 10000"
for i in $testlist;  do
    webbench -c $i --get http://localhost:8080/  > nginx_$i.result
    webbench -c $i --get http://localhost:80/  > apache_$i.result
done
