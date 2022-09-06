# https://intoli.com/blog/exit-on-errors-in-bash-scripts/# 
# Este script é interrompido se qualquer comando der errado
set -e

python -m fluxoagil.db.create_database

python main.py
