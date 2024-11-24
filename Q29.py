def includeTAX(itemprice,tax):
    withTax= itemprice*((100+tax)/100)
    return withTax

print(includeTAX(200,14))