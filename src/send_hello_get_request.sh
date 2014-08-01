#!/bin/bash
printf "running curl http://127.0.0.1:8080/hello/ -D - &\n"
time curl http://127.0.0.1:8080/hello/ -D - &
printf "running curl http://127.0.0.1:8080/hello/ -D - \n"
time curl http://127.0.0.1:8080/hello/ -D - 
