# SKKU-SMR-FileSystem

실험 방법

1. setup.sh을 실행시켜서 필요 프로그램들을 설치한다.

2. /dev/sda에 SMR-HDD를 놓고 parted를 사용해서 파티션을 만들어놓는다.

3. 측정하고 싶은 파일시스템에 맞춰서 postmark-<filesystem name> 을 실행한다. 
mkfs후 persistent cache를 비우기 위해서 2시간 동안 sleep한다.

1) blktrace를 사용하여 측정할 경우 터미널 하나를 띄운뒤에 blktrace -d /dev/sda를 실행시키고 postmark-blktrace.sh를 실행한다.

2) ftrace를 사용하여 측정할 경우 터미널 하나를 띄운뒤에 trace-cmd report -e block_rq_complete /dev/sda를 실행시키고 postmark-ftrace.sh를 실행한다.

이때 각 측정결과에 맞도록 쉘 프로그램의 경로들을 살짝씩 바꿔준다.

4. postmark 결과를 result 폴더에서, disk offset에 관련된 graph폴더에서 확인한다.
