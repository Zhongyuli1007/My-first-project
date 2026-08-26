# Git 学习笔记：第一天

日期：2026-08-25

## 1. PowerShell 基础

PowerShell 是 Windows 的命令行工具和脚本语言。Git 是在 PowerShell 中运行的版本管理程序。

```powershell
Get-Location             # 查看当前目录
Get-ChildItem            # 查看文件，也可以使用 ls
cd "D:\ChatGPT\project test learn git"  # 进入指定目录
cd ..                    # 返回上一级目录
cd \                     # 返回当前磁盘根目录
```

`Get-ChildItem` 输出中的 `Mode` 表示文件类型和属性：

- `d`：目录（directory）
- `a`：存档属性（archive）
- `h`：隐藏（hidden）
- `r`：只读（read-only）

## 2. Git、GitHub 和 GitLab

- Git：安装在电脑上的版本管理工具，可以离线工作。
- GitHub：托管 Git 仓库的在线平台。
- GitLab：与 GitHub 类似，也支持团队协作、代码审查和 CI/CD，常用于企业和私有部署。

Git 不依赖 GitHub。GitHub 和 GitLab 都只是 Git 可以连接的远程仓库平台。

## 3. Git 的核心模型

```text
工作区 --git add--> 暂存区 --git commit--> 本地仓库
```

- 工作区：正在编辑的文件。
- 暂存区：准备放入下一次提交的修改。
- 本地仓库：保存提交历史的 `.git` 目录。
- commit：一个可追踪的版本快照。

`.git` 是 Git 的内部数据目录，不要手动修改或删除。

## 4. 初始化和查看状态

```powershell
git init
git status
```

- `git init`：把当前目录初始化为 Git 仓库。
- `git status`：查看当前分支，以及哪些文件未跟踪、已修改或已暂存。

常见状态：

- `Untracked files`：Git 尚未跟踪的新文件。
- `Changes not staged for commit`：文件已修改，但尚未暂存。
- `Changes to be committed`：修改已暂存，将进入下一次提交。
- `working tree clean`：工作区没有未提交的修改。

## 5. Git 身份配置

```powershell
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

查看配置：

```powershell
git config user.name
git config user.email
git config --global --list
git config --list --show-origin
```

`user.name` 是提交中显示的作者名，不必和 GitHub 用户名一致。`user.email` 最好使用 GitHub 账号中已验证的邮箱，以便 GitHub 正确关联提交。

Git 提交身份与网站登录认证是两回事：

- 姓名和邮箱：记录提交作者。
- 密码、令牌或 SSH 密钥：证明是否有权限访问远程仓库。

## 6. 修改、暂存和提交

```powershell
git status
git diff
git add README.md
git diff --staged
git commit -m "清楚描述本次修改"
```

- `git status`：查看哪些文件发生了变化。
- `git diff`：查看尚未暂存的具体变化。
- `git add`：把指定修改放入暂存区。
- `git diff --staged`：查看下一次提交将包含的变化。
- `git commit`：把暂存区保存为一个本地版本快照。

注意：`git add` 不是上传，`git commit` 也不会上传到互联网。

## 7. 查看提交历史

```powershell
git log --oneline
git log --pretty=fuller
git log --oneline --decorate --graph --all
```

每次提交包含：

- 文件修改内容
- 作者和邮箱
- 作者时间和提交时间
- 提交说明
- 上一个提交
- 唯一的提交哈希

概念对应：

```text
commit  = 一个版本存档点
哈希值  = 提交的唯一编号
分支    = 一条开发路线
HEAD    = 当前所在的提交位置
tag     = 某个重要提交的固定版本名
```

## 8. 标签（tag）

标签通常用于标记发布版本：

```powershell
git tag v1.0
git tag
git show v1.0
```

创建带说明的标签：

```powershell
git tag -a v1.0 -m "第一个稳定版本"
```

commit 是日常修改产生的版本；tag 是给某个重要 commit 起的固定名称。

## 9. 分支（branch）

分支用于在不影响主线的情况下独立开发：

```powershell
git branch
git switch -c feature-note
git switch master
```

- `git branch`：查看分支，`*` 表示当前分支。
- `git switch -c feature-note`：创建并切换到新分支。
- `git switch master`：切换回主分支。

切换分支时，Git 会让工作区文件呈现该分支对应的版本。内容暂时消失通常不是文件丢失，而是当前分支不包含那次修改。

## 10. 合并分支（merge）

先切换到接收修改的分支，再合并来源分支：

```powershell
git switch master
git merge feature-note
```

这表示把 `feature-note` 的修改合并到当前 `master`。

如果主分支没有产生新的提交，Git 可能执行 `Fast-forward`（快进合并），即把主分支指针直接移动到较新的提交。

合并后查看历史并删除已完成的分支：

```powershell
git log --oneline --decorate --graph --all
git branch -d feature-note
```

删除已合并的分支名称不会删除已经合并到主分支的提交和文件。

## 11. 日常操作循环

```powershell
git status
git diff
git add 文件名
git diff --staged
git commit -m "说明本次修改"
git log --oneline
```

提交说明应简短、明确，说明这次提交完成了什么。

## 12. 下次学习

下一步学习远程仓库：

- 把默认分支从 `master` 改为 `main`
- 在 GitHub 创建远程仓库
- `git remote`：管理远程仓库地址
- `git push`：上传本地提交
- `git pull`：拉取并整合远程提交
- `git clone`：复制已有的远程仓库
- 处理合并冲突

