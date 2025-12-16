# Fish Shell

> PNG Export Size: `8.27 width` x `11.7 height` at `300dpi`

Fish is a terminal similar to Bash (Bourne Again SHell) and Zsh (Z Shell)

Some of the best features of Fish shell are Autosuggestions, Syntax Highlighting, Maths/Calculator, Search Functionality, and Abbreviations. Some of the Abbreviations I use are given below

## Abbreviations

It can be added at `/home/username/.config/fish/config.fish` (This is created as separate file for me)

---

### General Commands

* s - `sudo`

* c - `clear`

* e - `exit`

* d - `docker`

* g - `git`

* de - `deactivate`

* c. - `code .`

* hg - `history | grep`

* upd - `sudo apt-get update`

* upg - `sudo apt-get upgrade`

---

### Conda Commands

* ca - `conda activate`

* cde - `conda deactivate`

* cenv - `conda env list`

* ccr - `conda create -n <env_name> python=3.11 -y`

* cexp - `conda env export --name <env_name> > <filename>.yml`

* crm - `conda remove -n <env_name> --all -y`

---

### SSH Commands

* sr - `ssh appuser@192.168.1.230`

* sl - `ssh appuser@192.168.1.228`

---

### Docker Commands

* dps - `docker ps`

* di - `docker images`

* dex - `docker exec -it`

* dst - `docker start`

* ds - `docker stop`

* dc - `docker compose`

* dv - `docker volume`

* dn - `docker network`

* dl - `docker logs`

* db - `docker build`

* drm - `docker rm`

* drmi - `docker rmi`

* dbp - `docker builder prune`

---

### Python Commands

* pyt - `python`

* p3 - `python3`

* pi - `pip install`

* pu - `pip uninstall`

* psh - `pip show`

---

### UV Commands 

* ui - `uv init`

* ua - `uv add`

* ur - `uv remove`

* up - `uv pip`

* upl - `uv pip list`

* usv - `uv self version`

* ut - `uv tree`

---

### NVIDIA Commands

* ns - `nvidia-smi`

* wns - `watch nvidia-smi`

* nvc - `nvcc --version`

---

### Jupyter Commands

* jn - `jupyter notebook`

* jns - `jupyter notebook --ip 192.168.1.229 --port 8887 --no-browser`

---

### Ollama Commands

* os - `ollama show`

* orun - `ollama run`

* ol - `ollama list`

* ops - `ollama ps`

* orm - `ollama rm (remove)`

---

### Git Commands

* ga - `git add`

* gc - `git commit -m ""`

* gph - `git push`

* gpl - `git pull`

* gcl - `git clone`

* gs - `git status`

* gb - `git branch`

* gi - `git init`

* gr - `git revert`

* gst - `git stash`

* gch - `git checkout`

* gl - `git log`

* gacp - `git add commit & push`

* glg - `git log --oneline --graph --all`

---

### Long Commands

* fi - `find ./<filename> -type f > <filename>.txt`

* pcopy - `time cat <filename>.txt | parallel -j 10 -X -n 1 rsync -av --inplace {} ./<dest_dir_name>`

* sc - `scp <files> appuser@192.168.1.XXX:/home/appuser/LOCATION`
