# dnsbench

DNS Bench is a simple tool to benchmark various DNS servers from your network
to see which would be the optimal choice for you.  DNS reolution times have an
impact on how we perceive internet  is "fast" or "slow".  Leveraging a better
DNS improves your overall network experience.  Read about the details of [My journey
on tweaking my DNS](https://www.vivekv.info/posts/dnsbench/).

# Installation and Running
This is a simple python script that uses the python-dns module.  I use
[poetry](https://python-poetry.org/) for my module management and you will find
the TOML and the lock files along with the code.   

if you are familar with poetry, you can get it going with 
    `poetry install`

followed by 
    `poetry run python ./bench.py`

The program's output is self explanatory.

