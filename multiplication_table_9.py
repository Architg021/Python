
for i in range(2, 21):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:#before tables this is an  f string
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write('\n')
