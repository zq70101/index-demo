#!/usr/bin/expect
set p "[ lindex $argv 0 ]"
spawn scp 
set timeout 600
expect {
"Password:" { send "$p\r"}
"yes/no" { send "yes\r"; exp_continue}
"'s password:" { send "$p\r"}
}
expect {
"*No such file or directory" { exit 1 }
eof { send_user "expect read scp eof"; exit 0}
timeout {exit 2}
}
exit 0
