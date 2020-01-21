# Git Basic

---

> Git은 분산형 버전 관리 시스템이다.
>
> 소스코드의 이력을 확인하고, 협업관계에서 활용할 수 있다.



## 1. 기본 설정

---

* 윈도우에서 Git을 활용하기 위해서는 `git bash`가 필요하다.

  * [Git for Windows](https://gitforwindows.org/)

* 기본적으로 소스코드의 버전 정보를 기록하는 작성자(Author) 설정이 필요하다.

  ```bash
  $ git config --global user.name "Donghyeok-Lee"
  $ git config --global user.email "lee33843@gmail.com"
  ```

* 설정한 작성자 정보를 확인하기 위해서 아래 명령어를 실행한다.

  ```bash
  $ git config --global -l
  user.email=lee33843@gmail.com
  user.name=Donghyeok-Lee
  ```

### gitignore

> 프로젝트를 진행할 때, 개발 환경 혹은 프로젝트 사정 상 git으로 관리될 필요가 없거나 올라가면 안되는 파일이 있다. 이러한 파일들은 `.gitignore`에 입력한다. 

* 프로젝트 루트 경로에 위치시키는 것이 기본이지만, 하위 경로에 위치시켜도 하위 경로 기준으로 gitignore 설정이 적용된다.

* 프로젝트를 시작할 때 어떠한 내용을 적어야 할 지 모를 경우 [gitignore.io](https://www.gitignore.io/)에서 확인한다.

  ![image-20200121093635651](images/image-20200121093635651.png)





## 2. 로컬 저장소 활용법

### 2.1 Git 저장소 설정

특정 프로젝트 폴더에서 git을 활용하기 위해서 아래 명령어를 실행한다.

``` bash
$ git init # git으로 관리하도록 초기화
Initialized empty Git repository in C:/Users/multicampus/Desktop/이동혁/test/.git/
```

* `git init`이 정상적으로 완료되면, 루트 경로에 `.git`이라는 숨김 폴더가 생성된다. 앞으로 git 관련 모든 동작들은 이 폴더에 기록된다.

  ```bash
  $ ls -al
  total 4
  drwxr-xr-x 1 multicampus 197121 0  1월 21 09:39 ./
  drwxr-xr-x 1 multicampus 197121 0  1월 21 09:38 ../
  drwxr-xr-x 1 multicampus 197121 0  1월 21 09:39 .git/ # <- .git폴더
  ```

* git bash에서 (master)라는 브랜치 정보가 표기된다.

  ```bash
  multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/이동혁/test (master)
  ```

  

* `touch` 명령어를 통해 파일을 생성할 수 있다.

  ```bash
  $ touch c.txt # c.txt 파일 생성
  ```

  

### 2.2 add

> git에서 커밋을 하고 싶은 파일을 `staging area`로 이동시키는 명령어다.

```bash
$ git add a.txt		# 특정 파일을 add -> stage
$ git add images/	# 특정 폴더를 add -> stage
$ git add .			# 모든 파일 및 폴더를 add -> stage
```



#### add 이전 상태

추적하고 있지 않은 파일이 있다고 말해주고 있으며, 친절하게 git add 명령어를 작성해보라고 권유하기까지 한다.

```bash
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt
        b.txt

nothing added to commit but untracked files present (use "git add" to track)
```



#### add 이후 상태

add를 한 파일은 초록색 색상으로 commit할 준비가 되었다고 말해주고 있고, add를 하지 않은 파일은 여전히 빨간 색상으로 추적하지 않는 파일이라고 말해준다.

```bash
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        b.txt
```

따라서 git 작업을 할 때 항상 `git status` 명령어를 통해서 현재 상태를 확인해야 한다.



## 3. Commit

> 실제 Git을 통해 이력(버전)을 남기기 위해서는 `커밋(commit)`을 해야한다.

* 커밋을 남길 때는 항상 커밋 메시지를 작성한다. 메시지는 해당 이력에 대한 정보를 가지고 있다.

  ```bash
  $ git commit -m "적절한 commit message 작성"
  [master (root-commit) f6def5e] 작업 파일 추가
   2 files changed, 0 insertions(+), 0 deletions(-)
   create mode 100644 a.txt
   create mode 100644 b.txt
  ```

* 커밋 이력을 확인하기 위해서는 아래 명령어를 실행한다.

  ```bash
  commit f6def5ee8944767f0eb3d6e71d40bba679c6a0da (HEAD -> master)
  Author: Donghyeok-Lee <lee33843@gmail.com>
  Date:   Tue Jan 21 09:49:24 2020 +0900
  
      작업 파일 추가
  ```

  ```bash
  $ git status
  On branch master
  nothing to commit, working tree clean
  ```

* 이후 변경 사항이 발생하면 `add` -> `commit`을 진행한다.

  * `add` : 커밋할 대상 파일을 선정하는 작업
* `commit` : 이력을 확정하는 작업
  


* commit 잘못 친 경우 (vim으로 진입)
  * `i` 눌러서 입력, `esc` 눌러서 나오고, `wq` 쳐서 저장

    

## 4. 원격 저장소(Remote Repository) 활용하기

> Git != Github
>
> Git을 기반으로 원격 저장소를 제공해주는 서비스는 다양하다.
>
> 우리는 가장 인기있는 서비스인 Github을 기준으로 활용해보자.

## 4.1 기본 설정

#### 1) 원격 저장소 설정

원격 저장소(remote)를 `origin`이라는 이름으로 `github_URL`을 설정한다. 

* `origin`말고 원하는 이름을 설정해도 되지만, 일반적으로 `origin`을 사용한다.

```bash
$ git remote add origin github_URL
```

아래 명령어를 통해 저장된 원격 저장소 목록을 확인할 수 있다.

```bash
$ git remote -v

origin  https://github.com/Donghyeok-Lee/test1.git (fetch)
origin  https://github.com/Donghyeok-Lee/test1.git (push)
```

잘못 설정한 경우, 아래 명령어를 통해 삭제 가능하다.

```bash
$ git remote rm origin
$ git remote -v
```

## 4.2 Push

> 원격 저장소에 업로드하기 위해서 `push` 명령어를 사용한다.

`origin`으로 설정된 원격 저장소에 push한다. (==업로드한다.)

```bash
$ git push -u origin master

Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 235 bytes | 235.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/Donghyeok-Lee/test1.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```



작업하기 전에 `git pull`, 작업 끝나면 `git push`를 잊지 않도록 하자 :)



#### 파일 수정 후 

> 파일이 수정되었다는 정보를 알려 줌

```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

* 이후 `add` -> `commit`

  ```bash
  $ git commit -m "기능 추가"
  [master 4a27bbb] 기능 추가
   1 file changed, 1 insertion(+)
  ```

  

`README.md` 넣을때 `-u` 안 쓴 이유

`-u` : Default 값 설정, 자동으로 origin으로 업로드 되도록 설정

그 다음부터 origin에 올리고 싶다면 `git push`만 쳐도 됨



### Github 연결 순서

[로컬]

- 새로운 폴더 생성
- git으로 관리 선언 `->` git init
- 작업 파일 생성 `->` touch app.py # 공부한 파일
- git으로 관리할 파일 추가 `->` git add
- 파일들에 대한 커밋(버전) 남기기 -> git commit

[Github]

- 관리할 Repo 생성

[로컬]

- 원격 저장소 연결 `->` git remote add origin GithubURL
- 원격 저장소 업로드 `->` git push origin master



* 로컬.git에는 연결된 주소가 저장되어 있음
  * git remote -v 로 확인 가능



* `URL` 잘못 친 경우 (잘못 연결한 경우)
  * git remote rm origin `=>` 연결된 origin 주소 없애기



### clone

> Romote Repo(Github)에 있는 파일을 복제해오는 명령어
>
> clone 해온 경우 git init 필요 X(.git도 같이 옴)
>
> <u>clone 최초에 한 번</u>



사용법 : git clone https://github.com/Donghyeok-Lee/test.git 등



Github의 settings - Collaborators 에서 설정해줘야 clone, push, pull 할 수 있음





[실습]

[SSAFY]

- d.txt 생성
- add, commit, push

[Home]

* 원격 저장소에서 최신 자료 불러오기 (pull)
* e.txt 생성
* add. commit, push

[SSAFY]

* 원격 저장소에서 최신 자료 불러오기




