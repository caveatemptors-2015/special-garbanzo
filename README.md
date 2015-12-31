# portfolioX

## setting up your development environment

First, clone the project and create your branch.
```bash
git clone https://github.com/caveatemptors-2015/special-garbanzo.git
git checkout -b <my_name>
```

Second, install your virtual environment in the /project directory (the one
containing `LICENSE`, `README.md`, and `requirements.txt`). Then pip install
necessary modules from requirements.txt.

```bash
cd project
virtualenv env
pip install -r requirements.txt
```

Third, create the file /project/project/secret.py to include a secret key. It
ought to look like this:

```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k4cp8vc9vgy!3&2jh#1tomztm2o^7kkz&%qdp0jr6!mle*@g(d'
```

You can copy/paste SECRET_KEY from any of your old /project/project/settings.py
files. If you copy/paste the example it will probably also work, but that's a bad
idea (because this README is not a *SECRET*).

We move our SECRET_KEY from it's traditional home in `/project/project/settings.py`
to our special file `/project/project/secret.py` so that we may place
`secret.py` in our `.gitignore`, thus preventing it from being added to our
repositories and making our SECRET_KEY public.

### TODO: Database setup instruction.
