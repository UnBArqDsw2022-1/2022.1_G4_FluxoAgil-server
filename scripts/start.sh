# https://intoli.com/blog/exit-on-errors-in-bash-scripts/# 
# Este script é interrompido se qualquer comando der errado
set -e

printf ">>> Create database"
python -m fluxoagil.db.create_database

printf ">>> Start database"
python -m fluxoagil.db.seed

printf ">>> Start database"
python main.py
