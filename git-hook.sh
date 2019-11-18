echo "#!/bin/sh
flake8 --filename=*.py ./app" >> .git/hooks/pre-commit

chmod 777 .git/hooks/pre-commit
