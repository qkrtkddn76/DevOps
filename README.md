# DevOps
20220223 DevOps

## 해야할 일
- 1.Git Commit하기
- 2.Git Push하기
- 퇴근하기

## 초기 설정
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

## 이슈1 헬프 답
- 
- 

## Jenkins에서 커버리지 표현하기
### Coverage 설치
- 빋르  > Execute Windows batch command
 coverage run -m unittest discover
 coverage xml -o coverage.xml
### Cobertura 플러그인 설치
- 빌드 후 조치 > Publish Cobeertura Coverage report
  **/coverage.xml
