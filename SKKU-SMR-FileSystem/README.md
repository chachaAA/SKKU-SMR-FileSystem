#실험 시스템 환경


kernel : linux-4.6.0 
OS : Ubuntu 14.04 

linux-4.6.0은 kernel.org에서 받아서 사용하였고
ext4를 수정한 ext4-lazy를 적용하기 위해서 patch 파일을 사용해서
linux-4.6.0-lazy 커널을 만들었다.


실험을 하기전에 미리 linux-4.6.0 커널에서 postmark 폴더 안의 설명대로 설치를 다 맞춰놓고 ext4를 실험한 다음
linux-4.6.0-lazy 커널을 빌드해서 실험을 수행하는 것이 좋아보인다.
