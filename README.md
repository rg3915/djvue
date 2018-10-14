# djvue

Project using Django (without DRF) and VueJS based in [evolutio/djavue](https://github.com/evolutio/djavue).


## Como contribuir?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/djvue.git
cd djvue/backend
python3 -m venv .venv
source .venv/bin/activate
pip install --U pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python create_data.py
python manage.py runserver
```

Já temos um superuser cadastrado:

```
user: admin
pass: d
```

Abra outro terminal e rode a parte do frontend:

```
cd ../frontend
npm i
npm run dev
```
