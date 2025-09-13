#!/usr/bin/env sh

echo "Hello World!"

cd python
python3 -m venv my_venv
source ./my_venv/bin/activate
# pip install -r requirements.txt
# for c in {1..10}
for c in 1
do
    echo "Running Gaussian Elimination experiment for range: -$c to $c ..."
    python main.py -loA -$c -hiA $c -lob -$c -hib $c
done
deactivate
cd ..
