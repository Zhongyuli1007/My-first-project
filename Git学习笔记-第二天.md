# Git 学习笔记：第二天

日期：2026-08-26

## 1. 远程仓库

Git 是本地版本管理工具，GitHub 和 GitLab 是托管 Git 仓库的在线平台。

```powershell
git remote -v
git remote add origin https://github.com/用户名/仓库名.git
git remote set-url origin 新地址
git remote remove origin
```

一个本地仓库可以连接多个远程仓库，例如 `origin` 和 `other`。命令中明确写出名称即可切换：

```powershell
git pull origin main
git push other main
```

## 2. clone、fetch、pull、push

第一次下载远程仓库：

```powershell
git clone https://github.com/用户名/仓库名.git
cd 仓库名
```

`clone` 会创建目录、下载文件和历史，并自动配置 `origin`。

只下载远程新历史，不修改当前文件：

```powershell
git fetch origin
```

下载并合并远程更新：

```powershell
git pull
```

可以记作：

```text
git pull = git fetch + git merge
```

上传本地提交：

```powershell
git push
git push -u origin main
```

第一次推送使用 `-u` 建立本地 `main` 和远程 `origin/main` 的跟踪关系。查看跟踪关系：

```powershell
git branch -vv
```

## 3. 远程和本地历史不一致

如果 GitHub 仓库创建时已经有 README，而本地也有独立提交，第一次推送可能提示 `fetch first`。可以先拉取并允许合并独立历史：

```powershell
git pull origin main --allow-unrelated-histories
```

## 4. 合并冲突

`git status` 可能显示：

```text
both added: README.md
```

冲突文件中可能出现：

```text
<<<<<<< HEAD
本地内容
=======
远程内容
>>>>>>> origin/main
```

选择或合并内容，删除这些标记并保存，然后：

```powershell
git add README.md
git commit -m "合并远程仓库内容"
git push
```

放弃未完成的合并：

```powershell
git merge --abort
```

## 5. Git 代理

访问 GitHub 需要代理时，代理软件通常提供本地 HTTP 地址和端口。本次使用的是 `127.0.0.1:7890`：

```powershell
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
git ls-remote origin
```

关闭代理软件后，如果 Git 报代理错误，可以删除配置：

```powershell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 6. `.gitignore`

`.gitignore` 用于忽略不应提交的缓存、IDE 配置、日志和敏感文件：

```gitignore
__pycache__/
*.pyc
.idea/
.env
*.log
```

已经被 Git 跟踪的文件不会因为加入 `.gitignore` 自动停止跟踪。保留本地文件但停止跟踪：

```powershell
git rm --cached .env
git commit -m "停止跟踪环境配置文件"
```

## 7. `git revert`

`revert` 用一个新提交抵消旧提交，适合撤销已经推送到远程的修改：

```powershell
git revert HEAD
git revert --no-edit HEAD
git push
```

```text
revert：增加反向提交，保留完整历史
reset：移动分支指针，通常用于本地修改历史
```

## 8. Git 打开的 Vim 编辑器

执行 `git revert HEAD` 时，Git 可能打开 Vim 编辑提交说明。

```text
Esc → :wq → Enter    保存并退出
Esc → :q! → Enter    不保存并退出
```

## 9. 删除本地仓库

删除本地仓库就是删除项目文件夹和其中的 `.git`，不会影响 GitHub 远程仓库。确认路径后再执行：

```powershell
cd ..
Get-ChildItem .\Notes
Remove-Item -LiteralPath .\Notes -Recurse -Force
```

这是不可逆操作，执行前必须确认目标路径。

## 10. 今日流程

```powershell
git pull
# 修改文件
git status
git diff
git add 文件名
git diff --staged
git commit -m "说明修改"
git push
```

```text
clone：第一次下载
fetch：下载远程历史但不合并
pull：下载并合并
push：上传本地提交
revert：用新提交撤销旧提交
```
